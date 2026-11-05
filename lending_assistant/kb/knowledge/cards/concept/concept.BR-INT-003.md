---
id: concept.BR-INT-003
type: concept
title: Open the loan account in the core banking system and keep its number
summary: "The platform opens a loan account in the core banking system with the borrower reference, product code and sanctioned terms, and keeps the loan account number the system shows."
br_ids: [BR-INT-003]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [bridge.BR-INT-003, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform opens a loan account in the core banking system with the borrower reference, product code and sanctioned terms, and keeps the loan account number the system shows.

## What the rule says

BR-INT-003 (Must, BRD 9.2.1, PDF page 61) says the platform opens a loan account in the Core Banking System. It supplies the borrower reference, the product code and the sanctioned terms. It reads back and retains the loan account number as the core banking system displays it.

## Why the bank wants it

The BRD gives the reason in section 9.2, which says the core banking system has no interface: “There is therefore no transactional interface through which the platform can enquire on an account, open a loan account, disburse funds or post an accounting event.” (PDF page 60) Why the number is read back and kept is not given; the usual reason is that every later instruction needs that number.

## Example

After sanction, the platform opens an account for a borrower with the product code and a 12-month term. The core banking system shows a new account number, such as 5001-77-0042. The platform reads that number off the screen and keeps it against the loan.

## Terms to know

- **The loan's account:** the borrower's account for the loan at the bank, held in the core banking system.
- **Product code:** the core banking system's code for the type of loan.
- **Sanctioned terms:** the amount, rate and tenor the bank approved.
- **Read back:** read the result from the screen after acting.
