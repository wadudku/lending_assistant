---
id: devitem.D5
type: devitem
title: "D5 Versioned, approved configuration"
summary: "A planned add-on to Frappe Lending that makes product and risk rules versioned, effective-dated and approved by a second person, and stamps the version used on each loan record."
br_ids: [BR-LMS-117, BR-LMS-197]
brd_section: 7.2
doctypes: [Loan, Loan Product]
dev_items: [D5]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D5"
  - "sources/verification/FINAL_REPORT.md#D5"
  - "sources/verification/reqs.json#BR-LMS-117"
  - "sources/verification/reqs.json#BR-LMS-197"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-117"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-197"
  - "sources/verification/verification_report.md#BR-LMS-117"
  - "sources/verification/verification_report.md#BR-LMS-197"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that makes product and risk rules versioned, effective-dated and approved by a second person, and stamps the version used on each loan record.

## What we plan to build

D5 adds a Loan Product Change Request and a Credit Risk Rule Set, both submittable, with a workflow and an effective date. A scheduler applies an approved change on its effective date. A configuration version field is stamped on the Loan, the Demand, the Accrual, the Repayment and the Classification, so each record shows which rule version it used. It is built in a custom app.

## The gap it closes

BR-LMS-117 asks for product rules with versions, start dates and approval, and BR-LMS-197 asks that grade, provision and income rules are owned, versioned and approved. In the test, both are gaps: there are no effective dates, no approval step, no version number stored on loans or events, and results do not store a rule version. Verification found that the payment order is read from the product at each repayment, so a product edit changes how existing loans are repaid.

## Requirements it closes

BR-LMS-117 and BR-LMS-197, both verified as gaps.

## How, size and dependencies

Size: L (over three weeks), unchanged by verification, with small additions, including clearing the cached NPA thresholds when a product or the Company is saved (ND-25). The analysis names D5 with D11 and D14 as the big bank-grade pieces; the final report places it in step 2, with D9, D3 and D13.
