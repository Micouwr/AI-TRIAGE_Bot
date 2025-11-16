# ISO/IEC 42001 Mapping — AI Triage Bot

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
| Clause 5 - Accountability | Clear ownership, traceability | Fallback logging of low-confidence classifications | `fallback_log.json`, `tools/view_fallbacks.py` |
| Clause 6 - Risk Management | Identify and mitigate risks | PII detection filters, escalation protocols, Schema Validator & Change Detector | `bot_engine/pii_filters.py`, `risk_controls/fallback_protocols.md`, `scripts/validation/schema_validator.py` |
| Clause 7 - Transparency | Explainability, visibility | Human-readable fallback viewer, scope definition, Data Lineage Tracker | `tools/view_fallbacks.py`, `config/scope.yaml`, `scripts/transparency/data_lineage.py` |
| Clause 8 - Auditability | Evidence for compliance | Assertion-based test suite, version history, Data Quality Assertion Framework | `tests/test_router.py`, `lifecycle/version_history.md`, `scripts/quality/data_assertions.py` |

---

## Extended Governance Scripts

| Script Name | Governance Alignment | ISO/IEC 42001 Clause(s) |
|-------------|----------------------|--------------------------|
| Pipeline Health Monitor | Centralized monitoring of ETL jobs, alerts on failures/delays | Clause 5 (Accountability), Clause 6 (Risk Management) |
| Schema Validator & Change Detector | Detects schema drift, enforces contracts | Clause 6 (Risk Management) |
| Data Lineage Tracker | Maps dependencies, supports impact analysis | Clause 7 (Transparency) |
| Database Performance Analyzer | Identifies bottlenecks, generates optimization recommendations | Clause 6 (Risk Management), Clause 8 (Auditability) |
| Data Quality Assertion Framework | Automated checks for integrity, uniqueness, referential rules | Clause 8 (Auditability) |

---

### Notes
- Clauses 1-4 are acknowledged for completeness.  
- Clauses 5-8 are mapped to both core bot features and integrated scripts.  
- Extended governance scripts strengthen compliance alignment and provide measurable audit evidence.  
- This table will expand as new modules (e.g., escalation protocols, integrations) are added.