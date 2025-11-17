# Escalation Protocols - AI Triage Bot

This document outlines escalation procedures for unresolved fallback events, system errors, and governance threshold breaches, supporting ISO/IEC 42001 Clauses 5, 6, and 8.

## Escalation Triggers

Escalation is initiated when:
- Fallback rate exceeds 5% in a 24-hour window
- PII detection fails or flags unrecognized patterns
- Classification engine returns `ticket_type == "unknown"` more than 3 times in 1 hour
- Viewer tool fails to parse fallback logs
- Governance scripts detect schema drift or data quality violations

## Escalation Matrix

| Severity | Trigger | Escalation Path | Notification Target | Governance Alignment |
|----------|--------|------------------|--------------------|----------------------|
| Low | Single fallback event | Log only | No notification | Clause 8 |
| Medium | Repeated fallback events or unknown ticket types | Route to human agent, log, notify governance team | Clause 5, Clause 6 |
| High | PII detection failure, schema drift, viewer failure | Log, notify governance team, initiate manual review | AI Oversight Team | Clause 5, Clause 6, Clause 8 |
| Critical | Fallback rate &gt; 5% in 24h, multiple governance script failures | Log, notify governance team, escalate to system owner | William Ryan Micou | Clause 5, Clause 6 |

## Audit Notes

- All escalations are timestamped and retained for 90 days.
- Manual reviews are documented in `governance/escalation_reviews/` (folder to be created).
- Contributors must update this file when new escalation triggers or severity levels are introduced.
