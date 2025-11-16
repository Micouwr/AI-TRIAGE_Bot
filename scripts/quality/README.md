# Quality Scripts

Purpose: Validate LLM outputs for completeness, schema compliance, and confidence bounds.

## ISO/IEC 42001 Alignment
- Clause 6 (Risk Management): Prevents invalid or incomplete outputs
- Clause 8 (Auditability): Logs validation results for review

## Audit Notes
- Required fields: ticket_id, type, confidence, actions
- Confidence threshold: ≥ 0.5
- Failures logged with details