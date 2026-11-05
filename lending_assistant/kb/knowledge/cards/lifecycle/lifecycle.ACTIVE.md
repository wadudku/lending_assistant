---
id: lifecycle.ACTIVE
type: lifecycle
title: Loan state ACTIVE
summary: "In the BRD, ACTIVE is a loan with a schedule, raising demands and accruing interest. In Frappe Lending it is Disbursed for term loans, and Active only for credit lines."
br_ids: [BR-LMS-102]
brd_section: 5.3
doctypes: [Loan, Loan Disbursement]
dev_items: [D2]
lifecycle_state: ACTIVE
fields: [Loan.Status]
options: [Loan.Status=Disbursed, Loan.Status=Active]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:699", "lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:697"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-102"
  - "sources/verification/verification_report.md#BR-LMS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-102"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, devitem.D2]
version: 1
status: approved
approved_by: Owner
---
**In short:** In the BRD, ACTIVE is a loan with a schedule, raising demands and accruing interest. In Frappe Lending it is Disbursed for term loans, and Active only for credit lines.

## The BRD state

BRD 5.3 (PDF page 27) defines ACTIVE as: schedule generated; demands being raised and interest accruing. It is the normal running state of a loan.

## The Frappe Lending equivalent

The nearest Frappe Lending value depends on the loan type. A term loan whose disbursed amount reaches the loan amount becomes Disbursed (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:699`). A line of credit becomes Active (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:697`). The word Active is also used for the live repayment schedule of a loan, which is a different thing: a schedule is Active while it is the current plan. The coverage analysis rates the match as covered.

## Why they differ

The BRD uses one name for all running loans. Frappe Lending uses two, and keeps the loan's other facts (overdue, NPA, frozen) as separate fields, so a running loan can still read Disbursed while it is overdue (see `lifecycle.OVERDUE`). The proposed Servicing Status field (D2) would show ACTIVE only when no higher-ranked state applies.

## How a loan enters and leaves it

On a disbursement that completes the loan amount, the Loan Disbursement code sets Disbursed (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:699`); a part-disbursement gives Partially Disbursed (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:701`); a line of credit gets Active at its first disbursement (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:697`). The daily job closes an Active line of credit that is past its end date with no utilised limit (`lending/loan_management/doctype/loan/loan.py:2144`, scheduled at `lending/hooks.py:192`). In the tests, Draft moved to Sanctioned and then Disbursed.
