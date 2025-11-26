# Internal Audit Procedures - AI Triage Bot

**Document Status:** APPROVED  
**Operational Status:** FRAMEWORK  
**Document Version:** 1.0  
**Effective Date:** 2025-11-25  
**Owner:** William Ryan Micou  
**Audit Frequency:** Quarterly (when system becomes operational)  
**Purpose:** Audit procedures framework for ISO/IEC 42001:2023 compliance verification  

---

## 1. Audit Scope

### 1.1 Objectives
- Verify compliance with ISO/IEC 42001:2023 requirements
- Assess effectiveness of risk controls
- Validate accuracy of classification decisions
- Identify opportunities for system improvement

### 1.2 Audit Coverage

| Area | Frequency | Lead Auditor Required |
|------|-----------|----------------------|
| Policy Compliance | Quarterly | AI Governance Lead |
| Technical Controls | Quarterly | System Administrator |
| Classification Accuracy | Monthly | Human Review Agent |
| PII Detection | Quarterly | Compliance Officer |
| Fallback Logs | Monthly | Human Review Agent |
| Error Logs | Monthly | System Administrator |

---

## 2. Audit Checklist

### 2.1 Policy Compliance (Clause 5)

**Checklist Items:**

- [ ] AI Policy document is current (< 12 months old)
- [ ] All personnel have completed required training
- [ ] Training records are up-to-date and accessible
- [ ] Roles and responsibilities are clearly assigned
- [ ] Escalation procedures are documented and followed

**Evidence Required:**
- Training records from `governance/training_records/`
- Policy document review date
- Escalation log samples

**Pass Criteria:** 100% compliance with all items

---

### 2.2 Risk Management (Clause 6)

**Checklist Items:**

- [ ] PII detection patterns are tested and effective
- [ ] Confidence threshold (0.5) is appropriately set
- [ ] Fallback logging captures all low-confidence cases
- [ ] Error logging captures all LLM failures
- [ ] Risk register is reviewed and updated quarterly

**Evidence Required:**
- Test results from `tests/test_pii_filters.py`
- Sample of `fallback_log.jsonl` entries
- Sample of `governance/llm_error_log.jsonl` entries
- Risk register review meeting minutes

**Pass Criteria:** 90% or higher effectiveness in each control

---

### 2.3 Transparency (Clause 7)

**Checklist Items:**

- [ ] All classification decisions include confidence scores
- [ ] System configuration is documented in `scope.yaml`
- [ ] Prompt templates are version-controlled
- [ ] Audit logs are human-readable and accessible
- [ ] Fallback viewer tool is functional

**Evidence Required:**
- Configuration file `governance/config/scope.yaml`
- Git commit history for prompt changes
- Demonstration of fallback viewer tool
- Sample classification results with confidence scores

**Pass Criteria:** 100% compliance with documentation requirements

---

### 2.4 Operational Controls (Clause 8)

**Checklist Items:**

- [ ] System correctly classifies test tickets (>85% accuracy)
- [ ] Escalation rules in `scope.yaml` are enforced
- [ ] GUI is functional on all target platforms
- [ ] API key is securely stored (not in code)
- [ ] Error handling prevents system crashes

**Evidence Required:**
- Test suite results: `python -m pytest`
- Manual testing on Windows/Mac/Linux
- Code review of API key handling
- Error simulation tests

**Pass Criteria:** 
- 85% classification accuracy on test set
- Zero critical security findings
- Zero crashes during error conditions

---

### 2.5 Classification Accuracy Assessment

**Procedure:**

1. **Sample Selection:**
   - Randomly select 50 tickets from `fallback_log.jsonl`
   - Include tickets with confidence scores: 0.0-0.3, 0.3-0.5, 0.5-0.7, 0.7-1.0

2. **Human Review:**
   - Three independent reviewers classify each ticket
   - Use majority vote as "ground truth"
   - Compare AI classification to ground truth

3. **Metrics Calculation:**
```
   Accuracy = (Correct Classifications / Total Tickets) × 100%
   
   Precision = True Positives / (True Positives + False Positives)
   
   Recall = True Positives / (True Positives + False Negatives)
```

4. **Pass Criteria:**
   - Overall accuracy ≥ 85%
   - No category with accuracy < 70%
   - PII detection: Precision ≥ 90%, Recall ≥ 95%

**Documentation:**
Results logged in: `governance/audit_reports/accuracy_YYYY-MM-DD.json`

---

### 2.6 PII Detection Effectiveness

**Procedure:**

1. **Test Set Creation:**
   - Create 100 test tickets:
     - 50 with various PII types (SSN, email, phone, credit card)
     - 50 without PII (including edge cases)

2. **Automated Testing:**
```bash
   python -m pytest tests/test_pii_filters.py -v
```

3. **False Positive Analysis:**
   - Review tickets flagged as PII from last 30 days
   - Calculate false positive rate
   - Document common false positive patterns

4. **False Negative Review:**
   - Sample 100 tickets NOT flagged as PII
   - Manual review for missed PII
   - Calculate false negative rate

**Pass Criteria:**
- Automated tests: 100% pass rate
- False positive rate: < 10%
- False negative rate: < 5%

**Documentation:**
Results logged in: `governance/audit_reports/pii_detection_YYYY-MM-DD.json`

---

## 3. Log Review Procedures

### 3.1 Fallback Log Review

**Frequency:** Monthly

**Procedure:**

1. **Open fallback log:**
```bash
   python tools/fallback_viewer.py --date-range 30
```

2. **Review Categories:**
   - Count tickets by classification
   - Identify categories with high fallback rates
   - Flag patterns indicating prompt tuning needs

3. **Sample Deep Dive:**
   - Select 20 random fallback tickets
   - Verify correct handling
   - Document improvement opportunities

4. **Report Generation:**
   - Summary statistics (total, by category, by confidence range)
   - Trends vs. previous month
   - Recommendations for improvement

**Documentation:**
Report saved to: `governance/audit_reports/fallback_review_YYYY-MM.md`

---

### 3.2 Error Log Review

**Frequency:** Monthly

**Procedure:**

1. **Open error log:**
```bash
   cat governance/llm_error_log.jsonl | jq .
```

2. **Categorize Errors:**
   - API failures (network, rate limit, authentication)
   - Malformed responses (JSON parsing errors)
   - Unexpected exceptions

3. **Root Cause Analysis:**
   - Identify recurring error patterns
   - Determine if errors are transient or systematic
   - Assess impact on system availability

4. **Corrective Actions:**
   - Document required code fixes
   - Update error handling if needed
   - Escalate to AI Governance Lead if patterns emerge

**Documentation:**
Report saved to: `governance/audit_reports/error_review_YYYY-MM.md`

---

## 4. Audit Reporting

### 4.1 Report Structure
```markdown
# AI Triage Bot Audit Report

**Audit Period:** YYYY-MM-DD to YYYY-MM-DD  
**Auditor:** [Name]  
**Report Date:** YYYY-MM-DD  

## 1. Executive Summary
- Overall compliance status
- Key findings
- Recommended actions

## 2. Detailed Findings

### 2.1 Policy Compliance
- [Pass/Fail] with details

### 2.2 Risk Management
- [Pass/Fail] with details

### 2.3 Transparency
- [Pass/Fail] with details

### 2.4 Operational Controls
- [Pass/Fail] with details

### 2.5 Classification Accuracy
- Metrics and analysis

### 2.6 PII Detection
- Metrics and analysis

## 3. Non-Conformities
| ID | Severity | Description | Remediation Plan | Due Date |
|----|----------|-------------|------------------|----------|
| NC-001 | High | [Description] | [Action] | YYYY-MM-DD |

## 4. Opportunities for Improvement
| ID | Description | Expected Benefit | Priority |
|----|-------------|-----------------|----------|
| OFI-001 | [Description] | [Benefit] | High/Med/Low |

## 5. Follow-Up Actions
- [ ] Action 1 (Owner: [Name], Due: YYYY-MM-DD)
- [ ] Action 2 (Owner: [Name], Due: YYYY-MM-DD)

## 6. Next Audit Date
[YYYY-MM-DD]
```

### 4.2 Report Distribution
- AI Governance Lead (within 48 hours)
- System Owner (within 1 week)
- Relevant stakeholders (within 1 week)

### 4.3 Report Storage
Location: `governance/audit_reports/`

Retention: 7 years (compliance requirement)

---

## 5. Corrective Action Tracking

### 5.1 Non-Conformity Process

1. **Identification:** Documented in audit report
2. **Root Cause Analysis:** Within 1 week
3. **Corrective Action Plan:** Within 2 weeks
4. **Implementation:** Per action plan timeline
5. **Verification:** Follow-up audit within 3 months

### 5.2 Tracking Format
```json
{
  "nc_id": "NC-2025-001",
  "audit_date": "2025-11-25",
  "severity": "High",
  "description": "PII false negative rate exceeded threshold",
  "root_cause": "Regex pattern missing international phone formats",
  "corrective_action": "Update pii_filters.py with international patterns",
  "assigned_to": "System Administrator",
  "due_date": "2025-12-25",
  "status": "In Progress",
  "verification_date": null,
  "verified_by": null
}
```

Storage: `governance/corrective_actions.jsonl`

---

## 6. Continuous Monitoring

### 6.1 Automated Checks

**Daily Monitoring (via cron or scheduled task):**
```bash
#!/bin/bash
# governance/scripts/daily_check.sh

# Check for new errors in past 24 hours
ERROR_COUNT=$(grep -c "$(date -d 'yesterday' '+%Y-%m-%d')" governance/llm_error_log.jsonl)

if [ $ERROR_COUNT -gt 10 ]; then
    echo "ALERT: High error rate detected ($ERROR_COUNT errors)"
    # Send notification
fi

# Check fallback log size
FALLBACK_SIZE=$(wc -l < fallback_log.jsonl)
echo "Fallback log entries: $FALLBACK_SIZE"
```

**Weekly Monitoring:**
- Confidence score distribution analysis
- Classification category trends
- PII detection rate trends

---

## 7. External Audit Preparation

### 7.1 Annual External Audit Checklist

**30 Days Before Audit:**
- [ ] Compile all audit reports from past year
- [ ] Review and update all governance documents
- [ ] Ensure all training records are current
- [ ] Run full test suite and document results
- [ ] Prepare system demonstration environment

**7 Days Before Audit:**
- [ ] Review all non-conformities and status
- [ ] Prepare evidence binders (digital)
- [ ] Brief all personnel on audit process
- [ ] Test fallback viewer tool functionality

**Day of Audit:**
- [ ] Provide auditor with access to documentation
- [ ] Demonstrate system operation
- [ ] Provide log samples as requested
- [ ] Document auditor observations

---

## 8. Audit Tool: Fallback Viewer

**Purpose:** Facilitate human review of flagged tickets

**Usage:**
```bash
python tools/fallback_viewer.py [options]

Options:
  --date-range DAYS    Show entries from last N days
  --min-confidence X   Filter by minimum confidence score
  --category CAT       Filter by ticket category
  --contains-pii       Show only PII-flagged tickets
  --export CSV         Export results to CSV file
```

**See:** `tools/fallback_viewer.py` for implementation

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-25 | W.R. Micou | Initial audit procedures |
