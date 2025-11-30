# ISO/IEC 42001:2023 Mapping for AI Triage Bot Prototype

This document maps the features and controls of the AI Triage Bot to the relevant clauses of the ISO/IEC 42001:2023 standard for Artificial Intelligence Management Systems.

---

## Clause 4: Context of the Organization

- **4.2 Understanding the needs and expectations of interested parties:**
  - The system is designed to meet the needs of IT support teams by automating ticket classification, reducing manual effort, and improving response times.
  - The implementation of a GUI (`main_gui.py`) and a standalone executable makes the system accessible to non-technical users, meeting their expectation for user-friendly tools.

## Clause 6: Planning

- **6.1 Actions to address risks and opportunities:**
  - **Risk:** Inaccurate classification of support tickets.
    - **Mitigation:** The system uses a confidence score from the Gemini 1.5 Flash model. Low-confidence classifications are logged for human review (`fallback_log.jsonl`), and the confidence threshold is configurable in `governance/config/scope.yaml`.
  - **Risk:** Exposure of Personally Identifiable Information (PII).
    - **Mitigation:** A refined regex-based PII detection mechanism (`risk_controls/pii_filters.py`) is in place to flag tickets containing sensitive data. The detection logic is validated by a dedicated test suite (`tests/test_pii_filters.py`).
  - **Risk:** Unexpected system failures (e.g., API outages, malformed responses).
    - **Mitigation:** The system includes robust error handling that logs failures and defaults to a safe "unknown" classification. Test coverage has been expanded to include these failure modes (`tests/test_router.py`).

## Clause 8: Operation

- **8.2 Operational controls:**
  - **- 8.2.1 Operational planning and control:**
    - The entire classification process is defined and controlled, from prompt engineering (`prompts/classification_prompt.txt`) to response parsing and logging. All configurations are centralized in `governance/config/scope.yaml`.
  - **8.2.2 Change management:**
    - All significant changes, including the move to a configurable and more robust architecture, are tracked via version control. The updated `README.md` provides clear instructions for running and building the application.
  - **8.2.3 Outsourced processes:**
    - The use of the Gemini 1.5 Flash model is an outsourced process. The system manages the risks associated with this by validating the model's output and handling API failures gracefully.

## Clause 9: Performance Evaluation

- **9.1 Monitoring, measurement, analysis and evaluation:**
  - The system's performance can be evaluated by analyzing the fallback and error logs (`fallback_log.jsonl`, `governance/llm_error_log.jsonl`). These logs provide the data needed to assess the model's accuracy and identify areas for improvement.
  - The comprehensive test suite (`tests/`) serves as a continuous performance evaluation tool, ensuring that the system meets its requirements and that new changes do not introduce regressions.

---
