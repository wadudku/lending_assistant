---
id: bridge.BR-LMS-104
type: bridge
title: Track the approved limit separately from what was taken
summary: "Covered. The loan keeps the sanctioned Loan Amount apart from the Disbursed Amount, and credit lines also show maximum, used and available limit."
br_ids: [BR-LMS-104]
brd_section: 7.1
doctypes: [Loan]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan.Loan Amount, Loan.Disbursed Amount, Loan.Maximum Limit Amount, Loan.Utilized Limit Amount, Loan.Available Limit Amount]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.json:187", "lending/loan_management/doctype/loan/loan.json:579"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-104"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-104"
  - "sources/verification/verification_report.md#BR-LMS-104"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-104"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-104"
related: [concept.BR-LMS-104, brd_section.7.1, glossary.loc, lifecycle.PARTIALLY_DISBURSED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The loan keeps the sanctioned Loan Amount apart from the Disbursed Amount, and credit lines also show maximum, used and available limit.

## Business need

Where the approved limit differs from the amount funded, the bank wants the limit reference kept and the use of it tracked (BR-LMS-104, BRD 7.1, PDF page 46). See `concept.BR-LMS-104`.

## Frappe Lending today

The **Loan** holds **Loan Amount** (the sanctioned amount, `loan.json` line 187) and **Disbursed Amount** (`loan.json` line 352) as separate fields. For lines of credit it also holds **Maximum Limit Amount** (`loan.json` line 579), **Utilized Limit Amount** (`loan.json` line 603) and **Available Limit Amount** (`loan.json` line 595). The last two are read-only.

## Match or gap, and why

This is **covered**. In the test, a tranche loan showed a Loan Amount of 80,000 against a Disbursed Amount of 40,000 after the first tranche (verification_report.md:90). The three limit fields exist on the Loan (verification checked the fields, not a credit-line run). The coverage analysis rated this row covered, and verification confirmed it.

## What to do today

For a term loan read the sanctioned amount from **Loan Amount** and the paid-out amount from **Disbursed Amount**. For a line of credit read the three limit fields.

## Planned fix

Nothing is needed.
