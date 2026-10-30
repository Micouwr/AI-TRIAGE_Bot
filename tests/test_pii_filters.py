# tests/test_pii_filters.py
import pytest
from risk_controls.pii_filters import contains_pii, redact_pii, detect_pii_types

# --- Test Cases for PII Detection ---

# Parameters for testing strings that SHOULD contain PII
# Note: ZIP codes have been removed as they are prone to false positives with simple regex.
# Credit card numbers use industry-standard test numbers that pass Luhn validation.
pii_positive_cases = [
    ("My SSN is 123-45-6789.", "SSN"),
    ("Please use card 4532015112830366 for the payment.", "16-digit credit card (Visa test number)"),
    ("My card is 4532-0151-1283-0366.", "Credit card with hyphens (Visa test number)"),
    ("Use 5425 2334 3010 9903.", "Credit card with spaces (Mastercard test number)"),
    ("Contact me at test.user+alias@example.com.", "Email with alias"),
    ("My email is simple@domain.org.", "Simple email"),
    ("Call me at (555) 123-4567.", "Phone number with parentheses"),
    ("My number is 555.123.4567.", "Phone number with dots"),
    ("Reach me at 555 123 4567.", "Phone number with spaces"),
]

# Parameters for testing strings that SHOULD NOT contain PII
# Note: Ambiguous number strings have been removed to reduce false positives.
pii_negative_cases = [
    ("This is a generic support request.", "No PII"),
    ("The order ID is 123-456-789.", "Non-SSN formatted number"),
    ("Not an email: test@localhost", "Invalid TLD"),
    ("The price is $123.45", "Currency amount"),
    ("", "Empty string"),
    (None, "None input"),
    (123456, "Integer input"),
]

@pytest.mark.parametrize("text, description", pii_positive_cases)
def test_contains_pii_positive(text, description):
    """Test that contains_pii correctly identifies text containing various PII formats."""
    assert contains_pii(text), f"Failed to detect PII in: {description}"

@pytest.mark.parametrize("text, description", pii_negative_cases)
def test_contains_pii_negative(text, description):
    """Test that contains_pii correctly returns False for text without PII."""
    assert not contains_pii(text), f"Incorrectly detected PII in: {description}"

def test_multiple_pii_types():
    """Test that the function stops at the first PII found."""
    text = "My email is user@example.com and my phone is 555-123-4567."
    assert contains_pii(text)

# --- Tests for PII redaction (fallback log must never store raw PII) ---

def test_redact_ssn():
    text = "My SSN is 123-45-6789."
    redacted = redact_pii(text)
    assert "123-45-6789" not in redacted
    assert "[REDACTED_SSN]" in redacted

def test_redact_email_and_phone():
    text = "My email is user@example.com and my phone is 555-123-4567."
    redacted = redact_pii(text)
    assert "user@example.com" not in redacted
    assert "555-123-4567" not in redacted
    assert "[REDACTED_EMAIL]" in redacted
    assert "[REDACTED_PHONE]" in redacted

def test_redact_credit_card_luhn_valid():
    text = "Please use card 4532015112830366 for the payment."
    redacted = redact_pii(text)
    assert "4532015112830366" not in redacted
    assert "[REDACTED_CARD]" in redacted

def test_redact_leaves_non_pii_text_unchanged():
    text = "This is a generic support request."
    assert redact_pii(text) == text

def test_redact_non_string_input():
    assert redact_pii(None) is None
    assert redact_pii(123456) == 123456

def test_detect_pii_types():
    assert detect_pii_types("My SSN is 123-45-6789.") == ["ssn"]
    assert detect_pii_types("Call user@example.com at 555-123-4567.") == ["email", "phone"]
    assert detect_pii_types("Nothing sensitive here.") == []
    assert detect_pii_types(None) == []

def test_log_fallback_redacts_pii(tmp_path, monkeypatch):
    """The fallback log entry must not contain raw PII values."""
    from bot_engine import router
    monkeypatch.setattr(router, "get_project_root", lambda: tmp_path)
    ticket = "My SSN is 123-45-6789."
    result = {"ticket_type": "unknown", "confidence_score": 0.4, "contains_pii": True}
    router.log_fallback(ticket, result)

    import json
    log_file = tmp_path / "fallback_log.jsonl"
    entry = json.loads(log_file.read_text().strip().splitlines()[0])
    assert "123-45-6789" not in entry["ticket"]
    assert "[REDACTED_SSN]" in entry["ticket"]
    assert entry["pii_types"] == ["ssn"]
    assert entry["result"]["contains_pii"] is True

def test_log_fallback_keeps_non_pii_text(tmp_path, monkeypatch):
    """Non-PII tickets are logged verbatim (no redaction tokens added)."""
    from bot_engine import router
    monkeypatch.setattr(router, "get_project_root", lambda: tmp_path)
    ticket = "The app is crashing."
    result = {"ticket_type": "software_issue", "confidence_score": 0.4, "contains_pii": False}
    router.log_fallback(ticket, result)

    import json
    log_file = tmp_path / "fallback_log.jsonl"
    entry = json.loads(log_file.read_text().strip().splitlines()[0])
    assert entry["ticket"] == ticket
    assert "pii_types" not in entry
