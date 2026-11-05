---
id: concept.BR-LOS-202
type: concept
title: The account is confirmed and saved before any disbursement is tried
summary: Account opening must be confirmed and persisted before disbursement is attempted.
br_ids: [BR-LOS-202]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-202"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [bridge.BR-LOS-202, concept.BR-LOS-201, concept.BR-LOS-203]
version: 1
status: approved
approved_by: Owner
---
**In short:** Account opening must be confirmed and persisted before disbursement is attempted.

## What the rule says

BR-LOS-202 (Must, BRD 6.9, PDF page 43) says "Account opening shall be confirmed and persisted before disbursement is attempted." So disbursement does not start until the account opening is both confirmed and saved.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a payment cannot safely be sent to an account whose existence is not yet certain. The BRD's context for 6.9 on PDF page 43 is that "the controlling risk is duplicate disbursement arising from an uncertain response to an instruction that has in fact already executed".

## Example

The platform asks the core banking system to open a loan account. Only after the opening is confirmed and saved does the platform try to disburse.

## Terms to know

- **Persisted:** the BRD's word, used with confirmed; it does not define it.
- **Confirmed:** the BRD's word; BR-INT-003 (BRD 9.2.1) says the platform reads back and keeps the loan account number the core banking system shows.
