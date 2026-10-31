# AI Governance Framework Guide - AI Triage Bot

**Document Status:** APPROVED  
**Operational Status:** FRAMEWORK  
**Version:** 1.1  
**Last Updated:** 2025-11-25  
**Audience:** AI Governance Lead, Compliance Officers, Executive Stakeholders  
**Purpose:** Governance framework documentation for ISO/IEC 42001:2023 implementation  

---

## 🎯 Executive Summary

The AI Triage Bot implements ISO/IEC 42001:2023 governance controls in an LLM-powered ticket classification system. This document describes the governance framework structure, compliance mapping, and operational procedures.

### System Overview

**System Name:** AI-Triage-Bot  
**Function:** Automated classification of support tickets using Gemini 3.8 Flash  
**Status:** Work in progress - framework implementation  
**Owner:** William Ryan Micou  

---

## 📋 ISO/IEC 42001:2023 Compliance Overview

### What is ISO/IEC 42001?

ISO/IEC 42001:2023 is the international standard for **Artificial Intelligence Management Systems (AIMS)**. It provides a framework for responsible development, deployment, and use of AI systems.

---

## 🏗️ System Architecture and Governance Layers

### Three-Layer Governance Model
```
┌─────────────────────────────────────────────────┐
│         Layer 1: Policy & Documentation         │
│  (ai_policy.md, competence_requirements.md)     │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│         Layer 2: Technical Controls              │
│  (PII filters, confidence thresholds, logging)  │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│         Layer 3: Human Oversight                 │
│  (Fallback review, audits, escalation)          │
└─────────────────────────────────────────────────┘
```

### Governance Integration Points

| System Component | Governance Control | ISO Clause |
|------------------|-------------------|------------|
| LLM Classification | Confidence thresholds, fallback logging | 6.1 (Risk), 8.2 (Operations) |
| PII Detection | Automated regex + Luhn validation | 6.1 (Risk), 7.5 (Data) |
| User Interface | Clear result display with confidence scores | 7.3 (Transparency) |
| Configuration | Centralized YAML with version control | 8.2 (Operations) |
| Logging | JSONL audit trails with timestamps | 9.1 (Monitoring) |
| Review Tools | Fallback viewer for human oversight | 9.2 (Audit), 10.2 (Improvement) |

---

## 📊 Compliance Mapping: Clause-by-Clause

### Clause 4: Context of the Organization

**Requirement:** Understand organizational context and stakeholder needs

**Implementation:**
- **Documented Scope:** `governance/config/scope.yaml` defines system boundaries
- **Stakeholder Identification:** 
  - End users: Tier 1 support operators
  - Reviewers: Human review agents
  - Administrators: System admins
  - Leadership: AI Governance Lead
- **Use Case Definition:** Automated ticket triage with human escalation

**Evidence Files:**
- `governance/config/scope.yaml`
- `governance/ai_policy.md` (Section 1)
- `README.md`

**Status:** ✅ **COMPLIANT** - Full documentation of organizational context

---

### Clause 5: Leadership and Commitment

**Requirement:** Clear ownership, accountability, and policy

**Implementation:**
- **Designated Owner:** William Ryan Micou (documented in `scope.yaml`)
- **AI Policy Statement:** Comprehensive policy document with approval section
- **Role Definitions:** Clear responsibilities in competence requirements
- **Resource Allocation:** Training materials and tools provided

**Evidence Files:**
- `governance/ai_policy.md`
- `governance/competence_requirements.md`
- `governance/roles_and_responsibilities.md`
- `governance/config/scope.yaml` (owner field)

**Status:** ✅ **COMPLIANT** - Leadership framework established

---

### Clause 6: Planning (Risk Management)

**Requirement:** Identify, assess, and mitigate AI-specific risks

**Implementation:**

#### Risk 1: Incorrect Classification
- **Severity:** Medium
- **Mitigation:** 
  - Confidence threshold (default 0.5)
  - Fallback logging for review
  - Human escalation protocols
- **Monitoring:** Weekly accuracy assessments via fallback log review

#### Risk 2: PII Exposure
- **Severity:** High
- **Mitigation:**
  - Automated PII detection (SSN, credit cards, emails, phones)
  - Luhn algorithm for credit card validation
  - Automatic escalation when PII detected
  - Access controls on logs
- **Monitoring:** Quarterly false positive/negative analysis

#### Risk 3: Model Unavailability
- **Severity:** Medium
- **Mitigation:**
  - Graceful degradation (returns "unknown" on API failure)
  - Error logging for troubleshooting
  - Clear error messages to users
- **Monitoring:** Daily error log review

#### Risk 4: Bias in Classification
- **Severity:** Low
- **Mitigation:**
  - Regular audit of classification patterns
  - Diverse test set validation
  - Human review of edge cases
- **Monitoring:** Monthly bias assessment via fallback log analysis

#### Risk 5: API Rate Limiting
- **Severity:** Low
- **Mitigation:**
  - Free tier: 15 requests per minute
  - Error handling for rate limit responses
  - User notification of temporary unavailability
- **Monitoring:** Error log tracking of rate limit hits

**Evidence Files:**
- `governance/ai_policy.md` (Section 3: Risk Management)
- `risk_controls/pii_filters.py`
- `bot_engine/router.py` (error handling)
- `tests/test_pii_filters.py`, `tests/test_router.py`

**Status:** ✅ **COMPLIANT** - Comprehensive risk framework with technical controls

---

### Clause 7: Support (Transparency, Competence, Communication)

**Requirement:** Ensure adequate resources, training, and transparency

**Implementation:**

#### 7.2 Competence
- **Documented Requirements:** Role-specific competencies defined
- **Training Materials:** Four comprehensive guides covering all roles
- **Assessment Criteria:** Pass/fail thresholds (80%) and ongoing evaluation
- **Training Records:** Format specified in competence requirements

**Evidence Files:**
- `governance/competence_requirements.md`
- `docs/operator_quick_guide.md`
- `governance/training_materials/reviewer_handbook.md`
- `governance/training_materials/admin_technical_guide.md`
- `governance/training_materials/governance_framework.md` (this document)

#### 7.3 Transparency
- **Explainable Results:** Confidence scores displayed with all classifications
- **Audit Trails:** All decisions logged with timestamps
- **Configuration Visibility:** YAML files are human-readable
- **Review Tools:** Fallback viewer provides accessible log analysis

**Evidence Files:**
- `main_gui.py` (displays confidence scores)
- `fallback_log.jsonl`, `governance/llm_error_log.jsonl`
- `tools/fallback_viewer.py`

#### 7.5 Data Management
- **PII Controls:** Automated detection and flagging
- **Data Minimization:** Only preview (100 chars) logged in error logs
- **Retention Policies:** 90-day log retention documented
- **Access Controls:** Documented in admin guide

**Evidence Files:**
- `risk_controls/pii_filters.py`
- `bot_engine/router.py` (line: `ticket_preview = ticket_text[:100]`)
- `governance/training_materials/admin_technical_guide.md` (log rotation section)

**Status:** ✅ **COMPLIANT** - Comprehensive support structure for transparency and competence

---

### Clause 8: Operation (Operational Controls)

**Requirement:** Implement controls for AI system operation

**Implementation:**

#### 8.2.1 Operational Planning and Control
- **Defined Process:** Classification workflow documented
- **Configuration Management:** Centralized in `scope.yaml`
- **Escalation Rules:** Automated enforcement based on confidence/PII/category
- **Prompt Engineering:** Version-controlled templates

**Evidence Files:**
- `governance/config/scope.yaml` (escalation_rules section)
- `prompts/classification_prompt.txt`
- `bot_engine/router.py` (classification workflow)

#### 8.2.2 Change Management
- **Version Control:** Git repository with branch strategy
- **Testing Requirements:** Pytest suite required before deployment
- **Documentation Updates:** README and guides maintained
- **Rollback Capability:** Git enables easy reversion

**Evidence Files:**
- `.git/` repository history
- `tests/` directory with comprehensive test suite
- `README.md` with deployment instructions

#### 8.2.3 Outsourced Processes
- **Third-Party Model:** Gemini 3.8 Flash (Google)
- **Risk Controls:** 
  - Output validation (JSON parsing)
  - Error handling for API failures
  - No training data sent to Google (inference only)
  - API key security procedures
  - Rate limit awareness and handling
- **Monitoring:** Error logs track API failures

**Evidence Files:**
- `bot_engine/router.py` (API integration with error handling)
- `governance/llm_error_log.jsonl`
- `governance/training_materials/admin_technical_guide.md` (API key management)

**Status:** ✅ **COMPLIANT** - Operational controls implemented and documented

---

### Clause 9: Performance Evaluation

**Requirement:** Monitor, measure, and audit AI system performance

**Implementation:**

#### 9.1 Monitoring, Measurement, Analysis
- **Automated Logging:** All low-confidence and error cases captured
- **Review Tools:** Fallback viewer for statistical analysis
- **Metrics Tracking:**
  - Classification accuracy
  - Confidence score distribution
  - PII detection rates
  - Error frequencies
- **Reporting:** Weekly/monthly review templates provided

**Evidence Files:**
- `fallback_log.jsonl`
- `governance/llm_error_log.jsonl`
- `tools/fallback_viewer.py`
- `governance/training_materials/reviewer_handbook.md` (metrics section)

#### 9.2 Internal Audit
- **Audit Procedures:** Comprehensive quarterly audit checklist
- **Scope:** Policy compliance, risk controls, classification accuracy, PII effectiveness
- **Documentation:** Audit report template and corrective action tracking
- **Audit Tools:** Fallback viewer, test suite, log analysis

**Evidence Files:**
- `governance/audit_procedures.md`
- `tests/test_router.py`, `tests/test_pii_filters.py`

#### 9.3 Management Review
- **Review Schedule:** Quarterly internal, annual external
- **Review Inputs:** Audit reports, metrics, stakeholder feedback
- **Review Outputs:** Policy updates, corrective actions, improvements

**Evidence Files:**
- `governance/audit_procedures.md` (Section 7: External Audit Preparation)
- `governance/ai_policy.md` (Section 7: Policy Review)

**Status:** ✅ **COMPLIANT** - Comprehensive performance evaluation framework

---

### Clause 10: Improvement

**Requirement:** Continual improvement of AI management system

**Implementation:**

#### 10.2 Continual Improvement
- **Feedback Mechanisms:**
  - Human review provides classification corrections
  - Fallback log analysis identifies patterns
  - Error logs reveal technical issues
- **Improvement Process:**
  1. Issue identification (monitoring/audits)
  2. Root cause analysis
  3. Corrective action planning
  4. Implementation with testing
  5. Verification through metrics
- **Documentation:** Version history tracks improvements

**Evidence Files:**
- `governance/training_materials/reviewer_handbook.md` (Section: Providing Actionable Feedback)
- `governance/audit_procedures.md` (Section 5: Corrective Action Tracking)
- `lifecycle/version_history.md`

**Status:** ✅ **COMPLIANT** - Improvement framework established with clear processes

---

## 🎓 Governance Roles and Responsibilities

### Role Matrix

| Role | Primary Responsibilities | Key Competencies | Training Required |
|------|-------------------------|------------------|-------------------|
| **AI Governance Lead** | - Policy oversight<br>- Risk management<br>- Audit coordination<br>- Stakeholder communication | - ISO/IEC 42001:2023 knowledge<br>- Risk assessment<br>- Policy development | 16 hours initial<br>4 hours annual |
| **System Administrator** | - System deployment<br>- Configuration management<br>- Troubleshooting<br>- Log monitoring | - Python development<br>- YAML configuration<br>- API key security<br>- Testing procedures | 8 hours initial<br>2 hours annual |
| **Human Review Agent** | - Fallback log review<br>- Classification validation<br>- Pattern identification<br>- Feedback provision | - Ticket classification<br>- Log analysis<br>- PII handling<br>- Quality metrics | 4 hours initial<br>1 hour annual |
| **System Operator** | - Daily ticket processing<br>- Result interpretation<br>- Escalation execution | - Basic system operation<br>- Confidence interpretation<br>- PII recognition<br>- Error handling | 2 hours initial<br>30 min annual |

### Escalation Pathways
```
┌──────────────────┐
│  System Operator │ ---- Usage Questions --------> Team Lead
└──────────────────┘                                     │
         │                                               │
         │ Low Confidence / PII / Errors                 │
         ↓                                               │
┌──────────────────┐                                     │
│ Human Review     │ ---- Pattern Issues -------------> │
│ Agent            │                                     │
└──────────────────┘                                     │
         │                                               │
         │ Technical Issues / Config                     │
         ↓                                               ↓
┌──────────────────┐                          ┌──────────────────┐
│ System           │ ---- Policy/Compliance -> │ AI Governance    │
│ Administrator    │       Issues             │ Lead             │
└──────────────────┘                          └──────────────────┘
```

---

## 📈 Key Performance Indicators (KPIs)

### Operational Metrics

| Metric | Target | Measurement Frequency | Data Source |
|--------|--------|----------------------|-------------|
| **Classification Accuracy** | ≥ 85% | Monthly | Fallback log human review |
| **Average Confidence Score** | ≥ 0.70 | Weekly | Fallback log analysis |
| **Fallback Rate** | < 30% | Weekly | Fallback log count / total tickets |
| **PII False Positive Rate** | < 10% | Quarterly | PII detection audit |
| **PII False Negative Rate** | < 5% | Quarterly | PII detection audit |
| **API Error Rate** | < 5% | Daily | Error log analysis |
| **Average Response Time** | < 5 seconds | Monthly | Performance benchmarks |

### Compliance Metrics

| Metric | Target | Measurement Frequency | Data Source |
|--------|--------|----------------------|-------------|
| **Training Completion Rate** | 100% | Quarterly | Training records |
| **Audit Finding Closure** | < 30 days | Per audit | Corrective action tracker |
| **Policy Review Currency** | < 12 months | Annual | Policy document dates |
| **Test Pass Rate** | 100% | Pre-deployment | Pytest results |

---

## 🔄 Lifecycle Management

### Version Control Strategy

**Semantic Versioning:** `MAJOR.MINOR.PATCH`

- **MAJOR:** Breaking changes (e.g., new AI model, major architecture change)
- **MINOR:** New features (e.g., new ticket category, improved PII detection)
- **PATCH:** Bug fixes (e.g., error handling improvements)

**Current Version:** 1.1.0

**Version History Location:** `lifecycle/version_history.md`

---

## 🛡️ Risk Register

### Risk Assessment Matrix

| Risk ID | Risk Description | Likelihood | Impact | Risk Level | Mitigation Status |
|---------|-----------------|------------|--------|------------|-------------------|
| R-001 | Incorrect classification leads to misdirected tickets | Medium | Medium | **MEDIUM** | ✅ Mitigated (confidence thresholds) |
| R-002 | PII exposure through logs or errors | Low | High | **MEDIUM** | ✅ Mitigated (PII detection, log controls) |
| R-003 | API service disruption | Medium | Medium | **MEDIUM** | ✅ Mitigated (graceful degradation) |
| R-004 | Systematic bias in classifications | Low | Medium | **LOW** | ✅ Mitigated (regular audits) |
| R-005 | Unauthorized access to system/logs | Low | High | **MEDIUM** | ✅ Mitigated (access controls, API key security) |
| R-006 | Training data leakage to model provider | Very Low | Medium | **LOW** | ✅ Mitigated (no training, inference only) |
| R-007 | Inadequate operator training | Medium | Low | **LOW** | ✅ Mitigated (comprehensive training materials) |
| R-008 | API rate limit exceeded | Low | Low | **LOW** | ✅ Mitigated (error handling, user notification) |

**Risk Level Calculation:** Likelihood × Impact

**Review Frequency:** Quarterly (or after any security incident)

---

## 📋 Compliance Checklist Summary

### ISO/IEC 42001:2023 Compliance Status

| Clause | Requirement | Status | Evidence | Notes |
|--------|-------------|--------|----------|-------|
| **4** | Context of Organization | ✅ COMPLIANT | scope.yaml, ai_policy.md | Complete |
| **5** | Leadership & Commitment | ✅ COMPLIANT | ai_policy.md, roles_and_responsibilities.md | Complete |
| **6** | Planning (Risk Management) | ✅ COMPLIANT | ai_policy.md, pii_filters.py, router.py | Complete |
| **7.2** | Competence | ✅ COMPLIANT | competence_requirements.md, training materials | Complete |
| **7.3** | Transparency | ✅ COMPLIANT | main_gui.py, fallback_viewer.py, logs | Complete |
| **7.5** | Data Management | ✅ COMPLIANT | pii_filters.py, admin_technical_guide.md | Complete |
| **8.2** | Operational Controls | ✅ COMPLIANT | scope.yaml, router.py, tests/ | Complete |
| **9.1** | Monitoring & Measurement | ✅ COMPLIANT | Logs, fallback_viewer.py, reviewer_handbook.md | Complete |
| **9.2** | Internal Audit | ✅ COMPLIANT | audit_procedures.md, tests/ | Complete |
| **9.3** | Management Review | ✅ COMPLIANT | audit_procedures.md, ai_policy.md | Complete |
| **10.2** | Continual Improvement | ✅ COMPLIANT | reviewer_handbook.md, audit_procedures.md | Complete |

**Overall Compliance Status:** ✅ **100% COMPLIANT** for documented framework

---

## 📞 Governance Support

### For Governance Questions

**AI Governance Lead:** William Ryan Micou  
**Role:** System Owner & Lead Developer  

### For Compliance References

- **ISO/IEC 42001:2023:** https://www.iso.org/standard/81230.html
- **NIST AI RMF:** https://www.nist.gov/itl/ai-risk-management-framework
- **Google AI Principles:** https://ai.google/responsibility/principles/

### For Technical Implementation

- **Repository:** https://github.com/Micouwr/AI-TRIAGE_Bot
- **Documentation:** See `README.md` in repository
- **Training Materials:** All materials in `governance/training_materials/` and `docs/`

---

## 📚 Recommended Reading for Governance Leads

### Essential Standards and Frameworks

1. **ISO/IEC 42001:2023** - AI Management Systems (primary standard)
2. **ISO/IEC 23894:2023** - AI Risk Management
3. **ISO/IEC 38507:2022** - Governance of IT (AI implications)
4. **NIST AI Risk Management Framework** - Practical risk assessment
5. **EU AI Act** - Regulatory compliance requirements (Europe)

### Books and Resources

- "Artificial Intelligence Risk Management: A Framework for Better Outcomes" (NIST)
- "The Alignment Problem" by Brian Christian (AI ethics and safety)
- "Weapons of Math Destruction" by Cathy O'Neil (algorithmic accountability)
- Google AI's Responsible AI Practices documentation

### Professional Development

- **Certifications:** Consider ISO/IEC 42001 Lead Auditor certification
- **Communities:** Join AI governance forums and working groups
- **Conferences:** Attend AI ethics and governance conferences

---

## ✅ Final Compliance Statement

**System Name:** AI Triage Bot  
**Version:** 1.1.0  
**Standard:** ISO/IEC 42001:2023  
**Compliance Date:** 2025-11-25  
**Status:** COMPLIANT (Framework)  

This system has been designed and documented in accordance with ISO/IEC 42001:2023 requirements for Artificial Intelligence Management Systems. All mandatory clauses have been addressed with appropriate controls, documentation, and evidence.

**Scope:** Automated support ticket classification for IT help desk operations

**Governance Lead Statement:**  
This governance framework implements ISO/IEC 42001:2023 controls in a functional AI classification system. All governance controls are documented and ready for operational implementation.

**Prepared By:** William Ryan Micou  
**Date:** 2025-11-25  
**Next Review:** 2026-11-25  

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-25 | W.R. Micou | Initial framework |
| 1.1 | 2025-11-25 | W.R. Micou | Updated model to Gemini 2.5 Flash, added rate limiting risk |
---

**Document Version:** 1.1 | Last Updated: 2025-11-25
