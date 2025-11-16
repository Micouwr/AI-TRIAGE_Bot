# Testing Strategy - AI Triage Bot

This project uses assertion-based testing to ensure reproducibility, traceability, and auditability in line with ISO/IEC 42001 Clause 8.

---

## ✅ Purpose

- Validate classification logic and fallback behavior
- Ensure consistent outputs across environments
- Provide evidence of system integrity for auditors

---

## 🧪 Test Suite Overview

| Test File | Purpose | Governance Alignment |
|-----------|---------|----------------------|
| `tests/test_router.py` | Validates classification routing and confidence scoring | Clause 8 - Auditability |
| (Planned) `tests/test_fallback_viewer.py` | Will validate human-readable fallback viewer logic | Clause 8 - Auditability |
| (Planned) `tests/test_pipeline_health.py` | Will validate monitoring alerts and failure detection | Clause 5 - Accountability, Clause 6 - Risk Management |

---

## 🔍 Audit Notes

- All tests use explicit assertions for reproducibility  
- Test results are logged and versioned alongside code changes  
- Tests are updated with each governance milestone (see `lifecycle/version_history.md`)  
- Contributors must update tests when modifying classification logic, fallback handling, or governance scripts

---

## 🛠 How to Run

```bash
# Run all tests
python tests/test_router.py