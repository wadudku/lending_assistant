---
id: concept.BR-LMS-010
type: concept
title: "Servicing accepts only a complete, confirmed handoff; others go to an exception queue"
summary: Servicing takes a loan only when the handoff is complete and carries a confirmed payout reference; any other handoff is rejected to an exception queue with a reason and creates no loan.
br_ids: [BR-LMS-010]
brd_section: 5.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-011"
related: [bridge.BR-LMS-010, glossary.lms, concept.BR-LOS-010, concept.BR-LMS-011]
version: 1
status: approved
approved_by: Owner
---
**In short:** Servicing takes a loan only when the handoff is complete and carries a confirmed payout reference; any other handoff is rejected to an exception queue with a reason and creates no loan.

## What the rule says

BR-LMS-010 (Must, BRD 5.4, PDF page 28) says the LMS accepts a loan into servicing only where the handoff package is complete and carries a confirmed disbursement reference. An incomplete or unconfirmed handoff is rejected into an exception queue with a stated reason and does not create a loan.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a loan booked from half the data would carry errors for its whole life, and a payout that is not confirmed may not have happened.

## Example

A handoff arrives without a payout reference. Servicing creates no loan. The handoff goes to an exception queue with the reason “disbursement reference missing”, and someone must fix the cause and send it again.

## Terms to know

- **Exception queue:** a list of rejected items waiting for a person to resolve them.
- **Confirmed disbursement reference:** a payout number that the bank's core system has confirmed.
- **Complete package:** one that holds every item BR-LOS-010 lists.
