import json
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from risk_controls.pii_filters import contains_pii, redact_pii, detect_pii_types
from datetime import datetime, timezone

# --- Configuration Loading ---

def get_project_root() -> Path:
    """Returns the project root directory."""
    return Path(__file__).parent.parent

def load_config():
    """Loads the main configuration from the YAML file."""
    config_path = get_project_root() / "governance" / "config" / "scope.yaml"
    with config_path.open("r") as f:
        return yaml.safe_load(f)

# Load configuration and environment variables
config = load_config()
bot_config = config.get("bot_config", {})
TICKET_TYPES = config.get("ticket_types", [])
CONFIDENCE_THRESHOLD = bot_config.get("confidence_threshold", 0.5)
MODEL_NAME = bot_config.get("model_name", "gemini-3-flash-preview")

load_dotenv(get_project_root() / ".env")

# --- Gemini API Initialization ---

try:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
except (TypeError, ValueError) as e:
    print(f"Error: Gemini API key not configured. Please set GEMINI_API_KEY in a .env file. Details: {e}")
    client = None

# --- Core Functions ---

def prepare_prompt(ticket_text: str) -> str:
    """Loads the prompt template and formats it with categories and the ticket text."""
    prompt_path = get_project_root() / "prompts" / "classification_prompt.txt"
    with prompt_path.open("r") as f:
        prompt_template = f.read()

    categories_str = ", ".join(TICKET_TYPES)
    return f"{prompt_template.format(categories=categories_str)}\n\nTicket: {ticket_text}"

def invoke_llm(prompt: str) -> dict:
    """Invokes the Gemini model and returns the parsed JSON response."""
    if not client:
        raise ConnectionError("Gemini client is not initialized. Check API key.")

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.1)
        )
        # Extract text from response
        response_text = response.text
        # Assuming response text is a JSON string
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"LLM returned malformed JSON: {response_text}") from e
    except Exception as e:
        raise ConnectionError(f"API call to Gemini failed: {e}") from e

def process_llm_response(result: dict) -> tuple[str, float]:
    """Extracts and validates category and confidence from the LLM response."""
    category = result.get("category", "unknown")
    confidence = result.get("confidence", 0.0)

    if category not in TICKET_TYPES:
        category = "unknown"
        confidence = 0.0 # Confidence is unreliable if category is invalid

    return category, float(confidence)

# --- Escalation Rules ---
# The rules below are declared in governance/config/scope.yaml as plain strings,
# e.g. "if confidence_score < 0.7: escalate_to: human_agent". The parser here
# turns them into evaluators so every classification result carries a routing
# decision instead of the rules living only in documentation.

def _compare(left, op: str, right) -> bool:
    if op == "==":
        return left == right
    if op == "<":
        return left < right
    if op == ">":
        return left > right
    if op == "<=":
        return left <= right
    if op == ">=":
        return left >= right
    return False

def _parse_condition(condition_str: str):
    """Parses a rule condition into a callable evaluated against a result dict."""
    condition_str = condition_str.strip()
    for op in ("==", "<=", ">=", "<", ">"):
        if op in condition_str:
            field, _, value = condition_str.partition(op)
            field = field.strip()
            value = value.strip()
            if field == "confidence_score":
                threshold = float(value)
                return lambda result, f=field, t=threshold, o=op: _compare(float(result.get(f, 0.0)), o, t)
            return lambda result, f=field, v=value, o=op: _compare(str(result.get(f, "")), o, v)
    # Bare flag, e.g. "contains_pii": matches when the flag is truthy.
    field = condition_str
    return lambda result, f=field: bool(result.get(f, False))

def _parse_action(action_str: str) -> str:
    """Parses a rule action such as 'escalate_to: human_agent' into a route name."""
    _, _, route = action_str.strip().partition(":")
    route = route.strip()
    if not route:
        raise ValueError(f"Unparseable escalation action: {action_str!r}")
    return route

def _parse_escalation_rule(rule_str: str):
    """Parses one 'if <condition>: <action>' or 'else: <action>' rule string."""
    text = rule_str.strip()
    if text.startswith("else:"):
        return (lambda result: True), _parse_action(text[len("else:"):]), text
    if text.startswith("if "):
        condition_part, _, action_part = text[len("if "):].partition(":")
        if not action_part:
            raise ValueError(f"Unparseable escalation rule: {rule_str!r}")
        return _parse_condition(condition_part), _parse_action(action_part), text
    raise ValueError(f"Unparseable escalation rule: {rule_str!r}")

def _load_escalation_rules():
    """Parses the escalation_rules list from scope.yaml, skipping malformed entries."""
    parsed = []
    for rule_str in config.get("escalation_rules", []):
        try:
            parsed.append(_parse_escalation_rule(str(rule_str)))
        except ValueError:
            continue
    return parsed

ESCALATION_RULES = _load_escalation_rules()

def evaluate_routing(result: dict) -> dict:
    """
    Applies the escalation rules from governance/config/scope.yaml in order and
    returns the routing decision for a classification result, e.g.
    {"route": "human_agent", "reason": "if confidence_score < 0.7: escalate_to: human_agent"}.
    """
    for condition, route, rule_text in ESCALATION_RULES:
        if condition(result):
            return {"route": route, "reason": rule_text}
    # Fail safe: if no rule matches, escalate to a human.
    return {"route": "human_agent", "reason": "no matching rule; defaulted to human review"}

def classify_ticket(ticket_text: str) -> dict:
    """
    Classifies a support ticket using the Gemini 3 Flash model with governance layers.
    
    Complies with ISO/IEC 42001:2023 requirements for AI system operation and monitoring.
    """
    if not ticket_text or ticket_text.isspace():
        empty_result = {
            "ticket_type": "unknown",
            "confidence_score": 0.0,
            "contains_pii": False,
            "model": MODEL_NAME
        }
        empty_result["routing_decision"] = evaluate_routing(empty_result)
        return empty_result

    category = "unknown"
    confidence = 0.0

    try:
        prompt = prepare_prompt(ticket_text)
        llm_result = invoke_llm(prompt)
        category, confidence = process_llm_response(llm_result)
    except (ConnectionError, ValueError) as e:
        log_llm_error(ticket_text, str(e))
    except Exception as e:
        # Catch-all for unexpected errors during the process
        log_llm_error(ticket_text, f"An unexpected error occurred: {e}")

    # Apply governance layers
    pii_flag = contains_pii(ticket_text)
    
    final_result = {
        "ticket_type": category,
        "confidence_score": round(confidence, 2),
        "contains_pii": pii_flag,
        "model": MODEL_NAME
    }
    final_result["routing_decision"] = evaluate_routing(final_result)

    # Audit logging for low-confidence or failed classifications
    if confidence < CONFIDENCE_THRESHOLD or category == "unknown":
        log_fallback(ticket_text, final_result)

    return final_result

# --- Governance and Auditing ---

def log_entry(log_path: Path, entry: dict):
    """Appends a JSON entry to a specified log file."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a") as f:
        f.write(json.dumps(entry) + "\n")

def log_llm_error(ticket_text: str, error_msg: str):
    """Governance: Log when the AI model fails or returns an invalid response."""
    entry = {
        "error": error_msg,
        "ticket_preview": ticket_text[:100], # Log only a preview
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    log_path = get_project_root() / "governance" / "llm_error_log.jsonl"
    log_entry(log_path, entry)

def log_fallback(ticket_text: str, result: dict):
    """Governance: Log low-confidence or unknown classifications for human review.

    Tickets flagged for PII are logged with personal information redacted; the
    entry records which PII types were found instead of their values, so the
    log file never stores raw personal information.
    """
    pii_flagged = bool(result.get("contains_pii"))
    entry = {
        "ticket": redact_pii(ticket_text) if pii_flagged else ticket_text,
        "result": result,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    if pii_flagged:
        entry["pii_types"] = detect_pii_types(ticket_text)
    log_path = get_project_root() / "fallback_log.jsonl"
    log_entry(log_path, entry)
