# Documentation Index - Vigil Prototype

**Last Updated:** 2025-12-07  
**Owner:** William Ryan Micou  
**Purpose:** Index of all user-facing and training documentation  

---

## 📋 Overview

This directory contains all user-facing documentation, training materials, and project portfolio information for the Vigil prototype system.

---

## 📁 Directory Structure
```
docs/
├── README.md                           (This file)
├── operator_quick_guide.md             (End-user training guide)
├── PORTFOLIO.md                        (Project portfolio document)
└── iso42001_compliance_mapping.md      (ISO/IEC 42001:2023 compliance mapping)
```

---

## 📄 Documentation Files

### 1. Operator Quick Guide (`operator_quick_guide.md`)

**Audience:** Tier 1 Support Operators  
**Status:** APPROVED  
**Version:** 1.0  
**Last Updated:** 2025-11-25  
**ISO Clause:** 7.2 (Competence)  

**Contents:**
- Quick start instructions
- Step-by-step usage guide
- Understanding classification results
- When to escalate to human review
- Category definitions with examples
- PII handling procedures
- Troubleshooting common issues
- Best practices
- Quick reference card

**Training Duration:** 2 hours (initial), 30 minutes (annual refresher)

**When to Use:**
- Onboarding new operators
- Quick reference during daily operations
- Training refreshers
- Troubleshooting user questions

---

### 2. Project Portfolio (`PORTFOLIO.md`)

**Audience:** External stakeholders, recruiters, technical reviewers  
**Status:** APPROVED  
**Version:** 1.0  
**Last Updated:** 2025-11-25  

**Contents:**
- Project overview and objectives
- Technical implementation details
- ISO/IEC 42001:2023 governance implementation
- Documentation created
- Quality assurance approach
- Security and privacy implementation
- System architecture
- Skills demonstrated
- Development process
- Lessons learned
- Future enhancements

**When to Use:**
- Resume/portfolio presentation
- Project demonstrations
- Technical interviews
- Stakeholder briefings

---

### 3. ISO/IEC 42001:2023 Comprehensive Compliance Mapping (`iso42001_compliance_mapping.md`)

**Audience:** Auditors, compliance officers, governance leads  
**Status:** APPROVED  
**Version:** 1.0  
**Last Updated:** 2025-12-07  
**Purpose:** Complete mapping of system features to ISO/IEC 42001:2023 clauses

**Contents:**
- All 10 ISO/IEC 42001:2023 clauses with detailed mappings
- Evidence files for each requirement (22 supporting files documented)
- 8 identified risks with mitigations
- Compliance status tracking (95% compliant)
- Prototype feature alignment
- Comprehensive compliance checklist

**When to Use:**
- Internal audits
- External compliance reviews
- Governance oversight
- Risk assessments

---

## 🎓 Role-Based Documentation Map

### For System Operators (Tier 1 Support)
**Required Reading:**
1. ✅ `operator_quick_guide.md` - Daily usage guide
2. ✅ `../governance/ai_policy.md` - Policy overview (Sections 1-2)
3. ✅ `../governance/competence_requirements.md` - Training requirements

**Optional:**
- `../README.md` - System overview
- `../governance/roles_and_responsibilities.md` - Role clarification

**Estimated Training Time:** 2 hours

---

### For Human Review Agents
**Required Reading:**
1. ✅ `operator_quick_guide.md` - Foundation knowledge
2. ✅ `../governance/training_materials/reviewer_handbook.md` - Primary guide
3. ✅ `../governance/competence_requirements.md` - Training requirements
4. ✅ `../tools/README.md` - Fallback viewer usage

**Optional:**
- `../governance/ai_policy.md` - Full policy context
- `../governance/audit_procedures.md` - Audit procedures

**Estimated Training Time:** 4 hours

---

### For System Administrators
**Required Reading:**
1. ✅ `../governance/training_materials/admin_technical_guide.md` - Primary guide
2. ✅ `../governance/competence_requirements.md` - Training requirements
3. ✅ `../tests/README.md` - Testing procedures
4. ✅ `../README.md` - System overview

**Optional:**
- `operator_quick_guide.md` - Understanding user perspective
- `../governance/ai_policy.md` - Policy context

**Estimated Training Time:** 8 hours

---

### For AI Governance Leads
**Required Reading:**
1. ✅ `../governance/training_materials/governance_framework.md` - Primary guide
2. ✅ `../governance/ai_policy.md` - Complete policy
3. ✅ `../governance/audit_procedures.md` - Audit framework
4. ✅ `../governance/competence_requirements.md` - Training framework
5. ✅ `iso42001_compliance_mapping.md` - ISO/IEC 42001:2023 compliance mapping

**Optional:**
- `PORTFOLIO.md` - Project presentation context

**Estimated Training Time:** 16 hours

---

## 📚 Additional Resources

### Governance Documentation
- **Location:** `../governance/`
- **Index:** `../governance/README.md`
- **Key Documents:**
  - AI Policy Statement
  - Audit Procedures
  - Competence Requirements
  - Roles and Responsibilities

### Technical Documentation
- **Main README:** `../README.md`
- **Testing:** `../tests/README.md`
- **Tools:** `../tools/README.md`

### External References
- **ISO/IEC 42001:2023:** https://www.iso.org/standard/81230.html
- **Google Gemini API:** https://ai.google.dev/
- **NIST AI RMF:** https://www.nist.gov/itl/ai-risk-management-framework

---

## 📞 Contact

**Questions about documentation?**
- **System Owner:** William Ryan Micou
- **Training Coordinator:** [TBD]

**For documentation updates:**
- Create an issue in the GitHub repository
- Follow change management procedures in `../governance/roles_and_responsibilities.md`

---

## 🔄 Documentation Maintenance

### Review Schedule
- **Operator Quick Guide:** Annual review (next: 2026-11-25)
- **Portfolio Document:** Update after major milestones
- **ISO/IEC 42001:2023 Mapping:** Update when compliance requirements change
- **This Index:** Update when new documents added

### Version Control
- All documentation is version-controlled via Git
- Major updates increment version number
- Document history tracked in each file
- Changes require System Owner approval

---

## ✅ ISO/IEC 42001:2023 Compliance

**Clause 7.2 (Competence):**
- ✅ Training materials documented for all roles
- ✅ Competence requirements defined
- ✅ Assessment criteria established

**Clause 7.5 (Documented Information):**
- ✅ Documentation indexed and accessible
- ✅ Version control implemented
- ✅ Review schedule defined

---

**Document Version:** 1.1 | Created: 2025-11-29 | Updated: 2025-12-07
