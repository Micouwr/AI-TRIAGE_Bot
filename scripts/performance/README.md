# Performance Scripts

Purpose: Measure latency and throughput of classification and escalation components.

## ISO/IEC 42001 Alignment
- Clause 6 (Risk Management): Identifies performance bottlenecks
- Clause 8 (Auditability): Records latency metrics with thresholds

## Audit Notes
- Warning threshold: 500 ms
- Error threshold: 2000 ms
- Logged to `monitoring/pipeline_health.txt`