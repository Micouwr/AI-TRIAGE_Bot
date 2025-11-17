# AI Triage Bot – Prototype

A Python proof-of-concept exploring how AI governance principles (ISO/IEC 42001) can be applied to help desk ticket classification. Built to demonstrate transparency, modularity, and auditability as a learning project that bridges IT infrastructure expertise with ethical AI enablement.

---

## ✅ Implemented

- **Core classification engine** (`bot_engine/router.py`) with confidence scoring
- **Regex-based PII detection** (`bot_engine/pii_filters.py`) for basic data protection  
- **Pytest validation** (`tests/test_router.py`) for reproducible testing
- **JSONL fallback logging** (`fallback_log.json`) for transparency and error tracking
- **Governance documentation** (`docs/iso42001_mapping.md`) mapping features to ISO/IEC 42001 clauses
- **Lifecycle tracking** (`lifecycle/version_history.md`) for audit-ready version history

---

## 🔄 In Progress

- Fallback log viewer (`tools/view_fallbacks.py`) for human review
- Governance script skeletons under `scripts/` folder (monitoring, validation, transparency, performance, quality)

---

## 📋 Roadmap

- Expand pytest coverage for CI/CD integration
- Introduce sanitized real-world data validation examples  
- Incorporate governance scripts into compliance workflows
- Integrate LLM prompt engineering for advanced classification
- Build adapters for ticketing systems (Slack, Freshdesk, Zendesk) after core stability is confirmed

---

## 🚀 How to Run

```bash
# Run tests
python tests/test_router.py

# View fallback logs (viewer coming soon)
cat fallback_log.json
