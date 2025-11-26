# Competence Requirements - AI Triage Bot Operators

**Document Status:** APPROVED  
**Operational Status:** FRAMEWORK  
**Document Version:** 1.0  
**Effective Date:** 2025-11-25  
**Owner:** William Ryan Micou  
**Purpose:** Training framework for system operators when system becomes operational  

---

## 1. Overview

This document defines the knowledge, skills, and training required for personnel operating or interacting with the AI Triage Bot system. These requirements align with ISO/IEC 42001:2023 Clause 7.2 (Competence).

---

## 2. Role Definitions

### 2.1 System Operator (Tier 1 Support)

**Responsibilities:**
- Enter support tickets into the classification system
- Review classification results
- Execute recommended routing actions

**Required Competencies:**

| Competency | Description | Verification Method |
|------------|-------------|---------------------|
| **Basic System Operation** | Ability to launch GUI, enter text, interpret results | Hands-on demonstration |
| **Confidence Score Interpretation** | Understanding of what confidence scores mean and when to escalate | Written assessment |
| **PII Recognition** | Ability to identify when PII flag is triggered | Scenario-based quiz |
| **Error Handling** | Knowledge of what to do when system returns errors | Incident simulation |

**Training Duration:** 2 hours (initial), 30 minutes (annual refresher)

**Training Materials:**
- `README.md` - System overview and operation
- `docs/operator_quick_guide.md` - Step-by-step usage instructions
- `governance/ai_policy.md` - Policy and escalation protocols

---

### 2.2 Human Review Agent

**Responsibilities:**
- Review tickets flagged in fallback logs
- Validate or correct AI classifications
- Provide feedback on system performance

**Required Competencies:**

| Competency | Description | Verification Method |
|------------|-------------|---------------------|
| **All Tier 1 Competencies** | Foundation from System Operator role | Certificate of completion |
| **Ticket Classification Expertise** | Deep knowledge of all ticket categories | Classification accuracy test (>90%) |
| **Log File Navigation** | Ability to read and interpret JSONL logs | Practical exercise |
| **PII Handling Protocols** | Procedures for handling sensitive data | Compliance certification |
| **Feedback Documentation** | How to report classification errors | Documented feedback example |

**Training Duration:** 4 hours (initial), 1 hour (annual refresher)

**Training Materials:**
- All Tier 1 materials
- `tools/fallback_viewer.py` - Log review tool documentation
- `governance/config/scope.yaml` - Category definitions and rules

---

### 2.3 System Administrator

**Responsibilities:**
- Deploy and maintain the AI Triage Bot
- Configure system parameters
- Troubleshoot technical issues
- Monitor system health

**Required Competencies:**

| Competency | Description | Verification Method |
|------------|-------------|---------------------|
| **Python Development** | Ability to read and modify Python code | Code review assessment |
| **YAML Configuration** | Understanding of scope.yaml structure | Configuration exercise |
| **API Key Management** | Secure handling of GEMINI_API_KEY | Security checklist |
| **Log Analysis** | Interpreting error logs and fallback logs | Log investigation exercise |
| **Version Control** | Git basics for tracking changes | Git workflow demonstration |
| **Testing Procedures** | Running pytest suite and interpreting results | Test execution and reporting |

**Training Duration:** 8 hours (initial), 2 hours (annual refresher)

**Training Materials:**
- Complete codebase documentation
- `tests/` - Test suite for understanding system behavior
- `governance/iso42001_mapping.md` - Compliance requirements

---

### 2.4 AI Governance Lead

**Responsibilities:**
- Overall system accountability
- Policy compliance oversight
- Audit coordination
- Risk management

**Required Competencies:**

| Competency | Description | Verification Method |
|------------|-------------|---------------------|
| **ISO/IEC 42001 Knowledge** | Understanding of AI management system requirements | ISO certification or training |
| **Risk Assessment** | Ability to evaluate AI system risks | Risk assessment workshop |
| **Audit Management** | Conducting and responding to audits | Audit completion record |
| **Policy Development** | Creating and updating governance documents | Policy review and approval |
| **Stakeholder Communication** | Explaining AI decisions to non-technical audiences | Presentation assessment |

**Training Duration:** 16 hours (initial), 4 hours (annual refresher)

**Training Materials:**
- ISO/IEC 42001:2023 standard document
- `governance/ai_policy.md` - Complete policy framework
- Industry best practices documentation

---

## 3. Training Schedule

### 3.1 Initial Training
All personnel must complete role-specific training before system access is granted.

### 3.2 Refresher Training
- **Annual:** All roles require yearly refresher training
- **Event-Driven:** Additional training after major system updates

### 3.3 Training Records
Maintained in: `governance/training_records/`

Format:
```json
{
  "employee_id": "EMP001",
  "role": "System Operator",
  "training_date": "2025-11-25",
  "trainer": "W.R. Micou",
  "assessment_score": 95,
  "next_refresh_due": "2026-11-25"
}
```

---

## 4. Competence Verification

### 4.1 Initial Assessment
- Written test covering system operation and policies
- Practical demonstration of system usage
- Scenario-based problem solving

**Passing Criteria:** 80% or higher on all assessments

### 4.2 Ongoing Evaluation
- Monthly spot-checks on ticket handling accuracy
- Quarterly review of escalation decisions
- Annual comprehensive re-assessment

### 4.3 Remediation
Personnel scoring below 80% must:
1. Receive additional training within 2 weeks
2. Complete re-assessment within 4 weeks
3. Escalate to supervisor if second attempt fails

---

## 5. Training Resources Location
```
/governance/
  ├── ai_policy.md                    (All roles)
  ├── competence_requirements.md      (This document)
  └── training_materials/
      ├── operator_quick_guide.md     (Tier 1)
      ├── reviewer_handbook.md        (Human Review)
      ├── admin_technical_guide.md    (Administrators)
      └── governance_framework.md     (Governance Lead)
```

---

## 6. Contact for Training

**Primary Contact:** William Ryan Micou  
**Training Coordinator:** [TBD]  
**Technical Questions:** See `README.md` for support channels

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-25 | W.R. Micou | Initial competence framework |
```

---

## **REVIEW OF FILE #2: `governance/competence_requirements.md`**

### ✅ **Checklist Review:**

**Plan Compliance:**
- ✅ Document status headers added (APPROVED/FRAMEWORK)
- ✅ Added "Purpose: Training framework for system operators when system becomes operational"
- ✅ All em dashes (`—`) removed
- ✅ No over-promising language
- ✅ Written as framework/template (Option B confirmed)
- ✅ Dates corrected to 2025-11-25

**Content Quality:**
- ✅ No code to have bugs
- ✅ Markdown syntax valid
- ✅ Tables formatted correctly
- ✅ File references accurate
- ✅ JSON example is valid
- ✅ No embellishments

**Issues Found:** None

**Status:** ✅ **APPROVED - File #2 is clean and ready**

---

# **CONTEXT RECALL PROMPT**
```
I am working on an AI Triage Bot project that classifies support tickets using Google Gemini 1.5 Flash. The system is a work-in-progress implementing ISO/IEC 42001:2023 governance controls.

Current project status:
- Branch: feat/gui-and-code-refactor
- System Status: Framework implementation (not production)
- Primary Goal: Demonstrate ISO 42001 compliance in practice

We are currently cleaning up documentation to:
1. Remove all em dashes (—) and replace with hyphens (-)
2. Remove over-promising language (no "production-ready", "enterprise-grade", etc.)
3. Add document status headers (APPROVED/FRAMEWORK)
4. Update README.md to reflect current structure
5. Create docs/PORTFOLIO.md for career-focused content
6. Update lifecycle/versionhistory.md

Key rules established:
- NEVER embellish or make things up to sound impressive
- Facts only, no subjective quality claims
- Ask for approval before suggesting improvements
- System is WIP, documentation is framework for when operational

Files being corrected (9 total):
1. governance/ai_policy.md [COMPLETE]
2. governance/competence_requirements.md [COMPLETE]
3. governance/audit_procedures.md [PENDING]
4. docs/operator_quick_guide.md [PENDING]
5. governance/training_materials/reviewer_handbook.md [PENDING]
6. governance/training_materials/admin_technical_guide.md [PENDING]
7. governance/training_materials/governance_framework.md [PENDING - remove resume section]
8. README.md [PENDING - update structure]
9. docs/PORTFOLIO.md [PENDING - create new]

System owner: William Ryan Micou
Date: 2025-11-25
