# Version History - AI Triage Bot

This document tracks the lifecycle of the AI Triage Bot, including major changes, governance milestones, and audit-relevant updates.

---

| Version | Date | Key Changes / Features Added | Governance / Audit Notes |
|---------|------|------------------------------|--------------------------|
| v0.1 | 2025-11-17 | Initial prototype with core `router.py` classification | Established fallback logging (`fallback_log.json`) |
| v0.2 | 2025-11-17 | Added assertion-based test suite (`tests/test_router.py`) | Introduced confidence scoring for transparency |
| v0.3 | 2025-11-17 | Drafted `risk_controls/fallback_protocols.md` and `governance/config/scope.yaml` | Scoped project boundaries, documented fallback protocols |
| v0.4 | 2025-11-25 | Replaced manual tests with pytest, enhanced PII detection with Luhn algorithm, refactored logging to JSONL format, created `tools/` directory with `fallback_viewer.py` | Improved auditability with automated testing and stronger PII controls. Supports ISO/IEC 42001:2023 Clause 9.1 (Monitoring) |
| v0.5 | 2025-11-29 | Created 9 ISO/IEC 42001:2023 governance documents: ai_policy.md, audit_procedures.md, competence_requirements.md, roles_and_responsibilities.md, 3 training guides, operator_quick_guide.md, PORTFOLIO.md | Established comprehensive governance framework. Supports ISO/IEC 42001:2023 Clauses 5 (Leadership), 6 (Risk), 7 (Support), 8 (Operations), 9 (Performance), 10 (Improvement) |
| v0.6 | 2025-11-29 | Updated model references from Gemini 1.5 Flash to Gemini 2.5 Flash across all documentation and code | Reflects current system configuration. Updated `governance/config/scope.yaml` |
| v0.7 | 2025-11-29 | Created 4 folder README files: `governance/README.md`, `docs/README.md`, `tests/README.md`, `tools/README.md` | Enhanced documentation navigation. Supports ISO/IEC 42001:2023 Clause 7.5 (Documented Information) |
| v0.8 | 2025-12-02 | Consolidated ISO compliance mapping: created comprehensive `docs/iso42001_compliance_mapping.md`, deleted duplicate files (`iso42001_mapping.md`, `iso42001mapping.md`) | Single source of truth for ISO/IEC 42001:2023 compliance. Documents 95% compliance, 8 risks with mitigations, 22 supporting files. Resolves Clause 7.5 violation |
| v0.9 | 2025-12-07 | **SDK Migration:** Migrated from deprecated `google-generativeai` to modern `google-genai` SDK. Updated `requirements.txt`, `bot_engine/router.py`, `tests/test_router.py`. Fixed `tests/__init__.py` syntax error. All 24 tests passing (100%) | Ensures long-term SDK support (old SDK sunsets 2025-08-31). Supports ISO/IEC 42001:2023 Clause 8.3 (Change Management) |
| v1.0 | 2025-12-07 | **PII Detection Enhancement:** Fixed formatted credit card detection (hyphens/spaces), maintained Luhn validation, updated test data with valid industry-standard test credit card numbers. All 17 PII tests passing | Enhanced data protection. Supports ISO/IEC 42001:2023 Clause 6.1 (Risk Management - PII protection) |
| v1.1 | 2025-12-07 | **Repository Audit:** Standardized all ISO/IEC 42001:2023 references (9 files), removed em dashes, fixed model references (1.5→2.5 Flash), corrected tool filename references, updated documentation status (ISO mapping now APPROVED) | Ensures documentation accuracy and consistency. Supports ISO/IEC 42001:2023 Clause 7.5 (Documented Information) |
| v1.2 | Planned | Introduce real-world data examples (sanitized) | Validate working conditions with production-like data, strengthen transparency and auditability |
| v1.3 | Planned | Advanced monitoring dashboard (GUI-based fallback viewer) | Enhanced user experience for Human Review Agents. Supports ISO/IEC 42001:2023 Clause 9.1 (Monitoring) |
| v1.4 | Planned | Multi-model support architecture (Gemini + OpenAI) | Vendor risk mitigation. Supports ISO/IEC 42001:2023 Clauses 6.1 (Risk Management) and 8.4 (Outsourced Processes) |
| v1.5 | Planned | Integrate with Slack/Freshdesk APIs | Extend communication channels after core system stability confirmed |

---

## Session Summary

### Session 1 (2025-11-17 to 2025-11-29)
- Established core system functionality
- Created comprehensive ISO/IEC 42001:2023 governance framework
- Enhanced PII detection with Luhn algorithm
- Updated to Gemini 2.5 Flash

### Session 2 (2025-11-29 to 2025-12-07)
- **Documentation:** Created 4 folder READMEs, consolidated ISO compliance mapping
- **SDK Migration:** Fully migrated to modern google-genai SDK (all tests passing)
- **PII Enhancement:** Fixed formatted credit card detection, all 17 PII tests passing
- **Repository Audit:** Standardized all ISO/IEC 42001:2023 references across 9 files
- **Quality Assurance:** 24/24 tests passing (100%), enhanced Luhn validation
- **Compliance Status:** 95% ISO/IEC 42001:2023 compliant

---

## Notes

- Version numbers now reflect actual milestones achieved, not planned features
- All dates reflect actual completion dates from git commit history
- ISO/IEC 42001:2023 compliance is tracked and maintained across all changes
- Testing coverage is comprehensive: 24 tests (17 PII + 7 router) all passing
- SDK is modern and supported (google-genai replaces deprecated google-generativeai)
- This document serves as an evidence trail for audits and compliance reviews
- Real-world data examples will only be introduced after validation, with proper sanitization
- All governance documentation follows ISO/IEC 42001:2023 standard naming convention

---

**Document Version:** 2.0 | Last Updated: 2025-12-07
