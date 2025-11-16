# ISO/IEC 42001 Mapping — AI Triage Bot

This document maps AI Triage Bot features to ISO/IEC 42001 governance requirements for audit readiness.

---

## Clauses 1–4 — Contextual

| ISO/IEC 42001 Clause | Requirement Focus         | AI Triage Bot Feature(s)                  | Evidence/Reference File(s)         |
|-----------------------|---------------------------|-------------------------------------------|------------------------------------|
| Clause 1 — Scope      | Define boundaries of system | Operational scope defined in configuration | `config/scope.yaml`                |
| Clause 2 — Normative References | Reference applicable standards | ISO/IEC 42001 cited in governance docs | `docs/iso42001_mapping.md`         |
| Clause 3 — Terms & Definitions | Establish shared terminology | Glossary and inline comments in codebase | `README.md`, `docs/`               |
| Clause 4 — Context of Organization | Identify organizational context | Repo structure reflects modular governance design | `risk_controls/fallback_protocols.md`, `lifecycle/version_history.md` |

---

## Clauses 5–8 — Requirements

| ISO/IEC 42001 Clause | Requirement Focus       | AI Triage Bot Feature(s)                          | Evidence/Reference File(s)                  |
|-----------------------|-------------------------|--------------------------------------------------|---------------------------------------------|
| Clause 5 — Accountability | Clear ownership, traceability | Fallback logging of low-confidence classifications | `fallback_log.json`, `tools/view_fallbacks.py` |
| Clause 6 — Risk Management | Identify and mitigate risks | PII detection filters, escalation protocols       | `bot_engine/pii_filters.py`, `risk_controls/fallback_protocols.md` |
| Clause 7 — Transparency | Explainability, visibility | Human-readable fallback viewer, scope definition | `tools/view_fallbacks.py`, `config/scope.yaml` |
| Clause 8 — Auditability | Evidence for compliance | Assertion-based test suite, version history       | `tests/test_router.py`, `lifecycle/version_history.md` |

---

### Notes
- Clauses 1–4 are contextual and acknowledged for completeness.  
- Clauses 5–8 are mapped directly to implemented features.  
- This table will expand as new modules (e.g., escalation protocols, integrations) are added.