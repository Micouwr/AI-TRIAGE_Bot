"""
input_sanitizer.py

Validates and sanitizes raw inputs to reduce risk and enforce structure.
Aligns with ISO/IEC 42001: Clause 6 (Risk Management), Clause 8 (Auditability).
"""

import re
import json
from pathlib import Path
from typing import Dict, Any

SANITIZED_LOG = Path("monitoring/pipeline_health.txt")

PHONE_REGEX = re.compile(r"\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b")
EMAIL_REGEX = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

def _log(event):
    SANITIZED_LOG.parent.mkdir(parents=True, exist_ok=True)
    with SANITIZED_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")

def sanitize_input(text: str) -> Dict[str, Any]:
    """
    Returns a dict with:
    - sanitized_text: PII redacted
    - flags: list of detected risk markers
    - meta: counts of redactions by type
    """
    flags = []
    redactions = {"phone": 0, "email": 0}

    def _redact_phone(m):
        redactions["phone"] += 1
        flags.append("phone_detected")
        return "[PHONE_REDACTED]"

    def _redact_email(m):
        redactions["email"] += 1
        flags.append("email_detected")
        return "[EMAIL_REDACTED]"

    sanitized = PHONE_REGEX.sub(_redact_phone, text)
    sanitized = EMAIL_REGEX.sub(_redact_email, sanitized)

    event = {
        "timestamp": _ts(),
        "component": "input_sanitizer",
        "metric": "sanitization",
        "status": "ok",
        "details": {"flags": list(set(flags)), "redactions": redactions}
    }
    _log(event)

    return {
        "sanitized_text": sanitized,
        "flags": list(set(flags)),
        "meta": redactions
    }

def _ts():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S")

# Example usage
if __name__ == "__main__":
    sample = "Call me at (502) 555-1234 or email ryan@example.com."
    result = sanitize_input(sample)
    assert "[PHONE_REDACTED]" in result["sanitized_text"]
    assert "[EMAIL_REDACTED]" in result["sanitized_text"]