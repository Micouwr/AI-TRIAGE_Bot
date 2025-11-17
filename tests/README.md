# Testing Strategy - AI Triage Bot Prototype

This directory contains all the test scripts for the AI Triage Bot Prototype. The testing strategy is designed to ensure reproducibility, traceability, and auditability in line with ISO/IEC 42001 Clause 8.

## Purpose

- Validate classification logic and fallback behavior.
- Ensure consistent outputs across different environments.
- Provide evidence of system integrity for auditors.

## Test Suite Overview

The test suite is comprised of the following tests:

- `test_router.py`: Validates the classification routing and confidence scoring functionality of the AI Triage Bot.
- `test_fallback_viewer.py` (Planned): Validates the logic of the human-readable fallback viewer tool.
- `test_pipeline_health.py` (Planned): Validates monitoring alerts and failure detection within the pipeline.

Each test file focuses on specific aspects of the AI Triage Bot's functionality and is designed to align with ISO/IEC 42001 standards.

## Governance Alignment

| Test File | Purpose | ISO/IEC 42001 Clauses |
|-----------|---------|----------------------|
| `test_router.py` | Validates classification logic | Clause 8 - Auditability |
| `test_fallback_viewer.py` | Validates fallback viewer logic | Clause 8 - Auditability |
| `test_pipeline_health.py` | Validates monitoring alerts | Clause 5 - Accountability, Clause 6 - Risk Management |

---

## Audit Notes

- All tests use explicit assertions for reproducibility.
- Test results are logged and versioned alongside code changes.
- Tests are updated with each governance milestone (see `lifecycle/version_history.md`).
- Contributors must update tests when modifying classification logic, fallback handling, or governance scripts.

---

## How to Run

To run all tests, execute the following command in your terminal:

```bash
# Run all tests
python -m pytest tests/
