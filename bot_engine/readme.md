# Router.py

## Overview

`router.py` is a core component of the AI Triage Bot, responsible for classifying tickets using the Gemini 1.5 Flash model. It includes governance layers to handle PII detection and manage low-confidence classifications.

## Functionality

- **Ticket Classification**: Uses the Gemini 1.5 Flash model to classify tickets into predefined categories.
- **Governance Layers**: Applies rules for handling PII and logging errors or low-confidence classifications.
- **Logging**: Records errors and fallback cases for audit and review purposes.

## Usage

To use `router.py`, ensure you have the necessary environment variables set, such as `GEMINI_API_KEY`. Then, you can call the `classify_ticket` function with a ticket text as input.

```python
from router import classify_ticket

ticket_text = "Example ticket text here."
result = classify_ticket(ticket_text)
print(result)
