---
id: devitem.D10
type: devitem
title: D10 Reconciliation reports
summary: "A planned add-on to Frappe Lending that adds reports to check that interest, payments and partner positions agree across the records, and raises an exception for anything unmatched."
br_ids: [BR-LMS-145, BR-LMS-171, BR-LMS-213]
brd_section: 7.5
doctypes: [Loan Interest Accrual, Loan Demand, Loan Repayment, Loan Partner]
dev_items: [D10]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D10"
  - "sources/verification/FINAL_REPORT.md#D10"
  - "sources/verification/reqs.json#BR-LMS-145"
  - "sources/verification/reqs.json#BR-LMS-171r"
  - "sources/verification/reqs.json#BR-LMS-213"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-145"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-171"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-213"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [bridge.BR-LMS-171r, devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that adds reports to check that interest, payments and partner positions agree across the records, and raises an exception for anything unmatched.

## What we plan to build

D10 adds script reports: an interest chain (schedule, demand, accrual, collected, general ledger), repayments against the CBS reference, and the partner position. An unmatched item creates a Servicing Exception record (the queue defined in D9). It is built in a custom app.

## The gap it closes

BR-LMS-145 asks to check that the interest numbers agree everywhere. In the test, no such reconciliation report exists, and the CBS side also needs the integration (BR-LMS-145). BR-LMS-171 in section 7.7, which matches every payment from the bank to the books, needs the CBS feed and a reconciliation report. BR-LMS-213 asks for partner settlements and checks, and there was no scheduled partner reconciliation report.

## Requirements it closes

BR-LMS-145 (gap), BR-LMS-171 in section 7.7 (a gap that needs the CBS link) and BR-LMS-213 (partly covered). See `bridge.BR-LMS-171r`.

## How, size and dependencies

Size: M, unchanged by verification. The partner position now sits in ND-40 and `devitem.D19`. The CBS side needs the integration (BR-LMS-145, BR-LMS-171); the CBS posting bridge is `devitem.D13`. The final report places D10 in its last group.
