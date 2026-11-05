---
id: concept.BR-LOS-205
type: concept
title: The account is checked again just before payment and a bad account stops it
summary: "Account validation is run again immediately before disbursement, and a dormant, closed or otherwise ineligible account halts disbursement and raises an exception."
br_ids: [BR-LOS-205]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [bridge.BR-LOS-205, concept.BR-LOS-203]
version: 1
status: approved
approved_by: Owner
---
**In short:** Account validation is run again immediately before disbursement, and a dormant, closed or otherwise ineligible account halts disbursement and raises an exception.

## What the rule says

BR-LOS-205 (Must, BRD 6.9, PDF page 43) says "Account validation shall be re-executed immediately before disbursement." "A dormant, closed or otherwise ineligible account shall halt disbursement and raise an exception." So the check is repeated at the last moment, and three kinds of account named by the BRD stop the payment.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an account can change between the first check and the payment, so the bank checks again just before money moves.

## Example

An account passed validation earlier in the process. Just before disbursement the validation runs again and finds the account dormant. Disbursement stops and an exception is raised.

## Terms to know

- **Re-executed:** the BRD's word for validation being run again just before disbursement.
- **Dormant:** an account state the BRD names; it does not define it.
