AI Triage Bot

📌 Overview

AI Triage Bot is a governance‑grade ticket classification system designed for enterprise support environments. It classifies incoming tickets, detects sensitive information (PII), and enforces fallback logging for audit readiness. Built with modular Python components, it aligns with ISO/IEC 42001 principles of transparency, risk control, and accountability.

---

🧱 Architecture
- bot_engine/router.py → Core classification engine with confidence scoring  
- botengine/piifilters.py → Regex‑based PII detection  
- tests/test_router.py → Assertion‑based test suite for validation  
- fallback_log.json → Auto‑generated log of low‑confidence or unknown tickets  
- tools/view_fallbacks.py → Human‑readable fallback viewer (to be added)  
- riskcontrols/escalationprotocols.md → Escalation triggers and governance rules (to be added)  

---

⚖️ Governance Alignment
- Transparent fallback logging  
- Assertion‑based validation for audit trails  
- Modular design for audit‑ready deployment  
- ISO/IEC 42001 alignment: accountability, risk management, audit readiness  

---

🚀 How to Run
`bash

Run tests
python tests/test_router.py

View fallback logs
python tools/view_fallbacks.py
`

---

📂 Roadmap
- Add fallback viewer (tools/view_fallbacks.py)  
- Define escalation protocols (riskcontrols/escalationprotocols.md)  
- Extend test coverage with pytest for CI/CD  
- Optional: integrate LLM prompt engineering for advanced classification  
- Optional: build adapters for ticketing systems (Freshdesk, Zendesk, etc.)  

---