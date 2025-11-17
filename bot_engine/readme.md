# AI-TRIAGE-BOT: bot_engine Directory

The `bot_engine` directory contains the core logic of the AI Triage Bot, specifically focusing on ticket classification and governance.

## Overview

`router.py` is a critical component of the AI-TRIAGE-BOT, responsible for classifying tickets using the Gemini 1.5 Flash model. It includes governance layers to handle PII detection and manage low-confidence classifications.

## Functionality

- **Ticket Classification**: Utilizes the Gemini 1.5 Flash model to classify tickets into predefined categories such as access requests, billing questions, technical support, or unknown.
- **Governance Layers**: Applies rules for handling PII (Personally Identifiable Information) and logging errors or low-confidence classifications to ensure compliance and auditability.
- **Logging**: Records errors and fallback cases for audit and review purposes, helping to maintain transparency and accountability.

## Usage

To use `router.py`, ensure you have the necessary environment variables set, such as `GEMINI_API_KEY`. Then, you can call the `classify_ticket` function with a ticket text as input.

```python
from bot_engine.router import classify_ticket

ticket_text = "Example ticket text here."
result = classify_ticket(ticket_text)
print(result)
