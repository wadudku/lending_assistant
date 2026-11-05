---
id: lifecycle.WRITTEN_OFF
type: lifecycle
title: Loan state WRITTEN_OFF
summary: "In the BRD, WRITTEN_OFF is a balance written off under approval, with recovery rights kept. In Frappe Lending it is a status set when a write-off is submitted, and the automatic write-off has no approver."
br_ids: [BR-LMS-195, BR-LMS-202, BR-LMS-203, BR-LMS-201, BR-LMS-205]
brd_section: 5.3
doctypes: [Loan, Loan Write Off]
dev_items: [D2, D8]
lifecycle_state: WRITTEN_OFF
fields: [Loan.Status, Loan.Written Off Amount]
options: [Loan.Status=Written Off]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_write_off/loan_write_off.py:205", "lending/loan_management/doctype/loan_write_off/loan_write_off.py:204"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-195"
  - "sources/verification/reqs.json#BR-LMS-202"
  - "sources/verification/reqs.json#BR-LMS-203"
  - "sources/verification/reqs.json#BR-LMS-201"
  - "sources/verification/reqs.json#BR-LMS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-195"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-202"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-203"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-205"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D8"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, decision.waiver, devitem.D8, devitem.D2]
version: 2
status: approved
approved_by: Owner
---
**In short:** In the BRD, WRITTEN_OFF is a balance written off under approval, with recovery rights kept. In Frappe Lending it is a status set when a write-off is submitted, and the automatic write-off has no approver.

## The BRD state

BRD 5.3 (PDF page 27) defines WRITTEN_OFF as: unrecovered balance written off under approval; recovery rights retained per policy. BR-LMS-202 asks that the loan's history stays retrievable, and BR-LMS-203 that later recoveries are booked against the original loan.

## The Frappe Lending equivalent

Frappe Lending has a **Status** value Written Off, and the coverage analysis rates the match as covered. Submitting a **Loan Write Off** sets it, unless the write-off is a settlement write-off and it is the only one (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:204`, `lending/loan_management/doctype/loan_write_off/loan_write_off.py:205`). Cancelling the last submitted write-off returns the loan to Disbursed (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:199`). The company's DPD threshold for automatic write-off is read by the nightly classification, which creates and submits a write-off when the days past due exceed it. While a loan is Written Off, a repayment of any type except Write Off Recovery or Write Off Settlement is refused, unless the repayment is a write-off waiver (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1019-1024`; `decision.waiver` has the same exception).

## Why they differ

The verified results are covered for BR-LMS-195, 202 and 203. The controls are weaker than the BRD's: in the test, a manual write-off had no eligibility check (a loan with 0 days past due was written off) and the automatic write-off had no approver (DEF-35). After a write-off, accrual rows kept being created, and a classification run blanked the grade (DEF-36). The approval and record fields of BR-LMS-201 and BR-LMS-205 are partly covered (D8).

## How a loan enters and leaves it

A loan enters Written Off when a write-off is submitted, by a user or by the nightly run. It also goes back to Written Off when a Write Off Recovery or Write Off Settlement repayment is cancelled (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1519-1520`) and when a repayment repost ends with the loan written off (`lending/loan_management/doctype/loan_repayment_repost/loan_repayment_repost.py:476`). It stays there while recoveries come in as Write Off Recovery repayments, which are credited to the recovery account, and the loan stays Written Off (BR-LMS-203). Cancelling the last submitted write-off sends the loan back to Disbursed; while another submitted write-off remains, the loan stays Written Off (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:196-199`).

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
