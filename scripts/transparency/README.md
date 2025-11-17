# Transparency Scripts

Purpose: Capture decision rationale, confidence, and governance controls applied to ensure the AI Triage Bot Prototype operates transparently and in alignment with governance standards.

## ISO/IEC 42001 Alignment
- **Clause 5 (Accountability)**: Documents the rationale for each decision made by the bot.
- **Clause 8 (Auditability)**: Provides structured trace logs for audit purposes.

## Audit Notes
- Logs are written to `governance/decision_trace.jsonl`.
- Input summaries must be sanitized to prevent exposure of raw Personally Identifiable Information (PII).
- Reviewed weekly by the governance team to ensure compliance with standards.

These scripts are crucial for maintaining transparency and accountability in the AI Triage Bot's decision-making process.
