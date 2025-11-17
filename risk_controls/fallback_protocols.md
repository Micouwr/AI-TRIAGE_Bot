# Fallback Protocols - AI Triage Bot

This document outlines governance-aligned fallback handling procedures for low-confidence classifications, escalation failures, and malformed LLM outputs, supporting ISO/IEC 42001 Clauses 5, 6, and 8.

## Trigger Conditions

Fallback protocols activate when:
- `confidence_score &lt; 0.5`
- Escalation fails or times out
- `ticket_type == "unknown"`
- LLM output is malformed or missing required fields

These conditions are monitored by the classification engine and governance scripts.

## Actions

1. Route ticket to human agent with fallback flag
2. Log incident in `fallback_log.jsonl` with timestamp and input
3. Notify governance team if fallback rate exceeds 5% in a 24-hour window

## Audit Notes

- All fallback events must be timestamped and retained for **90 days**
- Fallback triggers are reviewed **weekly** by the AI oversight team
- Escalation protocols are documented separately in `risk_controls/escalation_protocols.md`
- Fallback viewer (`tools/view_fallbacks.py`) will support human-readable review

## Governance Alignment

| Clause | Alignment |
|--------|-----------|
| Clause 5 - Accountability | Ensures traceability of fallback events and human handoff |
| Clause 6 - Risk Management | Detects and responds to classification and escalation failures |
| Clause 8 - Auditability | Logs all fallback events with timestamps and retention policy |
