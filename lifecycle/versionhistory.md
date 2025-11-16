# Version History - AI Triage Bot

This document tracks the lifecycle of the AI Triage Bot, including major changes, governance milestones, and audit-relevant updates.

---

| Version | Date    | Key Changes / Features Added | Governance / Audit Notes |
|---------|---------|------------------------------|--------------------------|
| v0.1    | Nov 2025 | Initial prototype with core `router.py` classification | Established fallback logging (`fallback_log.json`) |
| v0.2    | Nov 2025 | Added assertion-based test suite (`tests/test_router.py`) | Introduced confidence scoring for transparency |
| v0.3    | Nov 2025 | Drafted `risk_controls/fallback_protocols.md` and `config/scope.yaml` | Scoped project boundaries, documented fallback protocols |
| v0.4    | Nov 2025 | Replaced manual tests with pytest, enhanced PII detection, refactored logging, and created `tools` directory | Improved auditability with automated testing and stronger PII controls |
| v0.5    | Planned | Incorporate Pipeline Health Monitor script | Extend accountability and risk monitoring features |
| v0.6    | Planned | Incorporate Schema Validator script | Strengthen risk management and schema drift detection |
| v0.7    | Planned | Incorporate Data Lineage Tracker script | Enhance transparency with lineage and impact analysis |
| v0.8    | Planned | Incorporate Database Performance Analyzer script | Improve risk and auditability with performance diagnostics |
| v0.9    | Planned | Incorporate Data Quality Assertion Framework script | Establish audit-ready quality gates and automated integrity checks |
| v1.0    | Planned | Introduce real-world data examples (sanitized) | Validate working conditions post-initial tests, strengthen transparency and auditability |
| v1.1    | Planned | Integrate with Slack/Freshdesk APIs | Extend communication channels after core system stability is confirmed |

---

### Notes
- Dates for v0.1 through v0.3 are recorded as Nov 2025, reflecting their completion in that month.  
- Populate future Date entries with actual commit timestamps once each milestone is completed.  
- Keep Planned items undated until the work is committed.  
- Real-world data examples will only be introduced after initial tests confirm working conditions, and all examples will be sanitized to protect sensitive information.  
- This table is an evidence trail, not a forecast. Only completed entries should have dates.