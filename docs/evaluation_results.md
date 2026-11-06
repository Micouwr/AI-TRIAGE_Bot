# Classification Evaluation Results

**Date:** 2026-11-01
**Model:** gemini-3.8-flash (temperature 0.1)
**Tickets:** 26, labeled by the author (see `docs/eval_tickets.json`)

## Why this model

The pin was upgraded to gemini-3.8-flash, the current generally-available
flash model on the free tier. The prompt template, ticket categories,
confidence threshold, PII detection, and routing rules are the repo's own,
unchanged.

## Summary

| Metric | Result |
|---|---|
| Tickets evaluated | 26 of 26 |
| Classification accuracy | 23 of 26 (88.5%) |
| PII detection recall | 6 of 6 (100%) |
| Escalated to human review | 10 of 26 (38.5%) |

All 26 tickets produced a model answer. There were no unresolved tickets in
this run; the two rate-limited tickets from the 2026-10-31 run (ids 20 and 24)
were evaluated this time.

## Per-ticket results

| ID | Expected | Predicted | Confidence | PII flagged | Route | Correct |
|---|---|---|---|---|---|---|
| 1 | password_reset | password_reset | 1.00 | no | automated_response | yes |
| 2 | password_reset | password_reset | 0.99 | no | automated_response | yes |
| 3 | password_reset | password_reset | 0.99 | yes | human_agent | yes |
| 4 | password_reset | password_reset | 0.98 | no | automated_response | yes |
| 5 | access_request | access_request | 0.99 | no | automated_response | yes |
| 6 | access_request | access_request | 0.98 | no | automated_response | yes |
| 7 | access_request | access_request | 0.99 | no | automated_response | yes |
| 8 | software_issue | software_issue | 0.98 | no | automated_response | yes |
| 9 | software_issue | software_issue | 0.98 | no | automated_response | yes |
| 10 | software_issue | software_issue | 0.98 | no | automated_response | yes |
| 11 | software_issue | software_issue | 0.96 | no | automated_response | yes |
| 12 | hardware_issue | hardware_issue | 0.98 | no | automated_response | yes |
| 13 | hardware_issue | hardware_issue | 0.98 | no | automated_response | yes |
| 14 | hardware_issue | hardware_issue | 0.95 | no | automated_response | yes |
| 15 | billing_question | billing_question | 0.99 | no | automated_response | yes |
| 16 | billing_question | billing_question | 0.99 | no | automated_response | yes |
| 17 | billing_question | billing_question | 0.98 | no | automated_response | yes |
| 18 | billing_question | billing_question | 0.98 | yes | human_agent | yes |
| 19 | compliance_flag | compliance_flag | 0.95 | yes | human_agent | yes |
| 20 | compliance_flag | compliance_flag | 0.95 | no | human_agent | yes |
| 21 | compliance_flag | compliance_flag | 0.98 | no | human_agent | yes |
| 22 | unknown | unknown | 0.95 | no | human_agent | yes |
| 23 | unknown | unknown | 0.95 | no | human_agent | yes |
| 24 | access_request | unknown | 0.95 | yes | human_agent | no |
| 25 | access_request | compliance_flag | 0.95 | yes | human_agent | no |
| 26 | billing_question | compliance_flag | 0.95 | yes | human_agent | no |

## Findings

**The classifier is accurate on clear tickets.** 23 of the 26 tickets were
classified correctly (password resets, access requests, software/hardware
issues, billing questions, and the correctly flagged compliance cases,
including 3 that contained PII), most at 0.95 confidence or above.

**PII handling works end to end.** All 6 PII-containing tickets were flagged,
all 6 were routed to human review, and redaction keeps raw values out of the
log.

**The unknown-to-human escalation rule is fixed and working.** Tickets 22 and
23 were vague ("The thing is broken again, please fix ASAP"). In the previous
run they routed to automated_response because no rule covered a confident
`unknown`. The rule added 2026-10-31 (`if ticket_type == unknown: escalate_to:
human_agent`) was already in effect during this run, and both tickets now route
to human review, as measured in the table above.

**The three misses are all PII-heavy tickets.** Ticket 25 ("I can't access my
account, my SSN is 123-45-6789, please verify me") was labeled access_request
but the model returned compliance_flag, repeating the same reading as the
previous run. Ticket 26, a billing question containing account identifiers,
also came back compliance_flag. Ticket 24, an access request with PII, came
back `unknown`. The pattern: when a ticket carries sensitive identifiers, the
model leans toward compliance_flag or gives up with unknown. Every one of
these still went to human review, which is the safe outcome, but the category
labels were wrong. The compliance_flag definition in the prompt may need
tightening to distinguish genuine compliance matters from PII-carrying service
requests.

**All three misses still got the safe routing.** The misses cost accuracy, not
safety: each one hit an escalation rule (PII flag, compliance_flag, or
unknown) and went to a human.

## Limitations

- Ground-truth labels were assigned by the author, not by independent labelers.
  Treat this as a first measurement, not a benchmark.
- Results reflect gemini-3.8-flash, not the retired gemini-2.5-flash.
- 26 tickets is a small sample; it covers the main categories but not the full
  variety of real support traffic.
- PII-heavy tickets are the weak spot (3 of 6 misclassified by category).
  They are all escalated to a human, so the failure mode is conservative.
