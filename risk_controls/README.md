# Risk Controls Documentation

This directory contains scripts and documentation related to the risk management and governance controls implemented in the AI Triage Bot Prototype. These controls ensure compliance with ISO/IEC 42001 standards, particularly focusing on accountability, risk management, and auditability.

## Contents

- **escalation_protocols.md**: Outlines escalation procedures for unresolved fallback events, system errors, and governance threshold breaches.
- **fallback_protocols.md**: Describes fallback handling procedures for low-confidence classifications, escalation failures, and malformed LLM outputs.
- **pii_filters.py**: A script to detect Personally Identifiable Information (PII) in support tickets.

## Purpose

The documents and scripts in this directory are designed to:
- Ensure the AI Triage Bot operates within defined risk parameters.
- Enable traceability and accountability in case of system failures or governance breaches.
- Support compliance with relevant ISO/IEC 42001 clauses.

## Usage

To use the risk controls:
1. Review the escalation and fallback protocols to understand the conditions under which they are triggered.
2. Use the `pii_filters.py` script to detect sensitive data in tickets.
3. Ensure that all governance and risk management activities are documented and aligned with the protocols outlined in this directory.

## How to Contribute

When updating risk controls:
- Ensure changes align with the bot's governance requirements and ISO/IEC 42001 standards.
- Update the relevant documentation to reflect new controls or changes in existing controls.
- Document any changes in the `version_history.md` file to maintain an audit trail.

## Review Schedule

- **Monthly**: Review and update risk controls and escalation protocols.
- **Quarterly**: Conduct a comprehensive audit of the risk management framework.

## Contact

For questions or to report issues with the risk controls documentation, contact William Micou at micouwr@gmail.com.
