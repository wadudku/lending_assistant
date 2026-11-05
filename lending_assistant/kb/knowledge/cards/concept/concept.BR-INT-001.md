---
id: concept.BR-INT-001
type: concept
title: Look up an account in the core banking system
summary: "The platform obtains an account's existence, status, product type, title, CIF reference and KYC currency from the core banking system."
br_ids: [BR-INT-001]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [bridge.BR-INT-001, glossary.cbs, glossary.cif, brd_section.6.3]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform obtains an account's existence, status, product type, title, CIF reference and KYC currency from the core banking system.

## What the rule says

BR-INT-001 (Must, BRD 9.2.1, PDF page 61) says that for a given account number the platform obtains six things: whether the account exists, its status, product type, account title, CIF reference and KYC currency. The BRD adds that this must be enough to satisfy the validation rules in Section 6.3.

## Why the bank wants it

The BRD gives the reason in the row: the six items must be “sufficient to satisfy the validation rules in Section 6.3” (PDF page 61).

## Example

A partner submits a payout account number. The platform asks the core banking system about it and gets back: the account exists, it is open, it is a savings product, the title is the borrower's name, it has a customer reference, and the identity check on it is current. The platform can then decide whether the account is acceptable.

## Terms to know

- **CBS:** the bank's main system. See `glossary.cbs`.
- **Account title:** the name the account is held in.
- **CIF reference:** the number of the customer record in the core banking system.
- **KYC currency:** whether the know-your-customer identity check on the customer is up to date.
