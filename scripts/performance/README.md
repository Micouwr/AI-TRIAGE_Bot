# Performance Scripts

Purpose: Measure latency and throughput of classification and escalation components to ensure they meet performance governance standards.

## ISO/IEC 42001 Alignment
- **Clause 6 (Risk Management)**: Identifies performance bottlenecks that could impact system reliability.
- **Clause 8 (Auditability)**: Records latency metrics with predefined thresholds for audit purposes.

## Audit Notes
- **Warning Threshold**: 500 ms
- **Error Threshold**: 2000 ms
- Logged to `monitoring/pipeline_health.txt`

These scripts are crucial for maintaining the operational integrity of the AI Triage Bot Prototype by identifying and addressing performance issues promptly.
