# Version History - AI Triage Bot

| Version | Date       | Key Changes / Features Added                          | Governance / Audit Notes                          |
|---------|------------|-------------------------------------------------------|--------------------------------------------------|
| v0.1    |            | Initial prototype with core `router.py` classification | Established fallback logging (`fallback_log.json`) |
| v0.2    |            | Added assertion-based test suite (`tests/test_router.py`) | Introduced confidence scoring for transparency    |
| v0.3    |            | Drafted `risk_controls/fallback_protocols.md` and `config/scope.yaml` | Scoped project boundaries, documented fallback protocols |
| v0.4    |            | Add `tools/view_fallbacks.py` for human-readable logs | Expand test coverage, prepare escalation protocols |
| v0.5    |            | Integrate with Slack/Freshdesk APIs                   | Document ISO/IEC 42001 clause mapping in `docs/iso42001_mapping.md` |