"""
output_validator.py

Validates LLM outputs for required fields, types, and confidence bounds.
Aligns with ISO/IEC 42001: Clause 6 (Risk Management), Clause 8 (Auditability).
"""

import json
import time
from pathlib import Path
from typing import Dict, Any

LOG_FILE = Path("monitoring/pipeline_health.txt")

REQUIRED_FIELDS = {
    "ticket_id": str,
    "type": str,
    "confidence": float,
    "actions": list
}

def _log(event):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")

def validate_output(payload: Dict[str, Any], min_confidence: float = 0.5) -> bool:
    """
    Validates:
    - Presence and type of REQUIRED_FIELDS
    - Confidence within [0.0, 1.0] and >= min_confidence
    Returns True if valid, False otherwise. Logs findings.
    """
    findings = []
    valid = True

    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in payload:
            findings.append(f"missing:{field}")
            valid = False
            continue
        if not isinstance(payload[field], expected_type):
            findings.append(f"type_error:{field}")
            valid = False

    conf = payload.get("confidence")
    if isinstance(conf, float):
        if conf < 0.0 or conf > 1.0:
            findings.append("confidence_out_of_bounds")
            valid = False
        elif conf < min_confidence:
            findings.append("confidence_below_threshold")
            valid = False

    event = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "component": "output_validator",
        "metric": "validation",
        "status": "pass" if valid else "fail",
        "details": findings or ["ok"]
    }
    _log(event)
    return valid

def time_str():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S")

# Example usage
if __name__ == "__main__":
    sample = {
        "ticket_id": "abc-123",
        "type": "routing",
        "confidence": 0.76,
        "actions": ["notify", "log"]
    }
    assert validate_output(sample, min_confidence=0.6) is True
