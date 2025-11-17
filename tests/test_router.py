# tests/test_router.py
import pytest
import json
from unittest.mock import patch, mock_open
from bot_engine.router import classify_ticket

# Mock the YAML file read
MOCK_YAML_CONFIG = """
ticket_types:
  - access_request
  - billing_question
  - technical_support
  - unknown
"""

@patch('builtins.open', new_callable=mock_open, read_data=MOCK_YAML_CONFIG)
@patch('bot_engine.router.model.generate_content')
def test_classify_password_reset(mock_generate_content, mock_file):
    """Test classification for a standard access request."""
    # Arrange: Configure the mock LLM response
    mock_response_text = json.dumps({
        "category": "access_request",
        "confidence": 0.92
    })
    mock_generate_content.return_value.text = mock_response_text

    ticket_text = "Please reset my password ASAP."

    # Act: Call the function under test
    result = classify_ticket(ticket_text)

    # Assert: Verify the outcome
    assert result["ticket_type"] == "access_request"
    assert result["confidence_score"] == 0.92
    assert result["contains_pii"] is False

@patch('builtins.open', new_callable=mock_open, read_data=MOCK_YAML_CONFIG)
@patch('bot_engine.router.model.generate_content')
def test_pii_phone_number(mock_generate_content, mock_file):
    """Test that PII is correctly detected."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "technical_support",
        "confidence": 0.85
    })
    mock_generate_content.return_value.text = mock_response_text

    ticket_text = "My phone number is 555-123-4567."

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["contains_pii"] is True
    assert result["ticket_type"] == "technical_support"

@patch('builtins.open', new_callable=mock_open, read_data=MOCK_YAML_CONFIG)
@patch('bot_engine.router.model.generate_content')
def test_classify_billing_question(mock_generate_content, mock_file):
    """Test classification for a standard billing question."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "billing_question",
        "confidence": 0.88
    })
    mock_generate_content.return_value.text = mock_response_text

    ticket_text = "Can you explain this invoice?"

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["ticket_type"] == "billing_question"
    assert result["confidence_score"] == 0.88
    assert result["contains_pii"] is False

@patch('builtins.open', new_callable=mock_open, read_data=MOCK_YAML_CONFIG)
@patch('bot_engine.router.model.generate_content')
def test_classify_unknown_with_pii(mock_generate_content, mock_file):
    """Test a low-confidence classification with PII."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "unknown",
        "confidence": 0.40
    })
    mock_generate_content.return_value.text = mock_response_text

    ticket_text = "My ZIP is 40202 and my SSN is 123-45-6789."

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["ticket_type"] == "unknown"
    assert result["confidence_score"] == 0.40
    assert result["contains_pii"] is True

@patch('builtins.open', new_callable=mock_open, read_data=MOCK_YAML_CONFIG)
@patch('bot_engine.router.model.generate_content')
def test_llm_failure_fallback(mock_generate_content, mock_file):
    """Test the fallback mechanism when the LLM call fails."""
    # Arrange: Simulate an exception from the LLM
    mock_generate_content.side_effect = Exception("API Error")

    ticket_text = "My request is urgent."

    # Act
    result = classify_ticket(ticket_text)

    # Assert: Verify that the function falls back to 'unknown'
    assert result["ticket_type"] == "unknown"
    assert result["confidence_score"] == 0.0
    assert result["contains_pii"] is False

@patch('builtins.open', new_callable=mock_open, read_data=MOCK_YAML_CONFIG)
@patch('bot_engine.router.model.generate_content')
@patch('bot_engine.router.log_fallback')
def test_low_confidence_triggers_fallback_log(mock_log_fallback, mock_generate_content, mock_file):
    """Test that low confidence scores trigger fallback logging."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "technical_support",
        "confidence": 0.49
    })
    mock_generate_content.return_value.text = mock_response_text

    ticket_text = "The app is crashing."

    # Act
    classify_ticket(ticket_text)

    # Assert
    mock_log_fallback.assert_called_once()

@patch('builtins.open', new_callable=mock_open, read_data=MOCK_YAML_CONFIG)
@patch('bot_engine.router.model.generate_content')
@patch('bot_engine.router.log_fallback')
def test_high_confidence_does_not_trigger_fallback_log(mock_log_fallback, mock_generate_content, mock_file):
    """Test that high confidence scores do not trigger fallback logging."""
    # Arrange
    mock_response_text = json.dumps({
        "category": "access_request",
        "confidence": 0.90
    })
    mock_generate_content.return_value.text = mock_response_text

    ticket_text = "I need to reset my 2FA."

    # Act
    classify_ticket(ticket_text)

    # Assert
    mock_log_fallback.assert_not_called()
