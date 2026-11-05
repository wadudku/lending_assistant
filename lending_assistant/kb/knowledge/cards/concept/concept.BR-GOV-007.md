---
id: concept.BR-GOV-007
type: concept
title: "When an outside system is down, the step pauses and retries"
summary: "If an outside system is unavailable, the affected step pauses with a clear message and retries by itself, and the platform never fails an application, corrupts a loan or invents a decision."
br_ids: [BR-GOV-007]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-007"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-GOV-007, concept.BR-GOV-003]
version: 1
status: approved
approved_by: Owner
---
**In short:** If an outside system is unavailable, the affected step pauses with a clear message and retries by itself, and the platform never fails an application, corrupts a loan or invents a decision.

## What the rule says

BR-GOV-007 (Must, BRD 3.4, PDF page 19) says the platform degrades gracefully. When any external system is unavailable, the affected step pauses with clear user messaging and automatic retry. It never fails an application, corrupts a loan's state, or produces a decision the external system did not give.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a short outage at a bureau or the core system should not cost the bank an applicant or leave a loan half-updated.

## Example

The credit bureau is down when an application is checked. The application shows “waiting for the bureau”, the check is retried later by itself, and the bureau's real answer decides the case. The system never approves or rejects on its own guess.

## Terms to know

- **Degrade gracefully:** keep working in a reduced way when a part fails, instead of stopping.
- **Pause:** hold a step until the outside system is back.
- **Automatic retry:** trying again without a person asking.
- **State of a loan:** the recorded status and figures of a loan.
