# AI-TRIAGE_Bot


1. Project Overview
> AI Triage Bot is a governance‑grade ticket classification system designed for enterprise support environments. It classifies incoming tickets, detects sensitive information (PII), and enforces fallback logging for audit readiness. Built with modular Python components, it aligns with ISO/IEC 42001 principles of transparency, risk control, and accountability.

---

2. Architecture
- bot_engine/router.py → Core classification engine with confidence scoring  
- botengine/piifilters.py → Regex‑based PII detection  
- tests/test_router.py → Assertion‑based test suite for validation  
- fallback_log.json → Auto‑generated log of low‑confidence or unknown tickets  
- tools/view_fallbacks.py → Human‑readable fallback viewer (to be added)  
- riskcontrols/escalationprotocols.md → Escalation triggers and governance rules (to be added)

---

3. Governance Alignment
- Transparent fallback logging  
- Assertion‑based validation for audit trails  
- Modular design for client deployment and SaaS licensing  
- ISO/IEC 42001 alignment: accountability, risk management, audit readiness  

---

4. How to Run
`bash

Run tests
python tests/test_router.py

View fallback logs
python tools/view_fallbacks.py
`

---