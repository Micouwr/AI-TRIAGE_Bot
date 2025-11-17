# AI Triage Bot – LLM-Powered Governance Prototype

A Python prototype that layers ISO/IEC 42001 governance controls onto an LLM-powered help desk classification engine. Built with GPT-4o-mini to explore transparent, auditable AI in IT operations.

---

## ✅ Implemented

- **LLM classification engine** (`bot_engine/router.py`) using GPT-4o-mini with model-derived confidence scoring and error logging
- **Regex-based PII detection** (`bot_engine/pii_filters.py`) for basic data protection
- **Pytest validation** (`tests/test_router.py`) for reproducible testing, including LLM failure modes
- **JSONL fallback logging** (`fallback_log.jsonl`) for transparency and audit trails
- **Governance documentation** (`docs/iso42001_mapping.md`) mapping features to ISO/IEC 42001 clauses
- **Version history** (`lifecycle/version_history.md`) tracking actual implementation vs. roadmap

---

## 🔄 In Progress

- **Fallback log viewer** (`tools/view_fallbacks.py`) for human review of low-confidence classifications
- **Governance script skeletons** under `scripts/` (monitoring, validation, transparency, performance, quality)

---

## 📋 Roadmap

- Expand pytest coverage for CI/CD integration
- Introduce sanitized real-world data validation examples
- Integrate LLM prompt engineering for advanced classification
- Build adapters for ticketing systems (Slack, Freshdesk, Zendesk) after core stability is confirmed

---

## 🚀 How to Run

```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your_key_here"

# Run tests
python tests/test_router.py

# View fallback logs
cat fallback_log.jsonl
