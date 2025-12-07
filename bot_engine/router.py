import json
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from risk_controls.pii_filters import contains_pii
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
MODEL_NAME = bot_config.get("model_name", "gemini-1.5-flash")

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

def classify_ticket(ticket_text: str) -> dict:
    """
    Classifies a support ticket using the Gemini 2.5 Flash model with governance layers.
    
    Complies with ISO/IEC 42001:2023 requirements for AI system operation and monitoring.
    """
    if not ticket_text or ticket_text.isspace():
        return {
            "ticket_type": "unknown",
            "confidence_score": 0.0,
            "contains_pii": False,
            "model": MODEL_NAME
        }

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
    """Governance: Log low-confidence or unknown classifications for human review."""
    entry = {
        "ticket": ticket_text,
        "result": result,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    log_path = get_project_root() / "fallback_log.jsonl"
    log_entry(log_path, entry)
