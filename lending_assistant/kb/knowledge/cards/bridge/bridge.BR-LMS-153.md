---
id: bridge.BR-LMS-153
type: bridge
title: Two repricing options
summary: "Partly covered. Both options exist on a single Loan Restructure, but only for one loan at a time, and the default term is the original term."
br_ids: [BR-LMS-153]
brd_section: 7.6
doctypes: [Loan Restructure]
verdict: partial
analysis_status: verified
dev_items: [D11]
fields: [Loan Restructure.New Repayment Method]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.json:156"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-153"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-153"
  - "sources/verification/verification_report.md#BR-LMS-153"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-153"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-153"
related: [concept.BR-LMS-153, brd_section.7.6, devitem.D11, glossary.emi]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Both options exist on a single Loan Restructure, but only for one loan at a time, and the default term is the original term.

## Business need

The bank wants repricing to offer a fixed-maturity mode and a fixed-instalment mode (BR-LMS-153, BRD 7.6, PDF page 49). See `concept.BR-LMS-153`.

## Frappe Lending today

The **Loan Restructure** has a **New Repayment Method** with two options: Repay Fixed Amount per Period and Repay Over Number of Periods (`loan_restructure.json` lines 156-157).

## Match or gap, and why

This is **partly covered**. In the test, both options worked on one loan: repaying over 7 periods gave an EMI of 9,013, and a fixed amount of 8,979 gave 8 rows (verification_report.md, BR-LMS-153, J5). With a rate-only change the default term reset to the original 12 months instead of the remaining term. With the fixed amount, the record and the Loan kept 12 periods while the schedule had 8 rows (DEF-19). The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Set the new term yourself on a rate-only change, and check the schedule length against the record after approval.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch. DEF-19 is logged in the verification report.
