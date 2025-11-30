# Testing Documentation - AI Triage Bot Prototype

**Last Updated:** 2025-11-29  
**Owner:** William Ryan Micou  
**Purpose:** Testing procedures, coverage information, and quality assurance guidelines  

---

## 📋 Overview

This directory contains the test suite for the AI Triage Bot prototype, ensuring functionality, reliability, and compliance with ISO/IEC 42001:2023 requirements.

---

## 📁 Directory Structure
```
tests/
├── README.md              (This file)
├── __init__.py           (Package initialization)
├── test_router.py        (Classification engine tests)
└── test_pii_filters.py   (PII detection tests)
```

---

## 🧪 Test Files

### 1. Router Tests (`test_router.py`)

**Purpose:** Validate core classification logic and error handling  
**Coverage:** Classification engine, API integration, fallback logging  
**Test Count:** 8 tests  

**Test Scenarios:**
- ✅ Standard ticket classification (access_request, billing_question, etc.)
- ✅ PII detection integration
- ✅ Low confidence fallback logging (< 0.5 threshold)
- ✅ High confidence bypassing fallback (≥ 0.5 threshold)
- ✅ LLM API failure handling
- ✅ Malformed JSON response handling
- ✅ Unknown category classification
- ✅ Mixed PII and low confidence scenarios

**Mocking Strategy:**
- Mock `bot_engine.router.model` to avoid actual API calls
- Return controlled JSON responses for predictable testing
- No API costs during test execution
- Fast test execution (< 5 seconds for full suite)

---

### 2. PII Filter Tests (`test_pii_filters.py`)

**Purpose:** Validate PII detection accuracy and prevent false positives/negatives  
**Coverage:** SSN, credit cards, emails, phone numbers  
**Test Count:** 14+ parameterized tests  

**Positive Test Cases (Should Detect PII):**
- ✅ SSN format: 123-45-6789
- ✅ Credit cards (16 digits with Luhn validation)
- ✅ Credit cards with hyphens: 1234-5678-1234-5678
- ✅ Credit cards with spaces: 1234 5678 1234 5678
- ✅ Email addresses (various formats)
- ✅ Phone numbers (parentheses, dots, spaces, hyphens)

**Negative Test Cases (Should NOT Detect PII):**
- ✅ Generic text without PII
- ✅ Non-SSN formatted numbers
- ✅ Invalid credit card numbers (fail Luhn check)
- ✅ Currency amounts
- ✅ Empty strings
- ✅ Non-string inputs (integers, None)

**Special Features:**
- Luhn algorithm validation for credit cards (reduces false positives)
- Parameterized tests for efficiency
- Edge case coverage

---

## 🚀 Running Tests

### Quick Start
```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run specific test file
python -m pytest tests/test_router.py -v
python -m pytest tests/test_pii_filters.py -v

# Run specific test function
python -m pytest tests/test_router.py::test_classify_password_reset -v
```

---

### Advanced Options
```bash
# Run with coverage report
pip install pytest-cov
python -m pytest --cov=bot_engine --cov=risk_controls --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser

# Run tests in parallel (faster)
pip install pytest-xdist
python -m pytest -n auto

# Stop on first failure
python -m pytest -x

# Show detailed output for failures only
python -m pytest --tb=short

# Run only failed tests from last run
python -m pytest --lf
```

---

## 📊 Test Coverage

### Current Coverage (as of 2025-11-29)

| Module | Coverage | Status |
|--------|----------|--------|
| `bot_engine/router.py` | ~85% | Good |
| `risk_controls/pii_filters.py` | ~95% | Excellent |
| `main_gui.py` | Not tested | GUI - manual testing required |

**Target:** 90% coverage for core business logic

**Not Covered:**
- GUI components (tkinter - requires manual testing)
- Environment variable loading
- File I/O edge cases

---

## ✅ Pre-Deployment Checklist

Before merging to main or deploying:

- [ ] All tests passing (`python -m pytest`)
- [ ] No test warnings or deprecation notices
- [ ] Coverage ≥ 85% for core modules
- [ ] No skipped tests without documented reason
- [ ] Manual GUI testing completed
- [ ] API key configured for integration testing
- [ ] Performance acceptable (< 5 seconds per classification)

---

## 🔧 Adding New Tests

### Template for Router Tests
```python
import pytest
import json
from unittest.mock import patch
from bot_engine.router import classify_ticket

@patch('bot_engine.router.model')
def test_your_new_test(mock_model):
    """Test description here."""
    # Arrange: Set up mock response
    mock_model.generate_content.return_value.text = json.dumps({
        "category": "your_category",
        "confidence": 0.85
    })
    
    ticket_text = "Your test ticket text"
    
    # Act: Call the function
    result = classify_ticket(ticket_text)
    
    # Assert: Verify results
    assert result["ticket_type"] == "your_category"
    assert result["confidence_score"] == 0.85
    assert result["contains_pii"] is False
```

---

### Template for PII Filter Tests
```python
import pytest
from risk_controls.pii_filters import contains_pii

def test_your_pii_pattern():
    """Test that your PII pattern is detected."""
    text = "Your test text with PII"
    assert contains_pii(text) is True

def test_your_non_pii_pattern():
    """Test that false positive is avoided."""
    text = "Your test text without PII"
    assert contains_pii(text) is False
```

---

## 🐛 Troubleshooting Test Failures

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'bot_engine'"**
- **Solution:** Run tests from project root, not from tests/ directory
- **Command:** `python -m pytest` (not `pytest` alone)

**Issue: "FAILED test_router.py - Mock not working"**
- **Solution:** Verify mock path matches import structure
- **Check:** Mock `bot_engine.router.model`, not `router.model`

**Issue: "Tests pass locally but fail in CI"**
- **Solution:** Check Python version consistency
- **Solution:** Verify all dependencies in requirements.txt

**Issue: "AttributeError: Mock object has no attribute 'text'"**
- **Solution:** Ensure mock return value structure matches actual API response
- **Fix:** `mock_model.generate_content.return_value.text = "..."`

---

## 📈 Test Metrics

### Performance Benchmarks

| Test Suite | Execution Time | Target |
|------------|----------------|--------|
| test_router.py | < 2 seconds | < 3 seconds |
| test_pii_filters.py | < 1 second | < 2 seconds |
| Full suite | < 5 seconds | < 10 seconds |

**If tests are slow:**
- Check for actual API calls (should be mocked)
- Check for file I/O operations
- Consider using pytest-xdist for parallel execution

---

## 🔒 Security Testing

### API Key Security
- ✅ Tests use mocking (no real API key needed)
- ✅ `.env` file not required for test execution
- ✅ No API costs incurred during testing

### PII Detection Validation
- ✅ Regular testing of PII patterns
- ✅ False positive tracking
- ✅ False negative monitoring
- ✅ Quarterly review of detection accuracy

---

## 📋 ISO/IEC 42001 Compliance

**Clause 8.2 (Operational Controls):**
- ✅ Testing procedures documented
- ✅ Test coverage requirements defined
- ✅ Pre-deployment checklist established

**Clause 9.1 (Monitoring & Measurement):**
- ✅ Test metrics tracked
- ✅ Coverage reports generated
- ✅ Performance benchmarks defined

---

## 🔄 Test Maintenance

### When to Update Tests

**Required:**
- When adding new ticket categories
- When modifying classification logic
- When changing PII detection patterns
- When updating API integration

**Best Practices:**
- Write tests BEFORE implementing features (TDD)
- Update tests when fixing bugs
- Remove obsolete tests when features deprecated
- Keep test data realistic but anonymized

### Review Schedule
- **Monthly:** Review failed tests in CI/CD
- **Quarterly:** Review test coverage gaps
- **Annual:** Full test suite audit

---

## 📞 Contact

**Questions about testing?**
- **System Owner:** William Ryan Micou
- **See also:** `../governance/training_materials/admin_technical_guide.md` (Testing section)

**For test failures or issues:**
- Check this documentation first
- Review error messages carefully
- Create an issue in GitHub repository if needed

---

## 🔗 Related Documentation

- **Main README:** `../README.md` - Project overview
- **Admin Guide:** `../governance/training_materials/admin_technical_guide.md` - Testing procedures
- **Governance:** `../governance/README.md` - Compliance documentation

---

**Document Version:** 1.0 | Created: 2025-11-29
```
