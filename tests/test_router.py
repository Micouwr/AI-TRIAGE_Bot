# tests/test_router.py
import pytest
import json
from unittest.mock import patch, MagicMock
from bot_engine.router import classify_ticket, evaluate_routing

# Define a consistent set of ticket types for testing purposes
MOCK_TICKET_TYPES = [
    "access_request",
    "billing_question",
    "technical_support",
    "unknown"
]

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.client')
def test_classify_password_reset(mock_client):
    """Test classification for a standard access request."""
    # Arrange: Configure the mock LLM response
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "access_request",
        "confidence": 0.92
    })
    mock_client.models.generate_content.return_value = mock_response

    ticket_text = "Please reset my password ASAP."

    # Act: Call the function under test
    result = classify_ticket(ticket_text)

    # Assert: Verify the outcome
    assert result["ticket_type"] == "access_request"
    assert result["confidence_score"] == 0.92
    assert result["contains_pii"] is False

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.client')
def test_pii_phone_number(mock_client):
    """Test that PII is correctly detected."""
    # Arrange
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "technical_support",
        "confidence": 0.85
    })
    mock_client.models.generate_content.return_value = mock_response

    ticket_text = "My phone number is 555-123-4567."

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["contains_pii"] is True
    assert result["ticket_type"] == "technical_support"

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.client')
def test_classify_billing_question(mock_client):
    """Test classification for a standard billing question."""
    # Arrange
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "billing_question",
        "confidence": 0.88
    })
    mock_client.models.generate_content.return_value = mock_response

    ticket_text = "Can you explain this invoice?"

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["ticket_type"] == "billing_question"
    assert result["confidence_score"] == 0.88
    assert result["contains_pii"] is False

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.client')
def test_classify_unknown_with_pii(mock_client):
    """Test a low-confidence classification with PII."""
    # Arrange
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "unknown",
        "confidence": 0.40
    })
    mock_client.models.generate_content.return_value = mock_response

    ticket_text = "My ZIP is 40202 and my SSN is 123-45-6789."

    # Act
    result = classify_ticket(ticket_text)

    # Assert
    assert result["ticket_type"] == "unknown"
    assert result["confidence_score"] == 0.40
    assert result["contains_pii"] is True

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.client')
def test_llm_failure_fallback(mock_client):
    """Test the fallback mechanism when the LLM call fails."""
    # Arrange: Simulate an exception from the LLM
    mock_client.models.generate_content.side_effect = Exception("API Error")

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
@patch('bot_engine.router.client')
def test_low_confidence_triggers_fallback_log(mock_client, mock_log_fallback):
    """Test that low confidence scores trigger fallback logging."""
    # Arrange
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "technical_support",
        "confidence": 0.49
    })
    mock_client.models.generate_content.return_value = mock_response

    ticket_text = "The app is crashing."

    # Act
    classify_ticket(ticket_text)

    # Assert
    mock_log_fallback.assert_called_once()

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.CONFIDENCE_THRESHOLD', 0.5)
@patch('bot_engine.router.log_fallback')
@patch('bot_engine.router.client')
def test_high_confidence_does_not_trigger_fallback_log(mock_client, mock_log_fallback):
    """Test that high confidence scores do not trigger fallback logging."""
    # Arrange
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "access_request",
        "confidence": 0.90
    })
    mock_client.models.generate_content.return_value = mock_response

    ticket_text = "I need to reset my 2FA."

    # Act
    classify_ticket(ticket_text)

    # Assert
    mock_log_fallback.assert_not_called()

# --- Routing decision tests (escalation rules from governance/config/scope.yaml) ---

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.client')
def test_routing_escalates_below_07_confidence(mock_client):
    """A 0.65 score passes the 0.5 fallback-logging threshold but must still escalate per scope.yaml."""
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "technical_support",
        "confidence": 0.65
    })
    mock_client.models.generate_content.return_value = mock_response

    result = classify_ticket("The app is crashing.")

    assert result["routing_decision"]["route"] == "human_agent"
    assert "confidence_score < 0.7" in result["routing_decision"]["reason"]

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES + ["compliance_flag"])
@patch('bot_engine.router.client')
def test_routing_escalates_compliance_flag(mock_client):
    """A compliance_flag ticket escalates even at high confidence."""
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "compliance_flag",
        "confidence": 0.95
    })
    mock_client.models.generate_content.return_value = mock_response

    result = classify_ticket("Delete all customer records immediately.")

    assert result["routing_decision"]["route"] == "human_agent"
    assert "compliance_flag" in result["routing_decision"]["reason"]

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.client')
def test_routing_escalates_pii(mock_client):
    """A PII-flagged ticket escalates even at high confidence."""
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "technical_support",
        "confidence": 0.90
    })
    mock_client.models.generate_content.return_value = mock_response

    result = classify_ticket("My phone number is 555-123-4567.")

    assert result["contains_pii"] is True
    assert result["routing_decision"]["route"] == "human_agent"
    assert "contains_pii" in result["routing_decision"]["reason"]

@patch('bot_engine.router.TICKET_TYPES', MOCK_TICKET_TYPES)
@patch('bot_engine.router.client')
def test_routing_automated_response(mock_client):
    """A high-confidence, non-PII ticket routes to automated response."""
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "category": "access_request",
        "confidence": 0.92
    })
    mock_client.models.generate_content.return_value = mock_response

    result = classify_ticket("Please reset my password ASAP.")

    assert result["routing_decision"]["route"] == "automated_response"

def test_routing_empty_ticket_escalates():
    """An empty ticket carries an escalation decision, not just unknown fields."""
    decision = evaluate_routing({
        "ticket_type": "unknown",
        "confidence_score": 0.0,
        "contains_pii": False,
    })
    assert decision["route"] == "human_agent"

def test_routing_first_matching_rule_wins():
    """Rules apply in order: a compliance_flag at low confidence cites the compliance rule."""
    decision = evaluate_routing({
        "ticket_type": "compliance_flag",
        "confidence_score": 0.40,
        "contains_pii": False,
    })
    assert decision["route"] == "human_agent"
    assert "compliance_flag" in decision["reason"]
