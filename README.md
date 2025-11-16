# AI Triage Bot - Prototype

A ticket classification proof-of-concept built in Python to explore AI governance principles (ISO/IEC 42001) in help desk automation.  
This prototype demonstrates modular design, PII detection, and audit-ready logging concepts, with planned extensibility for governance scripts, real-world data validation, and eventual ticketing system adapters.

---

## ✅ Implemented

- **Core classification engine** (`bot_engine/router.py`) with confidence scoring
- **Regex-based PII detection** (`bot_engine/pii_filters.py`) for basic data protection
- **Assertion-based validation** (`tests/test_router.py`) for reproducible testing
- **JSON fallback logging** (`fallback_log.json`) for transparency and error tracking
- **Governance documentation** (`docs/iso42001_mapping.md`) mapping features to ISO/IEC 42001 clauses
- **Lifecycle tracking** (`lifecycle/version_history.md`) for audit-ready version history

---

## 🔄 In Progress

- Fallback log viewer (`tools/view_fallbacks.py`) for human review
- Escalation protocols documentation (`risk_controls/fallback_protocols.md`)
- Integration of governance scripts under `scripts/`:
  - Monitoring (`scripts/monitoring/pipeline_health.py`)
  - Validation (`scripts/validation/schema_validator.py`)
  - Transparency (`scripts/transparency/data_lineage.py`)
  - Performance (`scripts/performance/db_analyzer.py`)
  - Quality (`scripts/quality/data_assertions.py`)

---

## 📋 Roadmap

- Expand test coverage with pytest for CI/CD integration
- Introduce sanitized real-world data examples for validation
- Incorporate governance scripts into compliance workflows
- Integrate LLM prompt engineering for advanced classification
- Build adapters for ticketing systems (Slack, Freshdesk, Zendesk) **after core stability is confirmed**

---

## 🎯 Governance Alignment

Designed with ISO/IEC 42001 principles:
- **Transparency** in logging and fallback handling
- **Modularity** for auditability and lifecycle tracking
- **Risk management** through PII detection, schema validation, and escalation protocols
- **Auditability** via assertion-based testing, version history, and quality gates

For detailed compliance mapping and lifecycle evidence:
- [ISO/IEC 42001 Mapping](docs/iso42001_mapping.md)
- [Version History](lifecycle/version_history.md)

---

## 🚀 How to Run

```bash
# Run tests
python tests/test_router.py

# View fallback logs (viewer coming soon)
cat fallback_log.json