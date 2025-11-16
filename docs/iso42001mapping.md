# ISO/IEC 42001 Mapping - AI Triage Bot

This document maps AI Triage Bot features and integrated governance scripts to ISO/IEC 42001 requirements.  
It also records milestone completion dates to maintain audit clarity and synchronization with `lifecycle/version_history.md`.

---

## Clauses 1-4 - Contextual

| ISO/IEC 42001 Clause | Requirement Focus         | AI Triage Bot Feature(s)                  | Evidence/Reference File(s)         | Status / Date |
|----------------------|---------------------------|-------------------------------------------|------------------------------------|---------------|
| Clause 1 - Scope     | Define boundaries of system | Operational scope defined in configuration | `config/scope.yaml`                | Completed (Nov 2025) |
| Clause 2 - Normative References | Reference applicable standards | ISO/IEC 42001 cited in governance docs | `docs/iso42001_mapping.md`         | Completed (Nov 2025) |
| Clause 3 - Terms & Definitions | Establish shared terminology | Glossary and inline comments in codebase | `README.md`, `docs/`               | Completed (Nov 2025) |
| Clause 4 - Context of Organization | Identify organizational context | Repo structure reflects modular governance design | `risk_controls/fallback_protocols.md`, `lifecycle/version_history.md` | Completed (Nov 2025) |

---

## Clauses 5-8 - Requirements

| ISO/IEC 42001 Clause | Requirement Focus       | AI Triage Bot Feature(s) / Integrated Script | Evidence/Reference File(s)                  | Status / Date |
|----------------------|-------------------------|----------------------------------------------|---------------------------------------------|---------------|
| Clause 5 - Accountability | Clear ownership, traceability | Fallback logging of low-confidence classifications, Pipeline Health Monitor | `fallback_log.json`, `tools/view_fallbacks.py`, `scripts/monitoring/pipeline_health.py` | Planned |
| Clause 6 - Risk Management | Identify and mitigate risks | PII detection filters, escalation protocols, Schema Validator, Database Performance Analyzer | `bot_engine/pii_filters.py`, `risk_controls/fallback_protocols.md`, `scripts/validation/schema_validator.py`, `scripts/performance/db_analyzer.py` | Planned |
| Clause 7 - Transparency | Explainability, visibility | Human-readable fallback viewer, scope definition, Data Lineage Tracker | `tools/view_fallbacks.py`, `config/scope.yaml`, `scripts/transparency/data_lineage.py` | Planned |
| Clause 8 - Auditability | Evidence for compliance | Assertion-based test suite, version history, Data Quality Assertion Framework | `tests/test_router.py`, `lifecycle/version_history.md`, `scripts/quality/data_assertions.py` | Planned |

---

## Extended Governance Scripts

| Script Name | Governance Alignment | ISO/IEC 42001 Clause(s) | Status / Date |
|-------------|----------------------|--------------------------|---------------|
| Pipeline Health Monitor | Centralized monitoring of ETL jobs, alerts on failures/delays | Clause 5, Clause 6 | Planned |
| Schema Validator & Change Detector | Detects schema drift, enforces contracts | Clause 6 | Planned |
| Data Lineage Tracker | Maps dependencies, supports impact analysis | Clause 7 | Planned |
| Database Performance Analyzer | Identifies bottlenecks, generates optimization recommendations | Clause 6, Clause 8 | Planned |
| Data Quality Assertion Framework | Automated checks for integrity, uniqueness, referential rules | Clause 8 | Planned |

---

## Real-World Data Examples (Planned)

| Example | Governance Alignment | ISO/IEC 42001 Clause(s) | Status / Date |
|---------|----------------------|--------------------------|---------------|
| Pipeline logs from production ETL | Demonstrates monitoring of actual job failures | Clause 5, Clause 6 | Planned |
| Schema drift in customer database | Validates detection of real schema changes | Clause 6 | Planned |
| Lineage of sales reporting tables | Provides transparency in real transformations | Clause 7 | Planned |
| Query performance metrics from PostgreSQL | Shows auditability of optimization recommendations | Clause 6, Clause 8 | Planned |
| Data quality checks on CRM records | Ensures integrity of live business data | Clause 8 | Planned |

---

## Future Extensions

| Integration | Governance Alignment | ISO/IEC 42001 Clause(s) | Status / Date |
|-------------|----------------------|--------------------------|---------------|
| Slack/Freshdesk APIs | Extends accountability and communication channels after core system stability is confirmed | Clause 5 | Future |

---

### Notes
- Clauses 1–4 are marked **Completed (Nov 2025)** to reflect the first three milestones achieved.  
- Clauses 5–8 and governance scripts are **Planned**, pending implementation.  
- Real-world data examples are **Planned** and will be introduced only after initial tests confirm working conditions, using sanitized datasets.  
- Slack/Freshdesk integration is explicitly marked