# Quality Scripts

Purpose: Validate LLM outputs for completeness, schema compliance, and confidence bounds to ensure the AI Triage Bot Prototype meets quality standards.

## ISO/IEC 42001 Alignment
- **Clause 6 (Risk Management)**: Prevents invalid or incomplete outputs.
- **Clause 8 (Auditability)**: Logs validation results for review and compliance checks.

## Audit Notes
- **Required Fields**: `ticket_id`, `type`, `confidence`, `actions`
- **Confidence Threshold**: ≥ 0.5
- Failures logged with details to `monitoring/pipeline_health.txt`

These scripts are essential for maintaining the quality and reliability of the AI Triage Bot's outputs.
