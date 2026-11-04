# Vigil: Project Portfolio

**Audience:** External stakeholders, recruiters, technical reviewers
**Status:** APPROVED
**Version:** 1.0
**Date:** 2026-10-30
**Author:** William Ryan Micou

> Note: project documentation has referenced this file since v0.5, but it was missing from the repository. This version was written to close that gap.

## 1. Project Overview and Objectives

Vigil is a prototype that shows how a routine IT support workflow, ticket triage, can be partly automated with an AI classifier while keeping a human in the loop for anything risky or uncertain.

The objective was never production software. It was to design the workflow end to end: what the AI is allowed to decide, where it must hand off to a person, and how every decision gets logged for audit. The working code exists to prove the workflow is real, not just a diagram.

Objectives:

- Classify incoming Tier 1 support tickets into defined categories, with a confidence score on every result.
- Route low-risk, high-confidence tickets toward automated handling.
- Escalate anything uncertain, unclassifiable, or containing personal information to a human reviewer.
- Log every decision in a structured format so the system can be audited.
- Wrap the system in governance documentation mapped to ISO/IEC 42001:2023.

## 2. Technical Implementation Details

- Language: Python 3.
- AI model: Google Gemini 3.8 Flash (gemini-3.8-flash), called through the google-genai SDK at low temperature (0.1) for consistent output. The project previously pinned Gemini 2.5 Flash, which Google retired for new API projects in 2026; the configuration was updated so the bot runs with current keys.
- Interface: a small tkinter desktop app. Paste in a ticket, get back a category and a confidence score.
- Classification prompt: a template in `prompts/classification_prompt.txt` that instructs the model to return only JSON with `category` and `confidence`.
- Ticket types: access_request, password_reset, software_issue, hardware_issue, billing_question, compliance_flag, unknown.
- PII detection: pattern matching in `risk_controls/pii_filters.py` for Social Security numbers, credit card numbers (with a Luhn check), phone numbers, and email addresses.
- Fallback logging: tickets the system cannot classify, classifies with low confidence, or flags for PII are written to `fallback_log.jsonl` for human review. A viewer tool in `tools/fallback_viewer.py` reads the log back.
- Configuration: `governance/config/scope.yaml` holds the model name, the 0.5 confidence threshold, ticket types, escalation rules, and the fallback protocol.

My role: I directed the design, defined the workflow requirements, the escalation logic, and the governance controls, and built the prototype with AI-assisted coding. The code is real and it runs. What this project demonstrates is workflow design and AI governance, not software engineering as a profession.

## 3. System Architecture

Ticket text in, routing decision out:

1. The operator pastes ticket text into the desktop app (`main_gui.py`).
2. `risk_controls/pii_filters.py` scans the text for personal information.
3. `bot_engine/router.py` sends the text to Gemini with the classification prompt and parses the JSON response into a category and confidence score.
4. The confidence score is checked against the 0.5 threshold from `scope.yaml`. Low-confidence, unknown, or PII-flagged tickets are written to the fallback log for human review.
5. Results display in the app window.

## 4. ISO/IEC 42001:2023 Governance Implementation

The governance package was built alongside the code, clause by clause:

- `governance/ai_policy.md`: AI policy with a risk table.
- `governance/audit_procedures.md`: how the system gets audited.
- `governance/roles_and_responsibilities.md`: defined roles, including AI Governance Lead.
- `governance/competence_requirements.md`: what people operating the system need to know.
- `governance/training_materials/`: framework guide, admin/technical guide, reviewer handbook.
- `docs/operator_quick_guide.md`: end-user guide for Tier 1 operators.
- `risk_controls/escalation_protocols.md` and `risk_controls/fallback_protocols.md`: what happens when the AI is unsure or fails.
- `docs/iso42001_compliance_mapping.md`: clause-by-clause mapping that marks each item IMPLEMENTED or PLANNED, honestly, not everything as done.
- `lifecycle/versionhistory.md`: version tracking across the build.

The compliance mapping is the piece I would show first. It does not claim full compliance; it states what is implemented and what is still planned.

## 5. Documentation Created

- `README.md`: install, usage, troubleshooting, security notes, roadmap.
- `docs/PORTFOLIO.md`: this file.
- `docs/operator_quick_guide.md`: operator guide.
- `docs/iso42001_compliance_mapping.md`: compliance mapping.
- `docs/README.md`, `governance/README.md`, `tests/README.md`, `tools/README.md`, `prompts/README.md`, `risk_controls/README.md`, `lifecycle/README.md`: per-folder indexes.
- All governance and training documents listed in section 4.

## 6. Quality Assurance Approach

- Automated pytest suite: 28 test cases. 21 cover PII detection (13 positive cases across SSN, card numbers, phones, and emails; 7 negative cases; 1 multi-type case). 7 cover the router: classification, PII-triggered fallback, low-confidence fallback logging, high-confidence pass-through, and LLM failure handling.
- Router tests use mocked LLM responses, so they verify the workflow logic, not live model accuracy. Measuring real classification accuracy against labeled tickets is a planned next step (see Future Enhancements).
- CI runs the test suite on every change.

## 7. Security and Privacy Implementation

- The Gemini API key lives in `.env` and is never committed.
- PII scanning runs on every ticket; PII-flagged tickets are routed to human review instead of automated handling.
- Known limitation, stated openly: the fallback log currently stores full ticket text, including text flagged for PII. Redacting logged tickets is on the fix list (see Future Enhancements).

## 8. Skills Demonstrated

- AI workflow design: deciding what the model handles and where humans stay in the loop.
- Human-review safeguards: escalation rules, fallback protocols, audit logging.
- AI governance: ISO/IEC 42001-aligned policy, risk controls, audit procedures, defined roles.
- Requirements as configuration: `scope.yaml` as executable requirements for thresholds, categories, and routing rules.
- Technical documentation: operator guides, training materials, compliance mapping.
- Prototyping: enough working Python to prove the design runs.

## 9. Development Process

Built iteratively across November and December 2025. Early versions established classification and PII detection. Later versions added the governance layer, the pytest suite, and the compliance mapping. Every version is recorded in `lifecycle/versionhistory.md`.

## 10. Lessons Learned

- Declaring escalation rules in a config file is not the same as enforcing them. The rules in `scope.yaml` are declared; wiring every result through them as routing decisions in code is the next build step. Documentation that outruns implementation is a finding, not a feature.
- Mocked tests prove the workflow logic, not the model. Real evaluation needs labeled tickets and measured accuracy.
- Governance documentation earns trust only when it is honest about implemented versus planned. The compliance mapping marks both, and this file does the same.
- Unused code is a finding, not a roadmap. The `scripts/` folder held five generic monitoring and validation stubs that nothing called, one of them validating a data schema the bot does not return. They were deleted rather than wired up: the functions they gestured at (PII redaction, audit logging, routing decisions) already live in the codebase, and a prototype earns trust by being small and honest.

## 11. Future Enhancements

- Add a short screen-recorded demo for reviewers who will not install a desktop app.
