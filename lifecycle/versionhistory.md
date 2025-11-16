# Version History — AI Triage Bot

This document tracks the lifecycle of the AI Triage Bot, including major changes, governance milestones, and audit‑relevant updates.

---

## v0.1 — Initial Prototype
- Created core `router.py` for ticket classification
- Added basic regex filters for PII detection
- Established fallback logging (`fallback_log.json`)

## v0.2 — Test Suite Integration
- Implemented `tests/test_router.py` with assertion‑based validation
- Added confidence scoring to classification engine
- Improved fallback logging transparency

## v0.3 — Governance Enhancements
- Drafted `risk_controls/fallback_protocols.md`
- Scoped project boundaries in `config/scope.yaml`
- Prepared placeholders for ISO mapping and lifecycle documentation

## v0.4 — Planned
- Add `tools/view_fallbacks.py` for human‑readable fallback review
- Expand test coverage with `pytest` for CI/CD
- Document escalation protocols in `risk_controls/escalation_protocols.md`

---

### Notes
- Each version increment reflects both technical and governance progress.
- Audit reviewers can trace compliance evolution across releases.