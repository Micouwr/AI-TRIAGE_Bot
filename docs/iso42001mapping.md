# ISO/IEC 42001 Mapping - AI Triage Bot

This document maps AI Triage Bot features and integrated governance scripts to ISO/IEC 42001 requirements.

---

## Clauses 1-4 - Contextual

| ISO/IEC 42001 Clause | Requirement Focus         | AI Triage Bot Feature(s)                  | Evidence/Reference File(s)         |
|----------------------|---------------------------|-------------------------------------------|------------------------------------|
| Clause 1 - Scope     | Define boundaries of system | Operational scope defined in configuration | `config/scope.yaml`                |
| Clause 2 - Normative References | Reference applicable standards | ISO/IEC 42001 cited in governance docs | `docs/iso42001_mapping.md`         |
| Clause 3 - Terms & Definitions | Establish shared terminology | Glossary and inline comments in codebase | `README.md`, `docs/`               |
| Clause 4 - Context of Organization | Identify organizational context | Repo structure reflects modular governance design | `risk_controls/fallback_protocols.md`, `lifecycle/version_history.md` |

---

## Clauses 5-8 - Requirements

| ISO/IEC 42001 Clause | Requirement Focus       | AI Triage Bot Feature(s) / Integrated Script | Evidence/Reference File(s)                  |
|----------------------|-------------------------|----------------------------------------------|---------------------------------------------|
| Clause 5 - Accountability | Clear ownership, traceability | Fallback logging of low-confidence classifications, Pipeline Health Monitor | `fallback_log.json`, `tools/view_fallbacks.py`, `scripts/monitoring/pipeline_health.py` |
| Clause 6 - Risk Management | Identify and mitigate risks | PII detection filters, escalation protocols, Schema Validator, Database Performance Analyzer | `bot_engine/pii_filters.py`, `risk_controls/fallback_protocols.md`, `scripts/validation/schema_validator.py`, `scripts/performance/db_analyzer.py` |
| Clause 7 - Transparency | Explainability, visibility | Human-readable fallback viewer, scope definition, Data Lineage Tracker | `tools/view_fallbacks.py`, `config/scope.yaml`, `scripts/transparency/data_lineage.py` |
| Clause 8 - Auditability | Evidence for compliance | Assertion-based test suite, version history, Data Quality Assertion Framework | `tests/test_router.py`, `lifecycle/version_history.md`, `scripts/quality/data_assertions.py` |

---

## Extended Governance Scripts

| Script Name | Governance Alignment | ISO/IEC 42001 Clause(s) |
|-------------|----------------------|--------------------------|
| Pipeline Health Monitor | Centralized monitoring of ETL jobs, alerts on failures/delays | Clause 5, Clause 6 |
| Schema Validator & Change Detector | Detects schema drift, enforces contracts | Clause 6 |
| Data Lineage Tracker | Maps dependencies, supports impact analysis | Clause 7 |
| Database Performance Analyzer | Identifies bottlenecks, generates optimization recommendations | Clause 6, Clause 8 |
| Data Quality Assertion Framework | Automated checks for integrity, uniqueness, referential rules | Clause 8 |

---

## Real-World Data Examples (Planned)

| Example | Governance Alignment | ISO/IEC 42001 Clause(s) |
|---------|----------------------|--------------------------|
| Pipeline logs from production ETL | Demonstrates monitoring of actual job failures | Clause 5, Clause 6 |
| Schema drift in customer database | Validates detection of real schema changes | Clause 6 |
| Lineage of sales reporting tables | Provides transparency in real transformations | Clause 7 |
| Query performance metrics from PostgreSQL | Shows auditability of optimization recommendations | Clause 6, Clause 8 |
| Data quality checks on CRM records | Ensures integrity of live business data | Clause 8 |

---

## Future Extensions

| Integration | Governance Alignment | ISO/IEC 42001 Clause(s) |
|-------------|----------------------|--------------------------|
| Slack/Freshdesk APIs | Extends accountability and communication channels after core system stability is confirmed | Clause 5 |

---

### Notes
- Clauses 1-4 are acknowledged for completeness.  
- Clauses 5-8 are mapped to both core bot features and integrated scripts.  
- Real-world data examples will be introduced only after initial tests confirm working conditions, with sanitized datasets.  
- Slack/Freshdesk integration is explicitly marked as a future extension, ensuring platform stability before external communication channels are added.