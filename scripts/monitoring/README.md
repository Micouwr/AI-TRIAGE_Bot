# Monitoring Scripts

Purpose: Track pipeline health, fallback triggers, and stage execution within the AI Triage Bot system.

## ISO/IEC 42001 Alignment
- Clause 5 (Accountability): Ensures traceability of monitored stages.
- Clause 6 (Risk Management): Detects failures and retries.
- Clause 8 (Auditability): Logs all monitoring events with timestamps.

## Audit Notes
- Logs written to `monitoring/pipeline_health.txt`
- Retention: 90 days minimum
- Weekly review required by oversight team
