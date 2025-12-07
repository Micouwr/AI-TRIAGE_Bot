# AI-TRIAGE-BOT Prototype

The `AI-TRIAGE-BOT Prototype` directory contains the core logic of the AI Triage Bot, specifically focusing on ticket classification and governance. This is a prototype version, and as such, it is subject to ongoing development and refinement.

## Overview

`router.py` is a critical component of the AI Triage Bot, responsible for classifying tickets using the Gemini 2.5 Flash model. It includes governance layers to handle PII detection and manage low-confidence classifications.

## Functionality

- **Ticket Classification**: Utilizes the Gemini 2.5 Flash model to classify tickets into predefined categories such as access requests, billing questions, technical support, or unknown.
- **Governance Layers**: Applies rules for handling PII (Personally Identifiable Information) and logging errors or low-confidence classifications to ensure compliance and auditability.
- **Logging**: Records errors and fallback cases for audit and review purposes, helping to maintain transparency and accountability.

## Usage

To use `router.py`, ensure you have the necessary environment variables set, such as `GEMINI_API_KEY`. Then, you can call the `classify_ticket` function with a ticket text as input.
```python
from AI_TRIAGE_BOT_Prototype.router import classify_ticket

ticket_text = "Example ticket text here."
result = classify_ticket(ticket_text)
print(result)
```
