# Fallback Protocols

## Trigger Conditions
Fallback protocols activate when:
- confidence_score < 0.5
- escalation fails or times out
- ticket_type is "unknown"
- LLM output is malformed or missing required fields

## Actions
1. Route ticket to human agent with fallback flag
2. Log incident in fallback_log.json
3. Notify governance team if fallback rate exceeds 5% in a 24-hour window

## Audit Notes
- All fallback events must be timestamped and retained for 90 days
- Fallback triggers are reviewed weekly by the AI oversight team
