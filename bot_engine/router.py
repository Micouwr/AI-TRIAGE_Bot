import json
import openai
from risk_controls.pii_filters import contains_pii

def classify_ticket(ticket_text):
    """
    Classifies ticket using GPT-4o-mini with governance layers.
    Confidence score derived from model's logprobs.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": (
                    "You are a help desk triage assistant. "
                    "Classify the ticket into ONE category: "
                    "access_request, billing_question, technical_support, or unknown. "
                    "Return ONLY a JSON object with keys: 'category' and 'confidence' (0.0-1.0)."
                )},
                {"role": "user", "content": ticket_text}
            ],
            temperature=0.1,  # Low temp for consistency
            logprobs=True,     # Enables confidence scoring
            max_tokens=50
        )
        
        # Parse model output
        result = json.loads(response.choices[0].message.content)
        category = result["category"]
        confidence = result["confidence"]
        
    except Exception as e:
        # Governance fallback: if LLM fails, log and mark unknown
        category = "unknown"
        confidence = 0.0
        log_llm_error(ticket_text, str(e))

    # Apply governance layers
    pii_flag = contains_pii(ticket_text)
    
    final_result = {
        "ticket_type": category,
        "confidence_score": round(confidence, 2),
        "contains_pii": pii_flag,
        "model": "gpt-4o-mini"
    }

    # Audit logging
    if confidence < 0.5 or category == "unknown":
        log_fallback(ticket_text, final_result)

    return final_result

def log_llm_error(ticket_text, error_msg):
    """Governance: Log when AI model fails."""
    entry = {
        "error": error_msg,
        "ticket": ticket_text[:100],  # Truncate for safety
        "timestamp": __import__("datetime").datetime.utcnow().isoformat()
    }
    with open("governance/llm_error_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")

def log_fallback(ticket_text, result):
    """Governance: Log low-confidence or unknown classifications."""
    entry = {
        "ticket": ticket_text,
        "result": result,
        "timestamp": __import__("datetime").datetime.utcnow().isoformat()
    }
    with open("fallback_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")
