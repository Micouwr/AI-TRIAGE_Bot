# System Administrator Technical Guide - AI Triage Bot

**Document Status:** APPROVED  
**Operational Status:** FRAMEWORK  
**Version:** 1.0  
**Last Updated:** 2025-11-25  
**Audience:** System Administrators  
**Prerequisite:** Python development experience, system administration skills  
**Purpose:** Technical guide for system administrators when system becomes operational  

---

## 🎯 Administrator Responsibilities

As a **System Administrator**, you are responsible for:

1. **Deployment** - Installing and configuring the AI Triage Bot
2. **Maintenance** - Updating dependencies and system components
3. **Monitoring** - Tracking system health and performance
4. **Troubleshooting** - Diagnosing and resolving technical issues
5. **Security** - Managing API keys and access controls
6. **Compliance Support** - Assisting with audits and log management

---

## 📦 Installation and Deployment

### System Requirements

**Minimum Specifications:**
- Python 3.10 or higher (3.8+ supported but 3.10+ recommended)
- 4GB RAM
- 500MB disk space
- Internet connection for Gemini API access

**Operating Systems:**
- Windows 10/11
- macOS 10.15+
- Linux (Ubuntu 20.04+, RHEL 8+, or equivalent)

---

### Fresh Installation

#### Step 1: Clone the Repository
```bash
git clone https://github.com/Micouwr/AI-TRIAGE_Bot.git
cd AI-TRIAGE_Bot
```

#### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Verify installation:**
```bash
pip list
```

Expected packages:
- google-generativeai>=0.3.0
- python-dotenv>=1.0.0
- pyyaml>=6.0
- pytest>=7.4.0
- pyinstaller>=6.0.0

#### Step 4: Configure API Key

**Create `.env` file in project root:**
```bash
# .env
GEMINI_API_KEY=your_actual_api_key_here
```

**Security Note:** 
- Never commit `.env` to version control
- Verify `.env` is in `.gitignore`
- Use environment-specific keys (dev/staging/prod)

**Obtain API Key:**
1. Visit https://makersuite.google.com/app/apikey
2. Create new API key
3. Copy to `.env` file

#### Step 5: Verify Installation
```bash
# Test the backend
python -c "from bot_engine.router import classify_ticket; print('Backend OK')"

# Test the GUI
python main_gui.py
```

---

### Building Standalone Executable

#### Windows Executable
```bash
pyinstaller --onefile --windowed ^
  --add-data "governance;governance" ^
  --add-data "prompts;prompts" ^
  --name "AI-Triage-Bot" ^
  main_gui.py
```

**Output:** `dist/AI-Triage-Bot.exe`

#### Mac/Linux Executable
```bash
pyinstaller --onefile --windowed \
  --add-data "governance:governance" \
  --add-data "prompts:prompts" \
  --name "AI-Triage-Bot" \
  main_gui.py
```

**Output:** `dist/AI-Triage-Bot` (or `.app` on Mac with `--windowed`)

---

### Deployment Checklist

**Pre-Deployment:**
- [ ] All tests passing: `python -m pytest`
- [ ] API key configured and validated
- [ ] Configuration files reviewed (`governance/config/scope.yaml`)
- [ ] Log directories created and writable
- [ ] User documentation distributed

**Post-Deployment:**
- [ ] Test classification with sample tickets
- [ ] Verify log files are being created
- [ ] Confirm PII detection is working
- [ ] Train operators on basic usage
- [ ] Set up monitoring alerts

---

## ⚙️ Configuration Management

### Core Configuration File

**Location:** `governance/config/scope.yaml`
```yaml
system_name: AI-Triage-Bot
owner: William Ryan Micou
description: >
  AI-powered support triage system designed to classify incoming tickets,
  determine escalation paths, and apply governance controls in alignment
  with ISO/IEC 42001:2023.

bot_config:
  confidence_threshold: 0.5      # Adjust based on accuracy requirements
  model_name: "gemini-1.5-flash" # Model selection

ticket_types:
  - access_request
  - password_reset
  - software_issue
  - hardware_issue
  - billing_question
  - compliance_flag
  - unknown

escalation_rules:
  - "if ticket_type == compliance_flag: escalate_to: human_agent"
  - "if confidence_score < 0.7: escalate_to: human_agent"
  - "if contains_pii: escalate_to: human_agent"
  - "else: route_to: automated_response"
```

---

### Tuning Confidence Threshold

**Current Default:** 0.5 (50%)

**Adjustment Guidelines:**

| Threshold | Effect | Use Case |
|-----------|--------|----------|
| 0.3 (30%) | More auto-classifications, higher error rate | High-volume, low-risk tickets |
| 0.5 (50%) | Balanced (recommended) | General purpose |
| 0.7 (70%) | Fewer auto-classifications, lower error rate | High-stakes tickets |

**To Change:**
1. Edit `governance/config/scope.yaml`
2. Modify `confidence_threshold: 0.5` to desired value
3. Restart application
4. Monitor fallback log for 1 week
5. Adjust as needed based on accuracy metrics

---

### Adding New Ticket Categories

**Process:**

1. **Update `scope.yaml`:**
```yaml
   ticket_types:
     - access_request
     - password_reset
     - your_new_category  # Add here
```

2. **Update prompt template:**
   Edit `prompts/classification_prompt.txt` if needed

3. **Add test cases:**
```python
   # tests/test_router.py
   def test_new_category():
       # Add test for new category
```

4. **Run tests:**
```bash
   python -m pytest tests/test_router.py -v
```

5. **Document in training materials:**
   Update `docs/operator_quick_guide.md` with category definition

6. **Train operators** on new category

---

## 🔍 Monitoring and Logging

### Log Files Overview

| Log File | Purpose | Location | Retention |
|----------|---------|----------|-----------|
| `fallback_log.jsonl` | Low-confidence classifications | Project root | 90 days |
| `governance/llm_error_log.jsonl` | API failures and errors | `governance/` | 90 days |

---

### Monitoring Fallback Log

**Daily Check:**
```bash
# Count entries from today
grep "$(date +%Y-%m-%d)" fallback_log.jsonl | wc -l

# View last 10 entries
tail -n 10 fallback_log.jsonl | jq .
```

**Weekly Analysis:**
```bash
python tools/fallback_viewer.py --date-range 7 --stats-only
```

**Alert Thresholds:**
- **Warning:** > 20% of tickets in fallback log
- **Critical:** > 40% of tickets in fallback log
- **Action:** Review prompt tuning or confidence threshold

---

### Monitoring Error Log

**Check for API errors:**
```bash
# Count errors in last 24 hours
grep "$(date -d 'yesterday' +%Y-%m-%d)" governance/llm_error_log.jsonl | wc -l

# View recent errors
tail -n 20 governance/llm_error_log.jsonl | jq .
```

**Common Error Types:**

1. **API Rate Limiting**
```json
   {"error": "Resource has been exhausted", ...}
```
   **Solution:** Implement exponential backoff or upgrade API quota

2. **Authentication Failures**
```json
   {"error": "API key not valid", ...}
```
   **Solution:** Verify GEMINI_API_KEY in `.env`

3. **Malformed JSON Responses**
```json
   {"error": "LLM returned malformed JSON", ...}
```
   **Solution:** Review prompt template, may need refinement

---

### Log Rotation

**Automated Log Rotation Script:**

**File:** `scripts/rotate_logs.sh`
```bash
#!/bin/bash
# Log rotation script - Run weekly via cron

LOG_DIR="."
ARCHIVE_DIR="logs/archive"
DAYS_TO_KEEP=90

# Create archive directory
mkdir -p "$ARCHIVE_DIR"

# Rotate fallback log
if [ -f "$LOG_DIR/fallback_log.jsonl" ]; then
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    mv "$LOG_DIR/fallback_log.jsonl" "$ARCHIVE_DIR/fallback_log_$TIMESTAMP.jsonl"
    touch "$LOG_DIR/fallback_log.jsonl"
    echo "Rotated fallback log"
fi

# Rotate error log
if [ -f "$LOG_DIR/governance/llm_error_log.jsonl" ]; then
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    mv "$LOG_DIR/governance/llm_error_log.jsonl" "$ARCHIVE_DIR/llm_error_log_$TIMESTAMP.jsonl"
    touch "$LOG_DIR/governance/llm_error_log.jsonl"
    echo "Rotated error log"
fi

# Delete logs older than retention period
find "$ARCHIVE_DIR" -name "*.jsonl" -mtime +$DAYS_TO_KEEP -delete
echo "Deleted logs older than $DAYS_TO_KEEP days"
```

**Set up cron job (Linux/Mac):**
```bash
crontab -e

# Add this line to run every Sunday at 2 AM
0 2 * * 0 /path/to/AI-TRIAGE_Bot/scripts/rotate_logs.sh
```

---

## 🧪 Testing and Quality Assurance

### Running the Test Suite

**Full test suite:**
```bash
python -m pytest
```

**Verbose output:**
```bash
python -m pytest -v
```

**Specific test file:**
```bash
python -m pytest tests/test_router.py -v
```

**With coverage report:**
```bash
pip install pytest-cov
python -m pytest --cov=bot_engine --cov=risk_controls --cov-report=html
```

**View coverage:** Open `htmlcov/index.html` in browser

---

### Test Categories

#### 1. Router Tests (`tests/test_router.py`)

Tests classification logic:
- Standard ticket classifications
- PII detection integration
- Low confidence fallback logging
- Error handling and graceful degradation
- Malformed LLM response handling

#### 2. PII Filter Tests (`tests/test_pii_filters.py`)

Tests PII detection:
- SSN detection
- Credit card validation (with Luhn algorithm)
- Email detection
- Phone number patterns
- False positive prevention

---

### Adding New Tests

**Template for new test:**
```python
# tests/test_router.py
import pytest
import json
from unittest.mock import patch
from bot_engine.router import classify_ticket

@patch('bot_engine.router.model')
def test_your_new_test(mock_model):
    """Test description here."""
    # Arrange: Set up mock response
    mock_model.generate_content.return_value.text = json.dumps({
        "category": "your_category",
        "confidence": 0.85
    })
    
    ticket_text = "Your test ticket text"
    
    # Act: Call the function
    result = classify_ticket(ticket_text)
    
    # Assert: Verify results
    assert result["ticket_type"] == "your_category"
    assert result["confidence_score"] == 0.85
    assert result["contains_pii"] is False
```

---

### Pre-Release Testing Checklist

Before deploying updates:

**Functional Tests:**
- [ ] All pytest tests passing
- [ ] Manual GUI testing on target OS
- [ ] API connectivity verified
- [ ] Configuration file loads correctly
- [ ] Logs are being written

**Performance Tests:**
- [ ] Response time < 5 seconds for typical tickets
- [ ] Memory usage < 500MB during operation
- [ ] No memory leaks after 100 classifications

**Security Tests:**
- [ ] API key not exposed in logs
- [ ] PII detection working correctly
- [ ] No sensitive data in error messages

---

## 🔐 Security Best Practices

### API Key Management

**DO:**
- ✅ Store API keys in `.env` file only
- ✅ Use different keys for dev/staging/prod
- ✅ Rotate keys every 90 days
- ✅ Restrict API key permissions to minimum required
- ✅ Monitor API usage for anomalies

**DON'T:**
- ❌ Commit `.env` to version control
- ❌ Share API keys via email or chat
- ❌ Hard-code keys in source files
- ❌ Use production keys in development
- ❌ Give API keys to end users

---

### Access Controls

**File Permissions (Linux/Mac):**
```bash
# Restrict .env file
chmod 600 .env

# Restrict log files (readable by admin group only)
chmod 640 fallback_log.jsonl
chmod 640 governance/llm_error_log.jsonl
```

**Windows:**
- Right-click `.env` → Properties → Security
- Remove all users except Administrators and SYSTEM

---

### PII Data Protection

**Log File Security:**
- Fallback logs may contain PII
- Store logs on encrypted drives
- Restrict access to authorized personnel only
- Implement secure deletion after retention period

**Compliance Requirements:**
- GDPR: Right to deletion (ensure logs can be purged)
- CCPA: Access controls and audit trails
- HIPAA: Encryption at rest and in transit (if healthcare data)

---

## 🐛 Troubleshooting Guide

### Issue: "Gemini model is not initialized"

**Symptoms:**
- Error message in GUI or logs
- All classifications return "unknown" with 0% confidence

**Diagnosis:**
```bash
# Check if .env exists
ls -la .env

# Verify API key is set
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key:', 'SET' if os.getenv('GEMINI_API_KEY') else 'NOT SET')"
```

**Solution:**
1. Verify `.env` file exists in project root
2. Check API key format (no quotes, no spaces)
3. Test API key:
```python
   import google.generativeai as genai
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
   model = genai.GenerativeModel("gemini-1.5-flash")
   response = model.generate_content("Test")
   print(response.text)
```

---

### Issue: High Fallback Rate (> 40%)

**Symptoms:**
- Many tickets appearing in fallback log
- Low average confidence scores

**Diagnosis:**
```bash
python tools/fallback_viewer.py --date-range 7 --stats-only
```

**Possible Causes:**

1. **Confidence threshold too high**
   - Review `governance/config/scope.yaml`
   - Consider lowering from 0.5 to 0.4

2. **Prompt needs tuning**
   - Review `prompts/classification_prompt.txt`
   - Add more specific instructions
   - Provide examples in prompt

3. **New ticket types emerging**
   - Analyze fallback log for patterns
   - Consider adding new categories

---

### Issue: PII False Positives

**Symptoms:**
- Tickets flagged as containing PII but don't actually have any
- Common with invoice numbers, ticket IDs

**Diagnosis:**
```bash
python tools/fallback_viewer.py --contains-pii --limit 20
```

Review flagged tickets manually

**Solution:**
1. Identify pattern causing false positives
2. Update `risk_controls/pii_filters.py` regex patterns
3. Add test cases to `tests/test_pii_filters.py`
4. Verify with: `python -m pytest tests/test_pii_filters.py -v`

---

### Issue: Application Freezes/Hangs

**Symptoms:**
- GUI becomes unresponsive
- Classification button doesn't respond

**Diagnosis:**
- Check if API is responding slowly
- Look for network issues
- Review error logs

**Solution:**
1. **Add timeout to API calls:**
   Edit `bot_engine/router.py`:
```python
   response = model.generate_content(
       prompt,
       generation_config=GenerationConfig(temperature=0.1),
       request_options={"timeout": 30}  # Add 30-second timeout
   )
```

2. **Verify threading is working:**
   Check `main_gui.py` - thread should be daemon mode

---

### Issue: Tests Failing After Update

**Symptoms:**
```
FAILED tests/test_router.py::test_classify_password_reset
```

**Diagnosis:**
```bash
python -m pytest tests/test_router.py -v --tb=short
```

**Common Causes:**

1. **Mock configuration mismatch**
   - Mock return value doesn't match new expected format
   - Update mock in test file

2. **New validation added**
   - Code now validates something tests don't account for
   - Update test to provide valid data

3. **Dependency version change**
   - Package update changed behavior
   - Pin versions in `requirements.txt`

---

## 📊 Performance Optimization

### Benchmarking

**Measure classification time:**
```python
# scripts/benchmark.py
import time
from bot_engine.router import classify_ticket

test_tickets = [
    "Please reset my password",
    "My laptop won't turn on",
    "I need access to the finance folder",
    # Add more test cases
]

times = []
for ticket in test_tickets:
    start = time.time()
    result = classify_ticket(ticket)
    elapsed = time.time() - start
    times.append(elapsed)
    print(f"Ticket classified in {elapsed:.2f}s - {result['ticket_type']}")

avg_time = sum(times) / len(times)
print(f"\nAverage classification time: {avg_time:.2f}s")
```

**Target:** < 5 seconds per classification

---

### Optimization Strategies

**1. Prompt Optimization**
- Shorter prompts = faster responses
- Remove unnecessary instructions
- Keep category list concise

**2. Model Selection**
- `gemini-1.5-flash` - Fast, good for most cases (current)
- `gemini-1.5-pro` - Slower but more accurate
- Configure in `scope.yaml`

**3. Caching (Future Enhancement)**
- Cache common ticket patterns
- Reduce API calls for similar tickets

---

## 🔄 Updates and Maintenance

### Updating Dependencies

**Check for updates:**
```bash
pip list --outdated
```

**Update specific package:**
```bash
pip install --upgrade google-generativeai
```

**Update all packages:**
```bash
pip install --upgrade -r requirements.txt
```

**Best Practice:**
1. Test updates in development environment first
2. Run full test suite after updates
3. Document version changes in `lifecycle/version_history.md`

---

### Version Control Best Practices

**Branching Strategy:**
```
main - Production-ready code
├── develop - Integration branch
└── feature/your-feature - Feature branches
```

**Before Merging to Main:**
1. All tests passing
2. Code reviewed
3. Documentation updated
4. Version number incremented

---

### Backup Procedures

**What to Backup:**
- Configuration files (`governance/config/scope.yaml`)
- Log archives (`logs/archive/`)
- Custom prompt templates (`prompts/`)
- Test data (if applicable)

**What NOT to Backup:**
- `.env` file (recreate in new environment)
- `__pycache__/` directories
- Virtual environment (`venv/`)

**Backup Schedule:**
- **Daily:** Log files (automated via log rotation)
- **Weekly:** Configuration files
- **Before updates:** Full system backup

---

## 📞 Support and Escalation

### Internal Support Tiers

**Tier 1: End Users**
- Contact: System Operator or Team Lead
- Issues: Basic usage questions, classification results

**Tier 2: System Administrator (You)**
- Contact: AI Governance Lead
- Issues: Configuration, deployment, performance

**Tier 3: AI Governance Lead**
- Contact: System Owner
- Issues: Policy, compliance, strategic decisions

---

### External Support

**Google Gemini API Issues:**
- Documentation: https://ai.google.dev/docs
- Support: https://support.google.com/

**Python/Library Issues:**
- Python: https://www.python.org/community/
- Libraries: Check respective GitHub repositories

---

## 📚 Additional Resources

### Internal Documentation
- **User Guide:** `docs/operator_quick_guide.md`
- **Review Handbook:** `governance/training_materials/reviewer_handbook.md`
- **Governance:** `governance/ai_policy.md`
- **ISO Mapping:** `governance/iso42001_mapping.md`

### External Resources
- Python Documentation: https://docs.python.org/3/
- Google Gemini API: https://ai.google.dev/
- ISO/IEC 42001: https://www.iso.org/standard/81230.html
- PyInstaller: https://pyinstaller.org/

---

## ✅ Quick Reference Commands
```bash
# Installation
pip install -r requirements.txt

# Run application
python main_gui.py

# Run tests
python -m pytest

# View fallback log
python tools/fallback_viewer.py --stats-only

# Build executable
pyinstaller --onefile --add-data "governance:governance" --add-data "prompts:prompts" main_gui.py

# Check API key
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Key present:', bool(os.getenv('GEMINI_API_KEY')))"

# Monitor errors
tail -f governance/llm_error_log.jsonl | jq .

# Count today's fallbacks
grep "$(date +%Y-%m-%d)" fallback_log.jsonl | wc -l
```

---

**Questions? Contact AI Governance Lead or System Owner.**

**Document Version:** 1.0 | Last Updated: 2025-11-25
