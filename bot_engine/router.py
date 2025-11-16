import json
import yaml
from risk_controls.pii_filters import contains_pii

def load_classification_rules():
    with open("governance/config/scope.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config.get("classification_rules", [])

def classify_ticket(ticket_text):
    rules = load_classification_rules()
    ticket_lower = ticket_text.lower()

    for rule in rules:
        if any(keyword in ticket_lower for keyword in rule["keywords"]):
            category = rule["ticket_type"]
            confidence = rule["confidence"]
            break
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

import datetime

def log_fallback(ticket_text, result):
    fallback_entry = {
        "ticket": ticket_text,
        "result": result,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

    with open("fallback_log.json", "a") as f:
        f.write(json.dumps(fallback_entry) + "\n")
