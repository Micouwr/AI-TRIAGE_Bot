# AI Triage Bot - ISO/IEC 42001 Governance Implementation

A work-in-progress system implementing ISO/IEC 42001:2023 governance controls in an LLM-powered support ticket classification application. Built with Google Gemini 2.5 Flash to demonstrate practical application of AI management system requirements.

---

## ✅ Current Features

- **Graphical User Interface** (`main_gui.py`) for interactive ticket classification
- **Standalone Executable** capability via PyInstaller for cross-platform distribution
- **LLM Classification Engine** (`bot_engine/router.py`) using Gemini 2.5 Flash with configurable confidence scoring and error handling
- **PII Detection** (`risk_controls/pii_filters.py`) with regex patterns and Luhn algorithm validation
- **Pytest Suite** (`tests/`) covering classification logic, PII detection, and edge cases
- **Centralized Configuration** (`governance/config/scope.yaml`) for system settings, ticket types, and model parameters
- **Governance Framework** with JSONL logging, audit procedures, and ISO/IEC 42001 documentation

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ (3.8+ supported but 3.10+ recommended)
- A Gemini API key (set as environment variable `GEMINI_API_KEY`)
  - Free tier supported (15 requests per minute)
  - Get your key at: https://makersuite.google.com/app/apikey

### Installation

1. **Clone the Repository:**
```bash
   git clone https://github.com/Micouwr/AI-TRIAGE_Bot.git
   cd AI-TRIAGE_Bot
```

2. **Create Virtual Environment:**
```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install Dependencies:**
```bash
   pip install --upgrade pip
   pip install -r requirements.txt
```

4. **Configure API Key:**
   Create a `.env` file in the project root:
```
   GEMINI_API_KEY=your_actual_api_key_here
```

5. **Verify Installation:**
```bash
   python -c "from bot_engine.router import classify_ticket; print('Backend OK')"
```

---

## 🖥️ Running the Application

### GUI Application
```bash
python main_gui.py
```

This launches the AI Ticket Classifier GUI where you can:
- Enter ticket text
- View classification results with confidence scores
- See PII detection flags

---

## 🏗️ Building Standalone Executable

### Windows
```bash
pyinstaller --onefile --windowed ^
  --add-data "governance;governance" ^
  --add-data "prompts;prompts" ^
  --name "AI-Triage-Bot" ^
  main_gui.py
```

### Mac/Linux
```bash
pyinstaller --onefile --windowed \
  --add-data "governance:governance" \
  --add-data "prompts:prompts" \
  --name "AI-Triage-Bot" \
  main_gui.py
```

**Output Location:** `dist/AI-Triage-Bot` (or `.exe` on Windows)

---

## 🧪 Running Tests
```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run specific test file
python -m pytest tests/test_router.py -v

# Run with coverage report
pip install pytest-cov
python -m pytest --cov=bot_engine --cov=risk_controls --cov-report=html
```

---

## 📁 Project Structure
```
AI-TRIAGE_Bot/
├── bot_engine/
│   ├── __init__.py
│   └── router.py                    # Core classification logic
├── risk_controls/
│   ├── __init__.py
│   └── pii_filters.py               # PII detection with Luhn algorithm
├── governance/
│   ├── __init__.py
│   ├── ai_policy.md                 # AI policy statement
│   ├── audit_procedures.md          # Audit framework
│   ├── competence_requirements.md   # Training requirements
│   ├── roles_and_responsibilities.md # Role definitions
│   ├── config/
│   │   └── scope.yaml               # System configuration
│   └── training_materials/
│       ├── admin_technical_guide.md
│       ├── governance_framework.md
│       └── reviewer_handbook.md
├── docs/
│   ├── operator_quick_guide.md      # User guide
│   └── PORTFOLIO.md                 # Project portfolio
├── tests/
│   ├── __init__.py
│   ├── test_router.py               # Router tests
│   └── test_pii_filters.py          # PII detection tests
├── tools/
│   ├── __init__.py
│   └── fallback_viewer.py           # Log analysis tool
├── prompts/
│   └── classification_prompt.txt    # LLM prompt template
├── lifecycle/
│   └── version_history.md           # Version tracking
├── main_gui.py                      # GUI application
├── requirements.txt                 # Python dependencies
├── .env                             # API key (create this, not in repo)
├── .gitignore
└── README.md                        # This file
```

---

## 🔧 Configuration

### Main Configuration File

**Location:** `governance/config/scope.yaml`

Key settings:
- `confidence_threshold`: Minimum confidence score (default: 0.5)
- `model_name`: AI model to use (default: "gemini-2.5-flash")
- `ticket_types`: List of classification categories
- `escalation_rules`: Rules for human escalation

### Ticket Categories

- `access_request` - User needs access to systems/files
- `password_reset` - Password or login issues
- `software_issue` - Application problems
- `hardware_issue` - Equipment problems
- `billing_question` - Invoice or payment inquiries
- `compliance_flag` - Legal, security, or policy concerns
- `unknown` - Unable to determine category

---

## 📊 Monitoring and Logs

### Log Files

| File | Purpose | Location |
|------|---------|----------|
| `fallback_log.jsonl` | Low-confidence classifications | Project root |
| `governance/llm_error_log.jsonl` | API errors and failures | `governance/` |

### Using the Fallback Viewer
```bash
# View all entries
python tools/fallback_viewer.py

# View last 7 days
python tools/fallback_viewer.py --date-range 7

# View summary statistics only
python tools/fallback_viewer.py --stats-only

# Filter by confidence score
python tools/fallback_viewer.py --max-confidence 0.3

# Export to CSV
python tools/fallback_viewer.py --export report.csv
```

---

## 📋 ISO/IEC 42001:2023 Compliance

This system implements governance controls aligned with ISO/IEC 42001:2023:

### Clause Mapping

| ISO Clause | Implementation | Evidence |
|------------|----------------|----------|
| **Clause 4** - Context | System scope and stakeholder identification | `governance/config/scope.yaml` |
| **Clause 5** - Leadership | Policy and role definitions | `governance/ai_policy.md`, `governance/roles_and_responsibilities.md` |
| **Clause 6** - Risk Management | PII detection, confidence thresholds, fallback logging | `risk_controls/pii_filters.py`, `bot_engine/router.py` |
| **Clause 7** - Transparency | Confidence scores, audit logs, training materials | `main_gui.py`, logs, `docs/`, `governance/training_materials/` |
| **Clause 8** - Operations | Configuration management, escalation rules, testing | `governance/config/scope.yaml`, `tests/` |
| **Clause 9** - Performance | Monitoring tools, audit procedures | `tools/fallback_viewer.py`, `governance/audit_procedures.md` |
| **Clause 10** - Improvement | Feedback mechanisms, version control | `governance/training_materials/reviewer_handbook.md` |

**Full Compliance Documentation:** See `governance/training_materials/governance_framework.md`

---

## 🎓 Training and Documentation

### For Operators
- **Quick Start:** `docs/operator_quick_guide.md`
- **Competence Requirements:** `governance/competence_requirements.md`

### For Review Agents
- **Review Handbook:** `governance/training_materials/reviewer_handbook.md`

### For Administrators
- **Technical Guide:** `governance/training_materials/admin_technical_guide.md`

### For Governance Leads
- **Governance Framework:** `governance/training_materials/governance_framework.md`
- **Audit Procedures:** `governance/audit_procedures.md`

### Project Portfolio
- **Portfolio Document:** `docs/PORTFOLIO.md`

---

## 🔒 Security Considerations

### API Key Management
- Store API key in `.env` file only
- Never commit `.env` to version control
- Verify `.env` is listed in `.gitignore`
- Use different keys for dev/staging/prod environments
- Free tier rate limits: 15 requests per minute, 1,500 per day

### PII Protection
- Fallback logs may contain PII
- Restrict log file access to authorized personnel only
- Follow organizational data privacy procedures
- Implement log retention and secure deletion policies

### Access Controls
```bash
# Linux/Mac: Restrict sensitive files
chmod 600 .env
chmod 640 fallback_log.jsonl
chmod 640 governance/llm_error_log.jsonl
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "Gemini model is not initialized"**
- **Solution:** Verify `.env` file exists with valid `GEMINI_API_KEY`

**Issue: Rate limit exceeded**
- **Solution:** Free tier allows 15 requests per minute. Wait 60 seconds or upgrade API plan.

**Issue: High fallback rate (>40%)**
- **Solution:** Review `governance/config/scope.yaml` and consider adjusting `confidence_threshold`

**Issue: PII false positives**
- **Solution:** Review patterns in `risk_controls/pii_filters.py` and add test cases

**Issue: Application freezes**
- **Solution:** Check network connection and API response times

**For detailed troubleshooting:** See `governance/training_materials/admin_technical_guide.md`

---

## 📈 Development Roadmap

### Completed
- ✅ Core classification engine with Gemini 2.5 Flash
- ✅ GUI application
- ✅ PII detection with Luhn validation
- ✅ Comprehensive test suite
- ✅ ISO/IEC 42001 governance framework
- ✅ Training materials and documentation
- ✅ Fallback log viewer tool

### Planned
- [ ] Fallback log viewer GUI
- [ ] Additional PII patterns (international formats)
- [ ] Performance benchmarking suite
- [ ] Integration adapters (Zendesk, Freshdesk, Slack)
- [ ] CI/CD pipeline for automated testing
- [ ] Enhanced error recovery mechanisms

---

## 🤝 Contributing

This is a personal learning project demonstrating ISO/IEC 42001 implementation. 

If you notice issues or have suggestions:
1. Check existing issues in the repository
2. Create a detailed issue report
3. Include steps to reproduce (if applicable)

---

## 📄 License

[Add your license information here]

---

## 📞 Contact

**System Owner:** William Ryan Micou  
**Repository:** https://github.com/Micouwr/AI-TRIAGE_Bot  

---

## 🙏 Acknowledgments

- **Google Gemini API** - LLM classification engine (Gemini 2.5 Flash)
- **ISO/IEC 42001:2023** - AI Management Systems standard framework
- **NIST AI RMF** - Risk management guidance

---

**Document Version:** 1.1 | Last Updated: 2025-11-25
