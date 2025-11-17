# tests/test_router.py
import pytest
from bot_engine.router import classify_ticket

def test_classify_password_reset():
    ticket_text = "Please reset my password ASAP."
    expected = {
        "ticket_type": "access_request",
        "confidence_score": 0.92,
        "contains_pii": False,
    }
    assert classify_ticket(ticket_text) == expected

def test_pii_phone_number():
    ticket_text = "My phone number is 555-123-4567."
    result = classify_ticket(ticket_text)
    assert result["contains_pii"] is True

def test_classify_billing_question():
    ticket_text = "Can you explain this invoice?"
    expected = {
        "ticket_type": "billing_question",
        "confidence_score": 0.88,
        "contains_pii": False,
    }
    assert classify_ticket(ticket_text) == expected

def test_classify_unknown_with_pii():
    ticket_text = "My ZIP is 40202 and my SSN is 123-45-6789."
    result = classify_ticket(ticket_text)
    assert result["ticket_type"] == "unknown"
    assert result["confidence_score"] < 0.5
    assert result["contains_pii"] is True

def test_classify_unknown_without_pii():
    ticket_text = "I need help with something."
    expected = {
        "ticket_type": "unknown",
        "confidence_score": 0.42,
        "contains_pii": False,
    }
    assert classify_ticket(ticket_text) == expected

def test_classify_invalid_input():
    with pytest.raises(ValueError):
        classify_ticket(None)  # Assuming classify_ticket raises ValueError for invalid inputs

# Additional tests can be added here as needed
