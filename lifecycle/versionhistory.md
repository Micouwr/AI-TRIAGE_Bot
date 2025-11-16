# Version History — AI Triage Bot

This document tracks the lifecycle of the AI Triage Bot, including major changes, governance milestones, and audit‑relevant updates.

---

| Version | Date       | Key Changes / Features Added                          | Governance / Audit Notes                          |
|---------|------------|-------------------------------------------------------|--------------------------------------------------|
| v0.1    | 2025-10-01 | Initial prototype with core `router.py` classification | Established fallback logging (`fallback_log.json`) |
| v0.2    | 2025-10-15 | Added assertion‑based test suite (`tests/test_router.py`) | Introduced confidence scoring for transparency    |
| v0.3    | 2025-10-30 | Drafted `risk_controls/fallback_protocols.md` and `config/scope.yaml` | Scoped project boundaries, documented fallback protocols |
| v0.4    | Planned    | Add `tools/view_fallbacks.py` for human‑readable logs | Expand test coverage, prepare escalation protocols |
| v0.5    | Planned    | Integrate with Slack/Freshdesk APIs                   | Document ISO/IEC 42001 clause mapping in `docs/iso42001_mapping.md` |

---

### Notes
- Each version increment reflects both technical and governance progress.  
- Dates are placeholders — update them with actual commit or release dates.  
- This table ensures auditors can trace compliance evolution across releases.