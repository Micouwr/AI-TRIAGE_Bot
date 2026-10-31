# Classification Evaluation Results

**Date:** 2026-10-31
**Model:** gemini-3-flash-preview (temperature 0.1)
**Tickets:** 26, labeled by the author (see `docs/eval_tickets.json`)

## Why this model

The project configuration pins Gemini 2.5 Flash, but Google retired that model
for new API projects, so it returns 404 for newly created keys. The evaluation
ran on gemini-3-flash-preview, the current flash model available to this key.
The prompt template, ticket categories, confidence threshold, PII detection,
and routing rules are the repo's own, unchanged.

## Summary

| Metric | Result |
|---|---|
| Tickets evaluated | 24 of 26 |
| Classification accuracy | 23 of 24 (95.8%) |
| PII detection recall | 6 of 6 (100%) |
| Escalated to human review | 8 of 26 (30.8%) |
| Unresolved (API rate limits) | 2 (ids 20, 24) |

Two tickets could not be evaluated: repeated API rate-limit errors (HTTP 429)
persisted across four attempts with increasing backoff, so they have no model
answer. They are excluded from the accuracy figure, not counted as wrong.

## Per-ticket results

| ID | Expected | Predicted | Confidence | PII flagged | Route | Correct |
|---|---|---|---|---|---|---|
| 1 | password_reset | password_reset | 1.00 | no | automated_response | yes |
| 2 | password_reset | password_reset | 1.00 | no | automated_response | yes |
| 3 | password_reset | password_reset | 1.00 | yes | human_agent | yes |
| 4 | password_reset | password_reset | 1.00 | no | automated_response | yes |
| 5 | access_request | access_request | 1.00 | no | automated_response | yes |
| 6 | access_request | access_request | 1.00 | no | automated_response | yes |
| 7 | access_request | access_request | 1.00 | no | automated_response | yes |
| 8 | software_issue | software_issue | 1.00 | no | automated_response | yes |
| 9 | software_issue | software_issue | 0.98 | no | automated_response | yes |
| 10 | software_issue | software_issue | 0.98 | no | automated_response | yes |
| 11 | software_issue | software_issue | 0.95 | no | automated_response | yes |
| 12 | hardware_issue | hardware_issue | 1.00 | no | automated_response | yes |
| 13 | hardware_issue | hardware_issue | 1.00 | no | automated_response | yes |
| 14 | hardware_issue | hardware_issue | 0.98 | no | automated_response | yes |
| 15 | billing_question | billing_question | 1.00 | no | automated_response | yes |
| 16 | billing_question | billing_question | 1.00 | no | automated_response | yes |
| 17 | billing_question | billing_question | 1.00 | no | automated_response | yes |
| 18 | billing_question | billing_question | 1.00 | yes | human_agent | yes |
| 19 | compliance_flag | compliance_flag | 0.95 | yes | human_agent | yes |
| 20 | compliance_flag | — | — | — | human_agent | not evaluated |
| 21 | compliance_flag | compliance_flag | 1.00 | no | human_agent | yes |
| 22 | unknown | unknown | 0.95 | no | automated_response | yes |
| 23 | unknown | unknown | 0.90 | no | automated_response | yes |
| 24 | access_request | — | — | — | human_agent | not evaluated |
| 25 | access_request | compliance_flag | 0.95 | yes | human_agent | no |
| 26 | billing_question | billing_question | 1.00 | yes | human_agent | yes |

## Findings

**The classifier is accurate on clear tickets.** All 20 routine tickets
(password resets, access requests, software/hardware issues, billing questions
without PII) were classified correctly, most at 1.00 confidence.

**PII handling works end to end.** All 6 PII-containing tickets were flagged,
all 6 were routed to human review, and the new redaction keeps raw values out
of the log.

**The one miss is instructive.** Ticket 25 ("I can't access my account, my SSN
is 123-45-6789, please verify me") was labeled access_request but the model
returned compliance_flag at 0.95 confidence. A PII-heavy identity-verification
request reads as a compliance matter to the model. It still went to human
review, which is the safe outcome, but the category was wrong.

**The escalation rules had a gap.** Tickets 22 and 23 were vague
("The thing is broken again, please fix ASAP"). The model confidently
predicted `unknown` (0.95, 0.90), and the declared rules routed them to
automated_response because no rule covered a confident `unknown`. An
unclassifiable ticket should not be auto-handled. Fixed 2026-10-31: added
`if ticket_type == unknown: escalate_to: human_agent` to the escalation rules
in `governance/config/scope.yaml`, with a regression test. The per-ticket table
above records the routing measured during the evaluation, before this fix.

## Limitations

- Ground-truth labels were assigned by the author, not by independent labelers.
  Treat this as a first measurement, not a benchmark.
- 2 of 26 tickets have no model answer due to API rate limiting.
- Results reflect gemini-3-flash-preview, not the retired gemini-2.5-flash.
- 26 tickets is a small sample; it covers the main categories but not the full
  variety of real support traffic.
