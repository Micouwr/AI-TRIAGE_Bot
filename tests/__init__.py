"""
Test Suite for AI Triage Bot
Covers router, PII filters, and edge cases.
"""

__all__ = []
```

---

## **FIX #7: Missing Prompt File**

Your router looks for `prompts/classification_prompt.txt` but you have `.md` files. 

### **Create: `prompts/classification_prompt.txt`**
```
You are a help desk triage assistant. Classify the ticket into ONE category: {categories}.

Return ONLY a valid JSON object with these exact keys:
- "category": one of the allowed categories
- "confidence": a float between 0.0 and 1.0

Do not include any explanations, markdown formatting, or additional text. Only return the JSON object.

Example:
{{"category": "access_request", "confidence": 0.92}}
