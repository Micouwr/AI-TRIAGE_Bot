# Operator Quick Guide - AI Triage Bot

**Document Status:** APPROVED  
**Operational Status:** FRAMEWORK  
**Version:** 1.0  
**Last Updated:** 2025-11-25  
**Audience:** Tier 1 Support Operators  
**Purpose:** Training guide for system operators when system becomes operational  

---

## 🎯 Quick Start

### What is the AI Triage Bot?
A tool designed to classify support tickets into categories using AI-powered analysis.

### What You Need
- The AI Triage Bot application installed on your computer
- Your Gemini API key configured (ask your System Administrator)
- Basic understanding of ticket categories

---

## 📋 Step-by-Step Usage

### Step 1: Launch the Application

**Windows:**
```
Double-click: AI-Triage-Bot.exe
```

**Mac/Linux:**
```bash
python main_gui.py
```

You should see the **AI Ticket Classifier** window open.

---

### Step 2: Enter Ticket Text

1. Click in the large text box labeled **"Enter Ticket Text:"**
2. Copy and paste the ticket content from your ticketing system
3. OR type the ticket description manually

**Example Ticket:**
```
User reports they cannot access the company VPN. 
They've tried restarting their computer but still 
getting "connection failed" error.
```

---

### Step 3: Click "Classify Ticket"

1. Click the **"Classify Ticket"** button
2. Wait 2-5 seconds (status bar will show "Classifying, please wait...")
3. Results will appear in the "Classification Results" section

---

### Step 4: Review the Results

The system will show you **three pieces of information:**

#### 📂 **Result: [Category]**
The ticket classification category. Possible values:
- `access_request` - User needs access to systems/files
- `password_reset` - Password or login issues
- `software_issue` - Application problems or bugs
- `hardware_issue` - Computer, printer, phone problems
- `billing_question` - Invoice or payment inquiries
- `compliance_flag` - Legal, security, or policy concerns
- `unknown` - System couldn't determine category

#### 🎯 **Confidence: [Score]%**
How confident the AI is in its classification:
- **70-100%** - High confidence
- **50-69%** - Medium confidence
- **0-49%** - Low confidence (human review required)

#### 🔒 **Contains PII: [Yes/No]**
Whether the ticket contains Personally Identifiable Information:
- **Yes** - Ticket has sensitive data (SSN, credit card, email, phone)
- **No** - No sensitive data detected

---

## ⚠️ When to Escalate to Human Review

**ALWAYS escalate when:**

1. ✋ **Confidence < 50%**
   - System is unsure about classification
   - Example: Confidence: 42%

2. 🔒 **Contains PII: Yes**
   - Ticket has sensitive personal information
   - Requires special handling for privacy compliance

3. 🚨 **Result: compliance_flag**
   - Legal, security, or policy concerns
   - Must be reviewed by qualified personnel

4. ❌ **Result: unknown**
   - System couldn't classify the ticket
   - May need additional information or human judgment

5. ⚠️ **Error Messages**
   - If you see any error in the status bar
   - Report to System Administrator

---

## 📊 Understanding Categories

### access_request
**What it is:** User needs permission to access systems, files, or resources

**Examples:**
- "I need access to the shared marketing drive"
- "Can you add me to the Finance team folder?"
- "New employee needs VPN credentials"

**Action:** Route to Identity & Access Management team

---

### password_reset
**What it is:** Login problems, forgotten passwords, account lockouts

**Examples:**
- "I forgot my password"
- "Account is locked after too many attempts"
- "Can't log into email"

**Action:** Route to Help Desk for password reset

---

### software_issue
**What it is:** Application bugs, crashes, or functionality problems

**Examples:**
- "Excel keeps crashing when I open files"
- "Can't send emails in Outlook"
- "Software update broke my workflow"

**Action:** Route to Application Support team

---

### hardware_issue
**What it is:** Physical equipment problems

**Examples:**
- "My laptop won't turn on"
- "Printer is jammed"
- "Monitor screen is flickering"

**Action:** Route to Hardware Support or IT Services

---

### billing_question
**What it is:** Invoice, payment, or subscription inquiries

**Examples:**
- "Why was I charged twice?"
- "How do I update my payment method?"
- "Need a copy of last month's invoice"

**Action:** Route to Finance or Billing department

---

### compliance_flag
**What it is:** Legal, security, privacy, or policy concerns

**Examples:**
- "Someone is accessing files they shouldn't have"
- "Suspicious login from unknown location"
- "GDPR data deletion request"

**Action:** IMMEDIATE escalation to Compliance Officer

---

### unknown
**What it is:** Ticket doesn't fit any category or is unclear

**Examples:**
- Very short or vague descriptions
- Mixed issues (multiple problems in one ticket)
- Unusual or rare requests

**Action:** Route to senior support agent for manual classification

---

## 🔒 PII Handling Procedures

### What is PII?
**Personally Identifiable Information** - Data that can identify a specific person:

- Social Security Numbers (123-45-6789)
- Credit card numbers (1234-5678-9012-3456)
- Email addresses (user@example.com)
- Phone numbers (555-123-4567)

### When PII is Detected

**DO:**
- ✅ Note that PII was detected
- ✅ Escalate to human review agent
- ✅ Follow your organization's data privacy procedures
- ✅ Mark ticket as "sensitive" in your ticketing system

**DON'T:**
- ❌ Share the ticket content publicly
- ❌ Copy PII to unsecured locations
- ❌ Discuss PII details with unauthorized personnel
- ❌ Ignore the PII flag

---

## 🐛 Troubleshooting Common Issues

### Issue: "Error: Gemini model is not initialized"
**Cause:** API key not configured  
**Solution:** Contact your System Administrator

---

### Issue: Application freezes or won't respond
**Cause:** Network issues or API timeout  
**Solution:** 
1. Wait 30 seconds
2. Close and restart the application
3. Try again
4. If persistent, report to System Administrator

---

### Issue: All tickets show "unknown" with 0% confidence
**Cause:** Possible API outage or configuration problem  
**Solution:**
1. Check your internet connection
2. Try 2-3 different tickets
3. If issue persists, report to System Administrator
4. Route tickets manually until system is restored

---

### Issue: Results seem incorrect
**Cause:** AI misclassification  
**Solution:**
1. Use your judgment - the AI is a tool to assist you, not replace you
2. Manually reclassify if needed
3. Log the issue for quality improvement tracking

---

## 📞 Getting Help

### For Technical Problems
**Contact:** System Administrator  
**Email:** [Your IT Support Email]  
**Phone:** [Your IT Support Phone]

### For Classification Questions
**Contact:** Human Review Agent or Team Lead  
**Process:** Escalate via your normal support workflow

### For Training Refreshers
**Contact:** Training Coordinator  
**Reference:** `governance/competence_requirements.md`

---

## ✅ Best Practices

### DO:
- ✅ Read the entire ticket before classifying
- ✅ Trust high-confidence results (70%+)
- ✅ Escalate when confidence is below 50%
- ✅ Always respect PII flags
- ✅ Use your human judgment when results seem wrong
- ✅ Report recurring issues to your supervisor

### DON'T:
- ❌ Skip reading the classification results
- ❌ Override PII flags without proper authorization
- ❌ Route compliance-flagged tickets without escalation
- ❌ Share API keys or credentials
- ❌ Modify system configuration files

---

## 🎓 Quick Reference Card

| Situation | Action |
|-----------|--------|
| Confidence ≥ 70% | Use classification, route accordingly |
| Confidence 50-69% | Review carefully, use judgment |
| Confidence < 50% | Escalate to human review |
| Contains PII: Yes | Follow PII handling procedures, escalate |
| Result: compliance_flag | IMMEDIATE escalation |
| Result: unknown | Escalate to senior agent |
| System error | Report to System Administrator |

---

## 📚 Additional Resources

- **Full Documentation:** `README.md`
- **Policy Overview:** `governance/ai_policy.md`
- **Category Definitions:** `governance/config/scope.yaml`
- **Training Requirements:** `governance/competence_requirements.md`

---

**Questions? Contact your supervisor or System Administrator.**

**Document Version:** 1.0 | Last Updated: 2025-11-25
```

---

