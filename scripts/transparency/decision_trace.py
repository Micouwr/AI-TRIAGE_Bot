"""
decision_trace.py

Captures decision rationale, inputs, and confidence for traceability.
Aligns with ISO/IEC 42001: Clause 5 (Accountability), Clause 8 (Auditability).
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional

TRACE_FILE = Path("governance/decision_trace.jsonl")

def _append_trace(record: Dict[str, Any]):
    TRACE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with TRACE_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

def trace_decision(
    ticket_id: str,
    input_summary: str,
    classification: str,
    confidence: float,
    rationale: Optional[str],
    controls_applied: Optional[list] = None,
    extra: Optional[Dict[str, Any]] = None
) -> None:
    """
    Appends a structured decision trace for audit review.
    - ticket_id: unique identifier for correlation
    - input_summary: sanitized description of input (no raw PII)
    - classification: e.g., 'routing', 'escalation', 'fallback'
    - confidence: 0.0-1.0
    - rationale: brief reason or key signals
    - controls_applied: list of governance controls enforced
    - extra: optional dict for additional context
    """
    record = {
        "timestamp": _ts(),
        "ticket_id": ticket_id,
        "input_summary": input_summary,
        "classification": classification,
        "confidence": confidence,
        "rationale": rationale,
        "controls_applied": controls_applied or [],
        "extra": extra or {}
    }
    _append_trace(record)

def _ts():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S")

# Example usage
if __name__ == "__main__":
    trace_decision(
        ticket_id="abc-123",
        input_summary="User asked for account help; email redacted.",
        classification="routing",
        confidence=0.83,
        rationale="High intent match; no risk flags.",
        controls_applied=["ip_filters", "output_validator"]
    )