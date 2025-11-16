# Version History - AI Triage Bot

This document tracks the lifecycle of the AI Triage Bot, including major changes, governance milestones, and audit-relevant updates.

---

| Version | Date | Key Changes / Features Added | Governance / Audit Notes |
|---------|------|------------------------------|--------------------------|
| v0.1    |      | Initial prototype with core `router.py` classification | Established fallback logging (`fallback_log.json`) |
| v0.2    |      | Added assertion-based test suite (`tests/test_router.py`) | Introduced confidence scoring for transparency |
| v0.3    |      | Drafted `risk_controls/fallback_protocols.md` and `config/scope.yaml` | Scoped project boundaries, documented fallback protocols |
| v0.4    | Planned | Add `tools/view_fallbacks.py` for human-readable logs | Expand test coverage, prepare escalation protocols |
| v0.5    | Planned | Integrate with Slack/Freshdesk APIs | Document ISO/IEC 42001 clause mapping in `docs/iso42001_mapping.md` |
| v0.6    | Planned | Incorporate Pipeline Health Monitor script | Extend accountability and risk monitoring features |
| v0.7    | Planned | Incorporate Schema Validator script | Strengthen risk management and schema drift detection |
| v0.8    | Planned | Incorporate Data Lineage Tracker script | Enhance transparency with lineage and impact analysis |
| v0.9    | Planned | Incorporate Database Performance Analyzer script | Improve risk and auditability with performance diagnostics |
| v1.0    | Planned | Incorporate Data Quality Assertion Framework script | Establish audit-ready quality gates and automated integrity checks |

---

### Notes
- Populate the Date column using the actual commit timestamps for each completed version.
- Keep Planned items undated until the work is completed and committed.
- This table is an evidence trail, not a forecast. Only completed entries should have dates.