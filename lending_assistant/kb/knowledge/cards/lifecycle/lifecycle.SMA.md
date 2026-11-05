---
id: lifecycle.SMA
type: lifecycle
title: Loan state SMA
summary: "In the BRD, SMA is the early-warning grade a loan reaches under the configured band. In Frappe Lending it is a classification code on the loan, not a status, and the move into it is not recorded."
br_ids: [BR-LMS-191, BR-LMS-192]
brd_section: 5.3
doctypes: [Loan, Loan Classification]
dev_items: [D2, D15]
lifecycle_state: SMA
fields: [Loan.Classification Code]
options: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1773", "lending/loan_management/doctype/loan/loan.py:1550"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-191"
  - "sources/verification/reqs.json#BR-LMS-192"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-192"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D15"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, glossary.sma, glossary.dpd, glossary.asset-classification, devitem.D15, devitem.D2]
version: 2
status: approved
approved_by: Owner
---
**In short:** In the BRD, SMA is the early-warning grade a loan reaches under the configured band. In Frappe Lending it is a classification code on the loan, not a status, and the move into it is not recorded.

## The BRD state

BRD 5.3 (PDF page 27) defines SMA as: early-warning classification reached under the configured band. SMA means special mention account, an early-warning grade before the non-performing grades. The bands are configurable (BR-LMS-191), so the BRD does not fix their limits.

## The Frappe Lending equivalent

There is no SMA status. The loan has a **Classification Code** field, which the classification run fills from the bands set up on the Company: each band has a lowest and highest days-past-due, a code and a name (`lending/loan_management/doctype/loan/loan.py:1773`, `lending/loan_management/doctype/loan/loan.py:1778`). A band with the code SMA has to be configured by the bank; the plain-English guide's example is SMA at 60 to 89 days past due. The coverage analysis rates the match as partly covered.

## Why they differ

Two differences matter. First, the code is a field, so a loan can be SMA and Disbursed together. Second, the move is not recorded: in the test the grade was written without a Version record, only NPA in and out is logged, and the days-past-due log that the grades could be rebuilt from is rewritten by value-dated payments (BR-LMS-192). For a loan with an unexpired watch period, the code is kept instead of being recalculated (`lending/loan_management/doctype/loan/loan.py:1546`). A restructure of an NPA loan sets a watch period (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:586`), and so does the classification run itself (`lending/loan_management/doctype/loan/loan.py:1341-1353`). The plan is a history record (D15) and a Servicing Status (D2).

## How a loan enters and leaves it

A loan enters SMA when the classification run finds its days past due inside the SMA band (`lending/loan_management/doctype/loan/loan.py:1550`). It leaves when the days past due leave the band, because payment brings them down or because they grow into a non-performing band (see `lifecycle.NPA`).
