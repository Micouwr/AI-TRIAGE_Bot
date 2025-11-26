# AI Triage Bot – LLM-Powered Governance Prototype

A Python prototype that layers ISO/IEC 42001 governance controls onto an LLM-powered help desk classification engine. Built with Gemini 1.5 Flash to explore transparent, auditable AI in IT operations.

---

## ✅ Features

- **Graphical User Interface** (`main_gui.py`) for easy, interactive ticket classification.
- **Standalone Executable** created with PyInstaller for cross-platform distribution.
- **LLM Classification Engine** (`bot_engine/router.py`) using Gemini 1.5 Flash with configurable confidence scoring and robust error handling.
- **Refined PII Detection** (`risk_controls/pii_filters.py`) with enhanced regex patterns and dedicated tests.
- **Expanded Pytest Suite** (`tests/`) covering edge cases like malformed LLM responses and empty inputs.
- **Centralized Configuration** (`governance/config/scope.yaml`) for bot settings, ticket types, and model parameters.
- **Comprehensive Governance** with JSONL fallback logging, error logging, and documentation mapping features to ISO/IEC 42001 clauses.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- An environment variable `GEMINI_API_KEY` set with your Gemini API key.

### Running the GUI Application

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application:**
    ```bash
    python main_gui.py
    ```
    This will launch the AI Ticket Classifier GUI, where you can enter ticket text and receive a classification.

### Building the Standalone Executable

For users who want to run the application without a Python environment, a standalone executable can be built.

1.  **Install Dependencies (including PyInstaller):**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Build Command:**
    ```bash
    pyinstaller --onefile --add-data "governance:governance" --add-data "prompts:prompts" main_gui.py
    ```

3.  **Find the Executable:**
    The executable will be located in the `dist/` directory.

### Running Tests

To ensure the application is working correctly, you can run the full test suite:
```bash
python -m pytest
```

---

## 📋 Project Roadmap

- Integrate a fallback log viewer for human review of low-confidence classifications.
- Introduce sanitized real-world data validation examples.
- Build adapters for ticketing systems (e.g., Slack, Freshdesk, Zendesk) after core stability is confirmed.
- Enhance CI/CD workflows for automated building and testing.
