---
id: concept.BR-INT-004
type: concept
title: Pay out against the opened account and keep the reference and date
summary: "The platform disburses against an opened loan account to the validated target account, and keeps the transaction reference and value date the core banking system records."
br_ids: [BR-INT-004]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [bridge.BR-INT-004, glossary.cbs, glossary.value-date]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform disburses against an opened loan account to the validated target account, and keeps the transaction reference and value date the core banking system records.

## What the rule says

BR-INT-004 (Must, BRD 9.2.1, PDF page 61) says the platform executes disbursement against an opened loan account, to the validated target account. It reads back and retains the transaction reference and the value date as the core banking system records them.

## Why the bank wants it

The BRD gives the reason in section 9.2, which says the core banking system has no interface: “There is therefore no transactional interface through which the platform can enquire on an account, open a loan account, disburse funds or post an accounting event.” (PDF page 60) Why the reference and value date are kept is not given; the usual reason is that they are what ties the platform's record to the bank's books.

## Example

The platform pays 100,000 into the borrower's checked account. The core banking system records reference TXN-20931 with value date 14 March. The platform keeps both against the loan, so the payout can be found in the bank's books.

## Terms to know

- **Disbursement:** paying the loan amount out to the borrower.
- **Target account:** the account the money goes to.
- **Value date:** the date from which the money counts in the account. See `glossary.value-date`.
- **Transaction reference:** the bank's number for the payment.
