# Governance Documentation - AI Triage Bot

**Document Status:** APPROVED  
**Last Updated:** 2025-11-29  
**Owner:** William Ryan Micou  
**Purpose:** Index and navigation for all governance documentation  

---

## 📋 Overview

This directory contains all governance documentation for the AI Triage Bot system, aligned with ISO/IEC 42001:2023 requirements for Artificial Intelligence Management Systems.

---

## 📁 Directory Structure
```
governance/
├── README.md                        (This file)
├── __init__.py
├── ai_policy.md                     (AI Policy Statement)
├── audit_procedures.md              (Audit Framework)
├── competence_requirements.md       (Training Requirements)
├── roles_and_responsibilities.md    (Role Definitions)
├── config/
│   └── scope.yaml                   (System Configuration)
└── training_materials/
    ├── admin_technical_guide.md     (System Administrator Guide)
    ├── governance_framework.md      (Executive Governance Documentation)
    └── reviewer_handbook.md         (Human Review Agent Guide)
```

---

## 📄 Core Governance Documents

### 1. AI Policy Statement (`ai_policy.md`)
**ISO Clause:** 5.2 (Policy)  
**Status:** APPROVED  
**Version:** 1.1  
**Last Updated:** 2025-11-25  

**Contents:**
- System purpose and scope
- Governance principles (human oversight, transparency, fairness, privacy)
- Risk management framework (8 identified risks)
- Roles and responsibilities
- Monitoring and continuous improvement
- Compliance references

**When to Use:** Reference for policy questions, audit preparation, stakeholder communication

---

### 2. Audit Procedures (`audit_procedures.md`)
**ISO Clause:** 9.2 (Internal Audit)  
**Status:** APPROVED  
**Version:** 1.0  
**Last Updated:** 2025-11-25  

**Contents:**
- Quarterly audit checklist
- Policy compliance verification
- Risk management assessment
- Classification accuracy testing
- PII detection effectiveness
- Log review procedures
- Audit reporting templates
- Corrective action tracking

**When to Use:** Quarterly internal audits, annual external audits, compliance verification

---

### 3. Competence Requirements (`competence_requirements.md`)
**ISO Clause:** 7.2 (Competence)  
**Status:** APPROVED  
**Version:** 1.0  
**Last Updated:** 2025-11-25  

**Contents:**
- Role definitions (4 roles: Operator, Review Agent, Administrator, Governance Lead)
- Required competencies for each role
- Training duration requirements
- Assessment criteria (80% passing threshold)
- Training records format
- Remediation procedures

**When to Use:** Onboarding new personnel, annual training refreshers, competence verification

---

### 4. Roles and Responsibilities (`roles_and_responsibilities.md`)
**ISO Clause:** 5.3 (Organizational Roles)  
**Status:** APPROVED  
**Version:** 1.0  
**Last Updated:** 2025-11-25  

**Contents:**
- System Owner responsibilities
- AI Governance Lead responsibilities
- Prompt Engineer responsibilities
- Support Operations Lead responsibilities
- Audit & Compliance Officer responsibilities
- Change management authority
- Review schedules

**When to Use:** Clarifying responsibilities, escalation procedures, change approvals

---

## 📚 Training Materials

### 1. Governance Framework Guide (`training_materials/governance_framework.md`)
**Audience:** AI Governance Lead, Compliance Officers, Executive Stakeholders  
**Status:** APPROVED  
**Version:** 1.1  
**Last Updated:** 2025-11-25  

**Contents:**
- Executive summary
- Three-layer governance model
- Detailed ISO 42001 clause-by-clause compliance mapping
- Role matrix and escalation pathways
- Key Performance Indicators (KPIs)
- Risk register
- Compliance checklist summary

**When to Use:** Executive briefings, compliance audits, governance training

---

### 2. System Administrator Technical Guide (`training_materials/admin_technical_guide.md`)
**Audience:** System Administrators  
**Status:** APPROVED  
**Version:** 1.1  
**Last Updated:** 2025-11-25  

**Contents:**
- Installation and deployment procedures
- Configuration management
- Monitoring and logging
- Testing and quality assurance
- Security best practices
- Troubleshooting guide
- Performance optimization
- Updates and maintenance

**When to Use:** System deployment, technical troubleshooting, maintenance procedures

---

### 3. Human Review Agent Handbook (`training_materials/reviewer_handbook.md`)
**Audience:** Human Review Agents  
**Status:** APPROVED  
**Version:** 1.0  
**Last Updated:** 2025-11-25  

**Contents:**
- Understanding fallback logs
- Using fallback viewer tool
- Classification validation process
- Category classification guidelines
- Common misclassification patterns
- PII validation procedures
- Quality metrics and reporting
- Escalation criteria

**When to Use:** Daily review activities, quality assurance, pattern identification

---

## ⚙️ Configuration

### System Configuration (`config/scope.yaml`)
**ISO Clause:** 8.2 (Operational Controls)  
**Status:** ACTIVE  
**Last Updated:** 2025-11-29  

**Key Settings:**
- `confidence_threshold`: 0.5 (50%)
- `model_name`: "gemini-2.5-flash"
- `ticket_types`: 7 categories
- `escalation_rules`: 4 rules

**When to Modify:**
- Adjusting confidence threshold based on accuracy metrics
- Adding new ticket categories
- Updating escalation rules
- Changing AI model

**Change Control:** All changes require System Owner approval and documentation in `lifecycle/version_history.md`

---

## 📊 Governance Metrics

### Monthly Metrics (Required)
- Classification accuracy (target: ≥85%)
- Average confidence score (target: ≥0.70)
- Fallback rate (target: <30%)
- PII detection rates

### Quarterly Metrics (Required)
- Internal audit completion
- Training completion rate (target: 100%)
- Policy review currency (target: <12 months)
- Test pass rate (target: 100%)

**Tracking:** See `governance/training_materials/reviewer_handbook.md` for metric templates

---

## 🔄 Document Review Schedule

| Document | Review Frequency | Next Review | Owner |
|----------|-----------------|-------------|-------|
| ai_policy.md | Annual | 2026-11-25 | AI Governance Lead |
| audit_procedures.md | Annual | 2026-11-25 | AI Governance Lead |
| competence_requirements.md | Annual | 2026-11-25 | AI Governance Lead |
| roles_and_responsibilities.md | Annual | 2026-11-25 | System Owner |
| scope.yaml | As needed | N/A | System Owner |
| Training materials | Annual | 2026-11-25 | AI Governance Lead |

---

## 📞 Contact

**Questions about governance documentation?**
- **AI Governance Lead:** William Ryan Micou
- **System Owner:** William Ryan Micou

**For document updates or corrections:**
- Create an issue in the GitHub repository
- Follow change management procedures in `roles_and_responsibilities.md`

---

## 🔗 Related Documentation

- **Main README:** `../README.md` - Project overview
- **Operator Guide:** `../docs/operator_quick_guide.md` - End-user instructions
- **Testing Documentation:** `../tests/README.md` - Testing procedures
- **Tools Documentation:** `../tools/README.md` - Fallback viewer usage

---

**Document Version:** 1.0 | Created: 2025-11-29
