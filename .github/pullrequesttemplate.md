# Pull Request Checklist - AI Triage Bot

Thank you for contributing!  
This project is governed by ISO/IEC 42001 principles and requires strict audit alignment.

Please confirm the following before submitting:

## ✅ Governance Documentation

- [ ] I updated `lifecycle/version_history.md` to reflect this change  
- [ ] I updated `docs/iso42001_mapping.md` to map this change to the relevant ISO clause(s)  
- [ ] I used truthful dates from the actual commit history (no placeholders)

## ✅ Testing and Risk Controls

- [ ] I added or updated tests in `tests/` to validate this change  
- [ ] I reviewed fallback behavior and updated `fallback_log.json` if applicable  
- [ ] I updated `risk_controls/` documentation if this change affects escalation or fallback protocols

## ✅ Commit Message

- [ ] My commit message references the governance impact (e.g., `feat: add schema validator (Clause 6)`)

---

If any of these items are not applicable, please explain why in the PR description.

This checklist helps maintain audit-readiness and ensures all changes are traceable and compliant.