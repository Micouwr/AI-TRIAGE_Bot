# Validation Scripts

Purpose: Sanitize and validate raw inputs to reduce risk and enforce structure.

## ISO/IEC 42001 Alignment
- Clause 6 (Risk Management): Detects and redacts PII
- Clause 8 (Auditability): Logs sanitization events with counts

## Audit Notes
- Regex patterns for phone numbers and emails
- Redactions logged with counts and flags
- Retention: 90 days minimum