---
id: devitem.D1
type: devitem
title: D1 Funded-loan handoff intake
summary: "A planned add-on to Frappe Lending that accepts one complete handoff package for a funded loan, rejects incomplete ones into an exception queue and books the loan and its payout together."
br_ids: [BR-LMS-100, BR-LMS-120]
brd_section: 7.1
doctypes: [Loan, Loan Disbursement]
dev_items: [D1]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D1"
  - "sources/verification/FINAL_REPORT.md#D1"
  - "sources/verification/reqs.json#BR-LMS-100"
  - "sources/verification/reqs.json#BR-LMS-120"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-100"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-120"
  - "sources/verification/verification_report.md#BR-LMS-100"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [devitem.D12, devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that accepts one complete handoff package for a funded loan, rejects incomplete ones into an exception queue and books the loan and its payout together.

## What we plan to build

D1 adds a whitelisted API that takes the full handoff package from the loan origination system, checks it, and creates the Loan and the Loan Disbursement in one transaction. A unique origination reference on the loan means a repeat call returns the same loan instead of a second one. Packages that fail the checks go to a Handoff Exception queue. A daily control report compares the origination system with the loan system. It is built in a custom app, without changing Frappe Lending.

## The gap it closes

In NRB's flow the loan arrives already funded, so booking and disbursement happen together. In the live test, nothing checks the handoff package as a whole, nothing sends an incomplete handoff to an exception queue, and the loan has no field for the origination audit reference. Verification found that no booking API exists in Frappe Lending 16.5.1.

## Requirements it closes

BR-LMS-100 (accept only loans that are really paid out) and BR-LMS-120 (build the first repayment plan). The coverage analysis also links BR-LMS-010, BR-LMS-011 and BR-GOV-030 (the daily control between the two systems).

## How, size and dependencies

Size: M (one to three weeks), unchanged by verification. Verification added two items to the scope: a product-level default for the payment holiday (ND-2) and a control on rate deviation (ND-5). The intake must also pass the repayment start date, because the schedule depends on it (DEF-5). The analysis puts D1 in the first group to build, with D2, D8 and D12; the final report keeps it in the foundation pack (Pack B).
