# Contributing to the Governance Script Suite

This repository enforces ISO/IEC 42001 governance standards. All contributions must align with clause-mapped controls, audit-trail integrity, and modular architecture.

## Contribution Guidelines

### ✅ Required for All New Scripts

- **Folder Placement**: Place your script in one of the following:
  - `monitoring/` – Pipeline health and fallback tracking
  - `performance/` – Latency and throughput measurement
  - `quality/` – Output validation and schema enforcement
  - `transparency/` – Decision rationale and trace logging
  - `validation/` – Input sanitization and risk detection

- **Clause Mapping**: Your script must align with at least one of the following ISO/IEC 42001 clauses:
  - Clause 5 – Accountability
  - Clause 6 – Risk Management
  - Clause 8 – Auditability

- **Logging Discipline**:
  - Use structured logging (JSON or JSONL)
  - Include timestamps and component labels
  - Log to `monitoring/pipeline_health.txt` or `governance/decision_trace.jsonl` as appropriate

- **README Update**:
  - Update the folder’s `README.md` to reflect your script’s purpose and clause alignment
  - Include audit notes (e.g., thresholds, retention, review frequency)

- **No Placeholders**:
  - Do not submit placeholder scripts or stub files
  - All commits must reflect functional, testable code

### ✅ Required for Modifications

- Clearly document changes in the script’s header comment
- Update the folder’s `README.md` if clause alignment or audit behavior changes
- Use descriptive, audit-friendly commit messages (e.g., `Refactor: tighten latency threshold in latency_tracker.py`)

## Review Process

All contributions are reviewed for:
- Clause alignment
- Logging integrity
- Modular structure
- Audit-trail completeness

Scripts that do not meet these standards will be rejected or flagged for revision.

---

By contributing, you agree to uphold the governance and audit standards required for ISO/IEC 42001 compliance.