"""
decision_trace.py

Purpose: Capture decision rationale, confidence, and governance controls applied.
Aligns with ISO/IEC 42001: Clause 5 (Accountability), Clause 8 (Auditability).

## Audit Notes
- Logs written to `governance/decision_trace.jsonl`.
- Input summaries must be sanitized (no raw PII).
- Reviewed weekly by governance team.
"""

import json
import time
from pathlib import Path

LOG_FILE = Path("governance/decision_trace.jsonl")

def _log(event):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")

def log_decision_rationale(decision_id, rationale, confidence, actions, sanitized_input):
    """
    Logs the decision rationale, confidence, and actions taken by the bot.
    """
    event = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "decision_id": decision_id,
        "rationale": rationale,
        "confidence": confidence,
        "actions": actions,
        "input_summary": sanitized_input
    }
    _log(event)

# Example usage
if __name__ == "__main__":
    log_decision_rationale(
        decision_id="123456",
        rationale="Ticket classified as 'access_request'",
        confidence=0.95,
        actions=["route_to_agent", "log_event"],
        sanitized_input="User requested access to system."
    )
