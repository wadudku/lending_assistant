---
id: lifecycle.PARTIALLY_DISBURSED
type: lifecycle
title: Loan state PARTIALLY_DISBURSED
summary: "In the BRD, PARTIALLY_DISBURSED is a tranche loan with an approved balance still to be drawn. Frappe Lending has a status of the same name, and it matches."
br_ids: [BR-LMS-102, BR-LMS-122]
brd_section: 5.3
doctypes: [Loan, Loan Disbursement]
dev_items: [D2]
lifecycle_state: PARTIALLY_DISBURSED
fields: [Loan.Status]
options: [Loan.Status=Partially Disbursed]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:701", "lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:699"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-122"
  - "sources/verification/reqs.json#BR-LMS-102"
  - "sources/verification/verification_report.md#BR-LMS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-122"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, devitem.D2]
version: 1
status: approved
approved_by: Owner
---
**In short:** In the BRD, PARTIALLY_DISBURSED is a tranche loan with an approved balance still to be drawn. Frappe Lending has a status of the same name, and it matches.

## The BRD state

BRD 5.3 (PDF page 27) defines PARTIALLY_DISBURSED as: a tranche product with an approved balance still to be drawn. A tranche loan is paid out in parts rather than in one amount.

## The Frappe Lending equivalent

Frappe Lending has a **Status** value Partially Disbursed. When a disbursement is submitted and the total disbursed is still below the loan amount, the code sets it (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:701`). The verification confirmed this for BR-LMS-122: Frappe keeps one repayment schedule per disbursement and a tranche number. The coverage analysis rates the match as covered.

## Why they differ

The two agree on the meaning and the name. The loan keeps the status until the rest is drawn or the loan moves on. The only remaining difference is the usual one: Frappe's status is one field among several, and the proposed Servicing Status (D2) would copy it across.

## How a loan enters and leaves it

A loan enters this state on a disbursement that leaves part of the loan amount undrawn (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:701`). It leaves when a later disbursement brings the total to the loan amount, which sets Disbursed (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:699`). Cancelling a disbursement can send the status back (the cancel path has its own status rules, `lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:641` for the case where nothing is left disbursed). In the test, the loan moved Sanctioned, Partially Disbursed, then Disbursed.
