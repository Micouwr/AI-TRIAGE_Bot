# Governance Script Suite

This directory contains governance-grade scripts designed to enforce ISO/IEC 42001 controls across monitoring, performance, quality, transparency, and validation. Each subfolder houses a modular Python script aligned with specific clauses, ensuring accountability, risk management, and auditability.

## Structure

- `monitoring/` – Pipeline health and fallback monitoring  
- `performance/` – Latency and throughput tracking  
- `quality/` – Output validation and schema enforcement  
- `transparency/` – Decision rationale and trace logging  
- `validation/` – Input sanitization and risk detection

## Clause Mapping

| Folder        | Purpose                                      | ISO/IEC 42001 Clauses |
|---------------|----------------------------------------------|------------------------|
| monitoring    | Track pipeline stages, log failures, retry logic | Clause 5, Clause 6, Clause 8 |
| performance   | Measure latency, flag slow components        | Clause 6, Clause 8 |
| quality       | Validate outputs for completeness/confidence | Clause 6, Clause 8 |
| transparency  | Capture decision rationale and controls      | Clause 5, Clause 8 |
| validation    | Sanitize inputs, redact PII                  | Clause 6, Clause 8 |

## Audit Notes

- All scripts log to JSONL or text files for traceability  
- Logs must be retained for ≥ 90 days  
- Weekly governance review required for monitoring and transparency outputs  
- Thresholds (latency, confidence, sanitization) are documented in each folder’s README

## Usage

Each script can be imported into the AI Triage Bot or run standalone for testing. Example usage is included at the bottom of each file. Logs are written to `monitoring/pipeline_health.txt` or `governance/decision_trace.jsonl` depending on the control.

---

This suite ensures that every operational control is modular, auditable, and clause-aligned, supporting enterprise deployment and ISO/IEC 42001 compliance.