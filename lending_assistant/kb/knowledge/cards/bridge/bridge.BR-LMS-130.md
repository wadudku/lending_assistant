---
id: bridge.BR-LMS-130
type: bridge
title: Raise the bills on their due dates
summary: Covered. A daily Process Loan Demand run raises demands of six types on their due dates.
br_ids: [BR-LMS-130]
brd_section: 7.4
doctypes: [Loan Demand, Process Loan Demand]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Demand.Demand Type]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_demand/loan_demand.json:69", "lending/loan_management/doctype/process_loan_demand/process_loan_demand.py:48", "lending/hooks.py:189"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-130"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-130"
  - "sources/verification/verification_report.md#BR-LMS-130"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-130"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-130"
related: [concept.BR-LMS-130, brd_section.7.4, glossary.demand, glossary.bpi]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A daily Process Loan Demand run raises demands of six types on their due dates.

## Business need

The bank wants demands raised on their due dates for the instalment and its components (BR-LMS-130, BRD 7.4, PDF page 48). See `concept.BR-LMS-130`.

## Frappe Lending today

A **Loan Demand** has a type: EMI, Penalty, Normal, Charges, BPI or Additional Interest (`loan_demand.json` line 69). The daily job `process_daily_loan_demands` creates a **Process Loan Demand** and submits it (`process_loan_demand.py` lines 48-54; scheduled in `hooks.py` line 189). The code that raises term-loan demands is `make_loan_demand_for_term_loans` (`loan_demand.py` line 252).

## Match or gap, and why

This is **covered**. In the test, a run on a due date billed the interest of 632.87 and the principal of 3,914.66 with the demand date equal to the due date (verification_report.md:187). Overdue penalty is billed as daily "Additional Interest" demands starting on the first day after the due date, and the grace days do not delay it. The coverage analysis rated this row covered, and verification confirmed it. Whether the penalty amount is calculated correctly is a separate question (BR-LMS-141).

## What to do today

Let the daily job run, or run **Process Loan Demand** for a date and a loan to check the bills for that day.

## Planned fix

Nothing is needed for the timing of the demands.
