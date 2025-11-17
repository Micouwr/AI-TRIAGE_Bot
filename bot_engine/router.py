import json
import os
import google.generativeai as genai
from risk_controls.pii_filters import contains_pii

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def classify_ticket(ticket_text):
    """
    Classifies ticket using Gemini 1.5 Flash with governance layers.
    """
    try:
        prompt = (
            "You are a help desk triage assistant. "
            "Classify the ticket into ONE category: "
            "access_request, billing_question, technical_support, or unknown. "
            "Return ONLY a JSON object with keys: 'category' and 'confidence' (0.0-1.0)."
        )
        
        response = model.generate_content(
            f"{prompt}\n\nTicket: {ticket_text}",
            generation_config={"temperature": 0.1}
        )
        
        # Parse model output
        result = json.loads(response.text)
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
        "model": "gemini-1.5-flash"
    }

    # Audit logging
    if confidence < 0.5 or category == "unknown":
        log_fallback(ticket_text, final_result)

    return final_result

def log_llm_error(ticket_text, error_msg):
    """Governance: Log when AI model fails."""
    entry = {
        "error": error_msg,
        "ticket": ticket_text[:100],
        "timestamp": __import__("datetime").datetime.utcnow().isoformat()
    }
    os.makedirs("governance", exist_ok=True)
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
