# Roles and Responsibilities — AI-Triage-Bot Governance

This document defines the roles, responsibilities, and authorities required to govern, operate, and maintain the AI-Triage-Bot system in alignment with ISO/IEC 42001:2023.

---

## 🧑‍💼 Governance Roles

### 1. System Owner
- **Name**: William Ryan Micou
- **Responsibilities**:
  - Define system scope and intended use
  - Approve lifecycle changes and decommissioning
  - Ensure compliance with ISO/IEC 42001 clauses

### 2. AI Governance Lead
- **Responsibilities**:
  - Maintain documentation and audit readiness
  - Oversee risk controls and fallback protocols
  - Coordinate with compliance and legal teams

### 3. Prompt Engineer
- **Responsibilities**:
  - Design and version prompts for classification and escalation
  - Monitor LLM behavior and edge cases
  - Ensure transparency and explainability in outputs

### 4. Support Operations Lead
- **Responsibilities**:
  - Define ticket categories and escalation paths
  - Validate bot performance against Tier 1 support metrics
  - Coordinate fallback handoffs to human agents

### 5. Audit & Compliance Officer
- **Responsibilities**:
  - Review logs and lifecycle documentation monthly
  - Conduct internal audits and prepare for external reviews
  - Validate adherence to ISO/IEC 42001 clauses 5.3, 6.1, 8.2, and 8.5

---

## 🔄 Change Management Authority

All changes to bot behavior, classification logic, or governance policies must be:
- Documented in `lifecycle/version_history.md`
- Approved by the System Owner and AI Governance Lead
- Reviewed by the Audit & Compliance Officer

---

## 📅 Review Schedule

- **Monthly**: Audit log review, fallback protocol validation
- **Quarterly**: Prompt performance analysis, risk control updates
- **Annually**: Full ISO/IEC 42001 compliance review

---

## 📌 Reference Documents

- `config/scope.yaml`
- `risk_controls/fallback_protocols.md`
- `lifecycle/version_history.md`
- `docs/iso42001_mapping.md`
