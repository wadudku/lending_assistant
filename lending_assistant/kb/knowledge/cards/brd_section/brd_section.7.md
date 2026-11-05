---
id: brd_section.7
type: brd_section
title: BRD 7 Business requirements — Loan Management System
summary: "Section 7 is the BRD's overview of the Loan Management System: what it runs after payout and the one constraint that governs all of it."
br_ids: []
brd_section: "7"
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
related: [brd_section.7.7, glossary.lms, glossary.cbs, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7 is the BRD's overview of the Loan Management System: what it runs after payout and the one constraint that governs all of it.

## What this section says

BRD 7 (PDF page 46) opens the Loan Management System part of the BRD. It says the LMS manages the bank's loan book after disbursement. The list covers repayment schedules, demands, interest accrual, repayments and their allocation, collateral, repricing and restructuring, delinquency, asset classification, provisions, recovery and write-off, statements and reports, and closing the loan. It holds 14 numbered sub-sections, 7.1 to 7.14, and Section 7.7 has two parts, 7.7.1 and 7.7.2.

## Why the bank wants it

The BRD gives its reason on the same page (PDF page 46): the loan book must be correct, explicable and reproducible. Every balance must trace to a posting, every posting to an approved event, and every approved event to an authorised actor and a rule version.

## How it meets Frappe Lending

The verified results are in the cards for each sub-section. Across all 103 Section 7 requirement rows the verified totals on 16.5.1 are: 31 covered, 49 partly covered, 18 gaps and 5 gaps that need the CBS link.

## Related cards

Sub-section cards: `brd_section.7.1` to `brd_section.7.14`, with `brd_section.7.7.1` and `brd_section.7.7.2` under 7.7 (`brd_section.7.7`). Terms: `glossary.lms`, `glossary.cbs`, `glossary.maker-checker`. The `glossary.maker-checker` card explains the two-user rule used throughout.
