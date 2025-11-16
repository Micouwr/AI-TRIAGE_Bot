import json
from risk_controls.pii_filters import contains_pii

def classify_ticket(ticket_text):
    if "password" in ticket_text.lower():
        category = "access_request"
        confidence = 0.92
    elif "invoice" in ticket_text.lower():
        category = "billing_question"
        confidence = 0.88
    else:
        category = "unknown"
        confidence = 0.42

    pii_flag = contains_pii(ticket_text)

    result = {
        "ticket_type": category,
        "confidence_score": round(confidence, 2),
        "contains_pii": pii_flag
    }

    if confidence < 0.5 or category == "unknown":
        log_fallback(ticket_text, result)

    return result

def log_fallback(ticket_text, result):
    fallback_entry = {
        "ticket": ticket_text,
        "result": result,
        "timestamp": __import__("datetime").datetime.utcnow().isoformat()
    }

    with open("fallback_log.json", "a") as f:
        f.write(json.dumps(fallback_entry) + "\n")
