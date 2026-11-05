---
id: lifecycle.BOOKED
type: lifecycle
title: Loan state BOOKED
summary: "In the BRD, BOOKED is a funded loan that has been accepted and recorded, with no schedule yet. In Frappe Lending the nearest state is Sanctioned, which is reached before the money moves."
br_ids: [BR-LMS-003, BR-LMS-102]
brd_section: 5.3
doctypes: [Loan, Loan Disbursement]
dev_items: [D1, D2]
lifecycle_state: BOOKED
fields: [Loan.Status]
options: [Loan.Status=Sanctioned]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:471", "lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:699"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-102"
  - "sources/verification/reqs.json#BR-LMS-120"
  - "sources/verification/verification_report.md#BR-LMS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-102"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D1"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, devitem.D1, devitem.D2]
version: 1
status: approved
approved_by: Owner
---
**In short:** In the BRD, BOOKED is a funded loan that has been accepted and recorded, with no schedule yet. In Frappe Lending the nearest state is Sanctioned, which is reached before the money moves.

## The BRD state

BRD 5.3 (PDF page 27) defines BOOKED as: a confirmed funded loan accepted and recorded, with the schedule not yet generated. It is the first of the twelve servicing states. NRB's flow starts from a loan that is already funded, so the loan system books it after the money has gone out.

## The Frappe Lending equivalent

The nearest Frappe Lending status is Sanctioned. When a Loan is submitted, the code sets its **Status** to Sanctioned (`lending/loan_management/doctype/loan/loan.py:471`); a draft loan is Draft, which is Frappe-only. The repayment schedule is created at disbursement, which matches the BRD's "schedule not yet generated".

## Why they differ

The two differ in timing. Frappe books a loan before the money moves, while NRB books it after, so the coverage analysis rates this match as partly covered and proposes booking and disbursing together in the handoff (D1). The names also differ: Sanctioned against BOOKED. The BRD itself says the names are supplier-proposed and NRB's own vocabulary should replace them (BR-LMS-003). The verified result for BR-LMS-102 is covered, with the caveat that no history of status changes is kept.

## How a loan enters and leaves it

A submitted Loan becomes Sanctioned (`lending/loan_management/doctype/loan/loan.py:471`), except that an imported loan whose status is already Closed keeps it (`lending/loan_management/doctype/loan/loan.py:465`). It leaves Sanctioned at the first disbursement: the Loan Disbursement code then sets Partially Disbursed or Disbursed (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:701`, `lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:699`), or Active for a line of credit (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:697`). In the walkthrough tests the status moved Draft, Sanctioned, then Disbursed.
