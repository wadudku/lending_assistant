---
id: concept.BR-LMS-011
type: concept
title: Sending the same handoff twice never creates a second loan
summary: A repeated handoff for the same origination reference returns the original loan and never creates a second one.
br_ids: [BR-LMS-011]
brd_section: 5.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-011"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
related: [bridge.BR-LMS-011, glossary.idempotency, concept.BR-GOV-002, concept.BR-LMS-010]
version: 1
status: approved
approved_by: Owner
---
**In short:** A repeated handoff for the same origination reference returns the original loan and never creates a second one.

## What the rule says

BR-LMS-011 (Must, BRD 5.4, PDF page 28) says the handoff is idempotent. A repeated handoff of the same origination reference returns the original booked loan and never creates a second loan record.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a handoff can be sent again after a network failure, and without this rule one payout would become two loans.

## Example

The origination system sends the handoff for reference ORG-1001 and the reply is lost, so it sends it again. Servicing returns the loan it already created for ORG-1001 and creates nothing new.

## Terms to know

- **Idempotent:** doing it twice has the same result as doing it once. See `glossary.idempotency`.
- **Origination reference:** the unique number the origination system gives a loan case.
- **Booked loan:** a loan already created in servicing.
