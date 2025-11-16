# Version History - AI Triage Bot

This document tracks the lifecycle of the AI Triage Bot, including major changes, governance milestones, and audit-relevant updates.

---

| Version | Date    | Key Changes / Features Added                          | Governance / Audit Notes                          |
|---------|---------|-------------------------------------------------------|--------------------------------------------------|
| v0.1    | Oct 2025 | Initial prototype with core `router.py` classification | Established fallback logging (`fallback_log.json`) |
| v0.2    | Oct 2025 | Added assertion-based test suite (`tests/test_router.py`) | Introduced confidence scoring for transparency    |
| v0.3    | Oct 2025 | Drafted `risk_controls/fallback_protocols.md` and `config/scope.yaml` | Scoped project boundaries, documented fallback protocols |
| v0.4    | Nov 2025 | Add `tools/view_fallbacks.py` for human-readable logs | Expand test coverage, prepare escalation protocols |
| v0.5    | Nov 2025 | Integrate with Slack/Freshdesk APIs                   | Document ISO/IEC 42001 clause mapping in `docs/iso42001_mapping.md` |
| v0.6    | Nov 2025 | Incorporate Pipeline Health Monitor script            | Extend accountability and risk monitoring features |
| v0.7    | Dec 2025 | Incorporate Schema Validator script                   | Strengthen risk management and schema drift detection |
| v0.8    | Dec 2025 | Incorporate Data Lineage Tracker script               | Enhance transparency with lineage and impact analysis |
| v0.9    | Dec 2025 | Incorporate Database Performance Analyzer script      | Improve risk and auditability with performance diagnostics |
| v1.0    | Jan 2026 | Incorporate Data Quality Assertion Framework script   | Establish audit-ready quality gates and automated integrity checks |

---

### Notes
- Dates are expressed as month/year for clarity and simplicity.  
- Each version increment reflects both technical and governance progress.  
- This table ensures auditors can trace compliance evolution across releases.