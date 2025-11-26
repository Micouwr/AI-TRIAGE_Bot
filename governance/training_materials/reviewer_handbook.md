# Human Review Agent Handbook - AI Triage Bot

**Document Status:** APPROVED  
**Operational Status:** FRAMEWORK  
**Version:** 1.0  
**Last Updated:** 2025-11-25  
**Audience:** Human Review Agents  
**Prerequisite:** Completion of Tier 1 Operator training  
**Purpose:** Training framework for human review agents when system becomes operational  

---

## 🎯 Your Role

As a **Human Review Agent**, you are the quality assurance layer for the AI Triage Bot. Your responsibilities include:

1. **Review flagged tickets** from the fallback log
2. **Validate or correct** AI classifications
3. **Identify patterns** indicating system issues
4. **Provide feedback** for continuous improvement
5. **Escalate concerns** to the AI Governance Lead

---

## 📊 Understanding the Fallback Log

### What is the Fallback Log?

The `fallback_log.jsonl` file contains tickets that were automatically flagged for human review due to:

- Low confidence scores (< 50%)
- Category classified as "unknown"
- System errors during classification

**Location:** `fallback_log.jsonl` (project root directory)

### Log Entry Structure
```json
{
  "ticket": "User cannot access shared drive...",
  "result": {
    "ticket_type": "access_request",
    "confidence_score": 0.42,
    "contains_pii": false,
    "model": "gemini-1.5-flash"
  },
  "timestamp": "2025-11-25T14:23:45.123456+00:00"
}
```

**Fields Explained:**
- `ticket` - The original ticket text
- `ticket_type` - AI's classification
- `confidence_score` - AI's confidence (0.0 - 1.0)
- `contains_pii` - Whether PII was detected
- `timestamp` - When the ticket was classified

---

## 🔧 Using the Fallback Viewer Tool

### Basic Usage
```bash
# View all fallback entries
python tools/fallback_viewer.py

# View entries from last 7 days
python tools/fallback_viewer.py --date-range 7

# View only low-confidence entries
python tools/fallback_viewer.py --max-confidence 0.3

# Export to CSV for analysis
python tools/fallback_viewer.py --date-range 30 --export review_report.csv
```

### Daily Review Workflow

**Step 1: Generate Summary Statistics**
```bash
python tools/fallback_viewer.py --stats-only
```

Review the output to understand:
- How many tickets need review
- Which categories have most fallbacks
- Average confidence scores
- PII detection rate

**Step 2: Review Recent Entries**
```bash
python tools/fallback_viewer.py --date-range 1 --limit 20
```

**Step 3: Export for Documentation**
```bash
python tools/fallback_viewer.py --date-range 7 --export weekly_review.csv
```

---

## ✅ Classification Validation Process

### For Each Flagged Ticket:

#### 1. Read the Complete Ticket
- Read the entire ticket text carefully
- Understand the user's issue or request
- Note any context clues

#### 2. Evaluate AI Classification

**Ask yourself:**
- Is the AI's classification correct?
- If incorrect, what should the category be?
- Why might the AI have misclassified this?

#### 3. Check Confidence Score

**Confidence Analysis:**
- **0-30%:** AI had very little certainty
- **31-49%:** AI was uncertain but had a preference
- **50-69%:** Medium confidence (shouldn't be in fallback log with default settings)
- **70-100%:** High confidence (rare in fallback log)

#### 4. Verify PII Detection

**Review for:**
- Social Security Numbers
- Credit card numbers
- Email addresses
- Phone numbers
- Addresses or other identifying information

**Note:** Both false positives and false negatives

#### 5. Document Your Decision

**Create a review record:**
```json
{
  "timestamp": "2025-11-25T10:30:00Z",
  "reviewer": "Your Name",
  "ticket_id": "fallback-entry-123",
  "ai_classification": "software_issue",
  "ai_confidence": 0.42,
  "correct_classification": "hardware_issue",
  "reason": "User mentioned laptop screen flickering (hardware symptom)",
  "action_taken": "Rerouted to hardware support",
  "feedback_notes": "AI may need more hardware-related training examples"
}
```

Save to: `governance/review_records/`

---

## 📂 Category Classification Guidelines

### Decision Tree for Ambiguous Cases
```
Is it about gaining access to something?
├─ Yes → access_request
└─ No ↓

Is it about login/password problems?
├─ Yes → password_reset
└─ No ↓

Is it about software not working correctly?
├─ Yes → software_issue
└─ No ↓

Is it about physical equipment problems?
├─ Yes → hardware_issue
└─ No ↓

Is it about charges/payments/invoices?
├─ Yes → billing_question
└─ No ↓

Is it a legal/security/privacy concern?
├─ Yes → compliance_flag (ESCALATE IMMEDIATELY)
└─ No ↓

Still unclear or multiple issues?
└─ unknown (escalate to senior agent)
```

---

## 🔍 Common Misclassification Patterns

### Pattern 1: Mixed Hardware/Software Issues

**Example Ticket:**
"My laptop is slow and Excel keeps crashing"

**AI Might Choose:** `software_issue` (focuses on Excel)  
**Correct Classification:** `hardware_issue` (slowness indicates hardware)  

**Why It Happens:** AI focuses on explicit application name  
**How to Help:** Provide feedback that slowness is often hardware-related

---

### Pattern 2: Vague Language

**Example Ticket:**
"It's not working"

**AI Might Choose:** `unknown` (no specifics)  
**Correct Classification:** Needs follow-up question  

**Why It Happens:** Insufficient information  
**How to Help:** Route back to user for clarification

---

### Pattern 3: Multiple Issues in One Ticket

**Example Ticket:**
"I can't log in AND I need access to the finance folder"

**AI Might Choose:** `access_request` (focused on latter part)  
**Correct Classification:** Split into two tickets  

**Why It Happens:** AI picks dominant theme  
**How to Help:** Note that ticket should be split

---

### Pattern 4: Implied vs. Explicit Issues

**Example Ticket:**
"Can you help me install Photoshop?"

**AI Might Choose:** `software_issue`  
**Correct Classification:** `access_request` (likely needs license/permission)  

**Why It Happens:** "Install" keyword triggers software category  
**How to Help:** Context matters - installations often require access requests

---

## 🔒 PII Validation and Handling

### False Positives (Flagged but NOT PII)

**Common Causes:**
- Invoice numbers that look like credit cards
- Ticket IDs in SSN format (123-45-6789)
- Internal phone extensions
- Generic example emails in tickets

**Action:** Note in review that PII detection was incorrect

---

### False Negatives (Missed PII)

**Common Missed Patterns:**
- International phone numbers
- Partial credit card numbers ("last 4 digits")
- Names combined with birthdates
- Passport numbers

**Action:** 
1. Mark as HIGH PRIORITY issue
2. Report to System Administrator immediately
3. Document for PII filter improvement

---

### PII Handling Procedure

When reviewing tickets with actual PII:

1. ✅ **DO NOT** copy PII to unsecured documents
2. ✅ Verify the ticket has been flagged in your ticketing system
3. ✅ Follow your organization's data privacy procedures
4. ✅ Ensure proper access controls on the fallback log
5. ✅ Document that PII was correctly detected

---

## 📈 Quality Metrics and Reporting

### Weekly Review Metrics

Track and report these metrics weekly:

**Metric 1: Classification Accuracy**
```
Accuracy = (Correct AI Classifications / Total Reviewed) × 100%

Target: ≥ 85%
```

**Metric 2: False Positive Rate (PII)**
```
FP Rate = (Incorrect PII Flags / Total PII Flags) × 100%

Target: < 10%
```

**Metric 3: False Negative Rate (PII)**
```
FN Rate = (Missed PII / Total with PII) × 100%

Target: < 5%
```

**Metric 4: Category Distribution**
- Track which categories have highest fallback rates
- Identify if certain categories need prompt tuning

---

### Monthly Report Template

**File:** `governance/review_reports/monthly_YYYY-MM.md`
```markdown
# Human Review Report - [Month Year]

**Reviewer:** [Your Name]  
**Period:** [Start Date] to [End Date]  
**Total Tickets Reviewed:** [Number]

## Summary Statistics
- Correct Classifications: X (Y%)
- Incorrect Classifications: X (Y%)
- PII False Positives: X
- PII False Negatives: X

## Top Misclassification Patterns
1. [Pattern description] - X occurrences
2. [Pattern description] - X occurrences
3. [Pattern description] - X occurrences

## Recommendations
- [Specific improvement suggestion]
- [Specific improvement suggestion]

## Escalations
- [Any issues escalated to AI Governance Lead]
```

---

## 🚨 When to Escalate

### Escalate to AI Governance Lead When:

1. **Systematic Bias Detected**
   - Pattern of incorrect classifications for specific ticket types
   - Example: All hardware issues misclassified as software

2. **Security Concerns**
   - Multiple PII false negatives
   - Potential data leakage issues

3. **System Performance Degradation**
   - Significant increase in fallback rate
   - Average confidence scores dropping

4. **Compliance Issues**
   - Compliance-flagged tickets not being handled properly
   - Audit trail gaps

5. **Unusual Patterns**
   - Sudden spike in "unknown" classifications
   - Error rate increase

**Escalation Process:**
1. Document the issue with evidence
2. Email AI Governance Lead with summary
3. Include supporting data (screenshots, CSV exports)
4. Follow up within 48 hours if no response

---

## 🎓 Continuous Improvement

### Providing Actionable Feedback

**Good Feedback:**
```
Issue: 15 tickets about "VPN connection failed" were 
classified as software_issue, but should be access_request 
since VPN problems are typically access/authentication related.

Suggestion: Add VPN-related keywords to access_request 
training examples.

Impact: Would reduce fallback rate by ~5% based on 
current volume.
```

**Poor Feedback:**
```
The AI is wrong sometimes.
```

---

### Self-Improvement Activities

- **Monthly:** Review your own accuracy against other reviewers
- **Quarterly:** Participate in calibration sessions with team
- **Annually:** Complete refresher training on new ticket categories

---

## 📞 Support and Resources

### For Review Questions
**Contact:** AI Governance Lead  
**Email:** [Governance Lead Email]

### For Technical Tool Issues
**Contact:** System Administrator  
**Email:** [Admin Email]

### For Process Improvements
**Submit to:** `governance/feedback/` directory  
**Format:** Markdown document with issue description and recommendation

---

## ✅ Daily Checklist

**Morning (15 minutes):**
- [ ] Run `python tools/fallback_viewer.py --stats-only`
- [ ] Note total entries since yesterday
- [ ] Check for any unusual spikes

**Mid-Day (30-60 minutes):**
- [ ] Review up to 20 fallback entries
- [ ] Document classifications in review records
- [ ] Note any patterns

**End of Day (10 minutes):**
- [ ] Update weekly metrics spreadsheet
- [ ] Flag any issues for escalation
- [ ] Export CSV if needed for weekly report

---

## 📚 Additional Resources

- **Operator Quick Guide:** `docs/operator_quick_guide.md`
- **AI Policy:** `governance/ai_policy.md`
- **Audit Procedures:** `governance/audit_procedures.md`
- **Competence Requirements:** `governance/competence_requirements.md`

---

**Questions? Contact your AI Governance Lead.**

**Document Version:** 1.0 | Last Updated: 2025-11-25
