---
id: concept.BR-INT-070
type: concept
title: A manual fallback for every automated transaction
summary: "Every automated transaction has a manual fallback: authorised bank staff can do it directly in the core banking system and record its reference, so a long outage does not halt lending."
br_ids: [BR-INT-070]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-070"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-070, glossary.cbs, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every automated transaction has a manual fallback: authorised bank staff can do it directly in the core banking system and record its reference, so a long outage does not halt lending.

## What the rule says

BR-INT-070 (Must, BRD 9.3, PDF page 63) says a manual fallback exists for every automated transaction. Authorised bank staff can perform the transaction directly in the core banking system and record its reference against the application or loan.

## Why the bank wants it

The BRD gives the reason in the row: “so that a prolonged automation outage does not halt lending” (PDF page 63).

## Example

The automation is down for a day. A trained officer opens the payout in the core banking system by hand, notes the transaction reference, and enters it against the loan in the platform. Lending carries on.

## Terms to know

- **Fallback:** a second way to do the same job when the first fails.
- **Authorised staff:** people the bank has allowed to do the transaction.
