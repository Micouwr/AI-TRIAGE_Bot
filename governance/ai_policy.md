# AI Policy Statement - Vigil

**Document Status:** DRAFT - SIGNATURES PENDING
**Operational Status:** FRAMEWORK
**Document Version:** 1.3
**Effective Date:** 2025-11-25  
**Owner:** William Ryan Micou  
**Review Cycle:** Annual  

---

## 1. Purpose and Scope

This AI Policy establishes the governance framework for the Vigil, an LLM-powered support ticket classification system. This policy defines accountability, risk management, and operational controls in alignment with ISO/IEC 42001:2023.

### 1.1 System Scope
- **System Name:** Vigil
- **Primary Function:** Automated classification of Tier 1 support tickets
- **AI Model:** Gemini 3.8 Flash (Google Generative AI)
- **Deployment Target:** Desktop application (Windows/Mac/Linux)
- **Current Status:** Framework implementation, not in production use

---

## 2. Governance Principles

### 2.1 Human Oversight
- All classifications below 70% confidence are flagged for human review
- Human agents retain final decision authority on all escalations
- System operates as an assistive tool, not autonomous decision-maker

### 2.2 Transparency
- Classification logic is auditable through configuration files
- All decisions are logged with timestamps and confidence scores
- Model responses are traceable to specific prompts

### 2.3 Fairness and Non-Discrimination
- Classification criteria are based solely on ticket content
- No demographic or user identity factors influence routing
- Regular audits ensure no systematic bias in classifications

### 2.4 Privacy and Data Protection
- PII detection mechanisms flag sensitive information
- Tickets containing PII are escalated to human agents
- No training data is collected from production tickets
- API keys are stored securely via environment variables

---

## 3. Risk Management

### 3.1 Identified Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Incorrect ticket routing | Medium | Confidence thresholds, fallback logging |
| PII exposure | High | Automated PII detection, escalation protocols |
| Model unavailability | Medium | Graceful degradation, error logging |
| Bias in classification | Low | Regular audit of fallback logs |
| API rate limiting | Low | Free tier awareness (low per-project limits; check quota in AI Studio), error handling |

### 3.2 Escalation Protocols
Automatic escalation to human agents when:
- Confidence score < 0.7
- PII detected in ticket text
- Category = "compliance_flag"
- LLM returns malformed response
- API rate limit exceeded

---

## 4. Roles and Responsibilities

### 4.1 AI Governance Lead
- **Responsibility:** Overall system accountability
- **Activities:** Monthly review of fallback logs, annual policy review
- **Contact:** William Ryan Micou

### 4.2 System Operators
- **Responsibility:** Daily operation of the classification system
- **Training Required:** Understanding of confidence thresholds, PII handling
- **Escalation Path:** AI Governance Lead for system failures

### 4.3 Human Review Agents
- **Responsibility:** Review flagged tickets from fallback log
- **Training Required:** Ticket classification criteria, PII protocols
- **SLA:** Review within 24 hours of flagging

---

## 5. Monitoring and Continuous Improvement

### 5.1 Performance Metrics
- **Accuracy:** Measured via human review of random sample (monthly)
- **Confidence Distribution:** Monitored via fallback logs
- **PII Detection Rate:** False positive/negative analysis (quarterly)

### 5.2 Audit Schedule
- **Internal Audits:** Quarterly review of logs and configurations
- **External Audits:** Annual third-party ISO/IEC 42001:2023 assessment
- **Incident Reviews:** Within 48 hours of any system failure

### 5.3 Improvement Process
1. Identify issues through monitoring or audits
2. Document in `lifecycle/version_history.md`
3. Implement fixes with test coverage
4. Deploy with rollback capability
5. Verify improvement through metrics

### 5.4 AI Objectives
The following measurable objectives apply to the Vigil system in ongoing operation. They were set from the 26-ticket evaluation baseline measured 2026-11-01 (88.5% classification accuracy, 100% PII recall) and are reviewed at each new evaluation and at the annual policy review.
- Classification accuracy at or above 85%
- PII recall at or above 95% (fewer than 5% PII false negatives)
- Every classification miss routed to human review

---

## 6. Compliance References

### 6.1 Standards Alignment
- ISO/IEC 42001:2023 - AI Management Systems
- NIST AI Risk Management Framework
- GDPR Article 22 (Automated Decision-Making)

### 6.2 Documentation
- `docs/iso42001_compliance_mapping.md` - Detailed clause mapping
- `governance/config/scope.yaml` - System configuration
- `risk_controls/fallback_protocols.md` - Escalation procedures

---

## 7. Policy Review and Updates

This policy will be reviewed annually or when:
- Significant system changes are implemented
- New regulatory requirements emerge
- Audit findings require policy updates
- Stakeholder feedback indicates gaps

**Next Review Date:** 2026-11-25

---

**Approval:**

Signatures are pending; the policy content is in use as a working draft until signed.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| System Owner | William Ryan Micou | [To Be Signed] | 2025-11-25 |
| Compliance Officer | [TBD] | [To Be Signed] | [TBD] |

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-25 | W.R. Micou | Initial policy creation |
| 1.1 | 2025-11-25 | W.R. Micou | Updated model to Gemini 2.5 Flash, added rate limiting risk |
| 1.2 | 2026-11-06 | W.R. Micou | Corrected human-review threshold to 70%, corrected free-tier limit wording, fixed compliance mapping path, marked approval signatures pending |
| 1.3 | 2026-11-06 | W.R. Micou | Added AI objectives in Section 5.4 (accuracy, PII recall, miss routing targets set from the evaluation baseline) |

