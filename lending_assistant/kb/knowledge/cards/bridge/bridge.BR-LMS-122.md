---
id: bridge.BR-LMS-122
type: bridge
title: Rebuild the plan when money is paid out in parts
summary: "Covered. Each confirmed tranche creates a new schedule, and the earlier one is set to Outdated."
br_ids: [BR-LMS-122]
brd_section: 7.3
doctypes: [Loan Disbursement, Loan Repayment Schedule]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:190", "lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:307"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-122"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-122"
  - "sources/verification/verification_report.md#BR-LMS-122"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-122"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-122"
related: [concept.BR-LMS-122, brd_section.7.3, lifecycle.PARTIALLY_DISBURSED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. Each confirmed tranche creates a new schedule, and the earlier one is set to Outdated.

## Business need

The bank wants the repayment plan rebuilt or adjusted on each confirmed drawdown of a tranche loan (BR-LMS-122, BRD 7.3, PDF page 48). See `concept.BR-LMS-122`.

## Frappe Lending today

Each **Loan Disbursement** of a term loan has its own **Loan Repayment Schedule** and a tranche number (`loan_disbursement.py` line 190). After a disbursement, the schedule that belongs to the latest tranche becomes Active and the earlier ones become Outdated (`loan_disbursement.py` lines 292-308). The loan status moves to Partially Disbursed until the full amount is drawn; see `lifecycle.PARTIALLY_DISBURSED`.

## Match or gap, and why

This is **covered**. In the test, tranche 1 (40,000 of 80,000) left the loan Partially Disbursed with a schedule. Tranche 2 made the loan Disbursed, created a new Active schedule and set the old one to Outdated (verification_report.md:98). The coverage analysis rated this row covered, and verification confirmed it. The "approved tranche rules" of the BRD are not a separate setting in Frappe Lending; the new schedule is built from the loan's state at the drawdown.

## What to do today

Submit each tranche as its own Loan Disbursement. Read the live plan from the schedule whose status is Active.

## Planned fix

Nothing is needed.
