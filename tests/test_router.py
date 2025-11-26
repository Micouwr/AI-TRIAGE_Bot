# tests/test_router.py
import pytest
import json
from unittest.mock import patch
from bot_engine.router import classify_ticket

# Define a consistent set of ticket types for testing purposes
MOCK_TICKET_TYPES = [
    "access_request",
    "billing_question",
    "technical_support",
    "unknown"
]

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.model')
def test_classify_password_reset(mock_model):
    """Test classification for a standard access request."""
    # Arrange: Configure the mock LLM response
    mock_response_text = json.dumps({
        "category": "access_request",
        "confidence": 0.92
    })
    mock_model.generate_content.return_value.text = mock_response_text

    ticket_text = "Please reset my password ASAP."

    # Act: Call the function under test
    result = classify_ticket(ticket_text)

    # Assert: Verify the outcome
    assert result["ticket_type"] == "access_request"
    assert result["confidence_score"] == 0.92
    assert result["contains_pii"] is False

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.model')
def test_pii_phone_number(mock_model):
    """Test that PII is correctly detected."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "technical_support",
        "confidence": 0.85
    })
    mock_model.generate_content.return_value.text = mock_response_text

    ticket_text = "My phone number is 555-123-4567."

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["contains_pii"] is True
    assert result["ticket_type"] == "technical_support"

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.model')
def test_classify_billing_question(mock_model):
    """Test classification for a standard billing question."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "billing_question",
        "confidence": 0.88
    })
    mock_model.generate_content.return_value.text = mock_response_text

    ticket_text = "Can you explain this invoice?"

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["ticket_type"] == "billing_question"
    assert result["confidence_score"] == 0.88
    assert result["contains_pii"] is False

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.model')
def test_classify_unknown_with_pii(mock_model):
    """Test a low-confidence classification with PII."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "unknown",
        "confidence": 0.40
    })
    mock_model.generate_content.return_value.text = mock_response_text

    ticket_text = "My ZIP is 40202 and my SSN is 123-45-6789."

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["ticket_type"] == "unknown"
    assert result["confidence_score"] == 0.40
    assert result["contains_pii"] is True

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.model')
def test_llm_failure_fallback(mock_model):
    """Test the fallback mechanism when the LLM call fails."""
    # Arrange: Simulate an exception from the LLM
    mock_model.generate_content.side_effect = Exception("API Error")

    ticket_text = "My request is urgent."

    # Act
    result = classify_ticket(ticket_text)

    # Assert: Verify that the function falls back to 'unknown'
    assert result["ticket_type"] == "unknown"
    assert result["confidence_score"] == 0.0
    assert result["contains_pii"] is False

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.CONFIDENCE_THRESHOLD', 0.5)
@patch('bot_engine.router.log_fallback')
@patch('bot_engine.router.model')
def test_low_confidence_triggers_fallback_log(mock_model, mock_log_fallback):
    """Test that low confidence scores trigger fallback logging."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "technical_support",
        "confidence": 0.49
    })
    mock_model.generate_content.return_value.text = mock_response_text

    ticket_text = "The app is crashing."

    # Act
    classify_ticket(ticket_text)

    # Assert
    mock_log_fallback.assert_called_once()

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.CONFIDENCE_THRESHOLD', 0.5)
@patch('bot_engine.router.log_fallback')
@patch('bot_engine.router.model')
def test_high_confidence_does_not_trigger_fallback_log(mock_model, mock_log_fallback):
    """Test that high confidence scores do not trigger fallback logging."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "access_request",
        "confidence": 0.90
    })
    mock_model.generate_content.return_value.text = mock_response_text

    ticket_text = "I need to reset my 2FA."

    # Act
    classify_ticket(ticket_text)

    # Assert
    mock_log_fallback.assert_not_called()
