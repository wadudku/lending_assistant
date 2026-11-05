---
id: bridge.BR-LMS-152
type: bridge
title: Never change what is already paid
summary: "Partly covered. For one loan the paid history is kept, but the unpaid part is rebuilt wrongly and the loan's paid totals are reset."
br_ids: [BR-LMS-152]
brd_section: 7.6
doctypes: [Loan Restructure, Loan]
verdict: partial
analysis_status: verified
dev_items: [D11]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:684"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-152"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-152"
  - "sources/verification/verification_report.md#BR-LMS-152"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-152"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-152"
related: [concept.BR-LMS-152, brd_section.7.6, devitem.D11, decision.restructure, bridge.BR-LMS-125]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. For one loan the paid history is kept, but the unpaid part is rebuilt wrongly and the loan's paid totals are reset.

## Business need

The bank wants repricing to leave paid instalments and posted history untouched and to recalculate only what is still owed (BR-LMS-152, BRD 7.6, PDF page 49). See `concept.BR-LMS-152`.

## Frappe Lending today

A single-loan repricing is a **Loan Restructure** (see `decision.restructure`). When it is approved, the old schedule is marked Restructured and a new one is built. The leftover bulk class would overwrite the rate, but it has no document type and cannot run (see `bridge.BR-LMS-150`). On approval the code also sets the loan's total principal paid and total amount paid to zero (`loan_restructure.py` lines 684-708).

## Match or gap, and why

This is **partly covered**. In the test, approving a restructure kept the old schedule with all 12 rows unchanged, the paid demands still linked to it, and the five repayments and the ledger unchanged (verification_report.md, BR-LMS-152, J5). But the unpaid part was rebuilt wrongly: the accrued interest of 667.87 added to the first EMI was billed as interest and also left in principal, so the loan's pending principal was 60,717.92 against 60,050.05 in the ledger (DEF-18, also in develop). After the restructure the Loan form's paid totals showed 0, and a prior credit adjustment was subtracted twice (DEF-24). The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Check the pending principal against the ledger after every restructure, and read paid-to-date from Loan Repayment, not the Loan form.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch. DEF-18 and DEF-24 are logged in the verification report.
