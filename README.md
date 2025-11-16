# AI Triage Bot – Prototype

A ticket classification proof-of-concept built in Python to explore AI governance principles (ISO/IEC 42001) in help desk automation. This prototype demonstrates modular design, PII detection, and audit-ready logging concepts, with planned extensibility for LLM integration and ticketing system adapters.

## ✅ Implemented

- **Core classification engine** (`bot_engine/router.py`) with confidence scoring
- **Regex-based PII detection** (`botengine/piifilters.py`) for basic data protection
- **Assertion-based validation** (`tests/test_router.py`) for reproducible testing
- **JSON fallback logging** (`fallback_log.json`) for transparency and error tracking

## 🔄 In Progress

- Fallback log viewer (`tools/view_fallbacks.py`) for human review
- Escalation protocols documentation (`riskcontrols/escalationprotocols.md`)

## 📋 Roadmap

- Expand test coverage with pytest for CI/CD integration
- Integrate LLM prompt engineering for advanced classification
- Build adapters for ticketing systems (Slack, Freshdesk, Zendesk)

## 🎯 Governance Alignment

Designed with ISO/IEC 42001 principles: transparency in logging, modularity for auditability, and risk-aware classification thresholds.

## 🚀 How to Run

```bash
# Run tests
python tests/test_router.py

# View fallback logs (viewer coming soon)
cat fallback_log.json
