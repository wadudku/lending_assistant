---
id: devitem.D9
type: devitem
title: D9 Batch run and exception framework
summary: "A planned add-on to Frappe Lending that gives each batch job a status and a per-loan result, a queue for things that go wrong, alerts on job failure and a two-step bulk payment upload. Verification made it larger."
br_ids: [BR-LMS-135, BR-LMS-166, BR-LMS-223, BR-LMS-224, BR-LMS-225]
brd_section: 7.13
doctypes: [Loan Demand, Loan Interest Accrual, Loan Repayment]
dev_items: [D9]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D9"
  - "sources/verification/FINAL_REPORT.md#D9"
  - "sources/verification/reqs.json#BR-LMS-135"
  - "sources/verification/reqs.json#BR-LMS-166"
  - "sources/verification/reqs.json#BR-LMS-223"
  - "sources/verification/reqs.json#BR-LMS-224"
  - "sources/verification/reqs.json#BR-LMS-225"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-135"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-166"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-223"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-224"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-225"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that gives each batch job a status and a per-loan result, a queue for things that go wrong, alerts on job failure and a two-step bulk payment upload. Verification made it larger.

## What we plan to build

D9 adds a Servicing Batch Run record (Draft, Queued, In Process, Completed, Cancelled) that wraps the accrual, demand and classification runs, with one row per loan and its outcome and a Resume failed rows action. A Servicing Exception record (type, loan, owner, opened on, ageing, closure note) holds the things that went wrong. An alert fires on a job failure and on a repeated failure. Bulk repayment becomes two steps: validate the file, then post. It is built in a custom app.

## The gap it closes

In the test, the accrual, demand and classification runs had no clear status (BR-LMS-223) and the demand run had no per-loan result list or resume action (BR-LMS-135). Bulk upload had no upload screen and no validate-all-first step, and a failed loan still got a demand and accrual catch-up and a repost (BR-LMS-166). There were no owned, aged work queues (BR-LMS-224) and no alerting (BR-LMS-225).

## Requirements it closes

BR-LMS-135, BR-LMS-166, BR-LMS-223 and BR-LMS-225 (partly covered) and BR-LMS-224 (gap).

## How, size and dependencies

Size: M to L in the analysis, now L. Verification says the stock error-log notification is disabled and bulk upload is available only through the API (ND-7, ND-43, ND-44). The stock notification and the Assign and First Seen features shorten the alert part, so the final report says the alert plumbing can use the stock Error Log notification once it is enabled. The final report places D9 in step 2, with D3, D13 and D5.
