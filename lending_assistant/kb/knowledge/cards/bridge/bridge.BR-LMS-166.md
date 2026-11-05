---
id: bridge.BR-LMS-166
type: bridge
title: Upload many payments in one file
summary: "Partly covered. There is a bulk posting method and a log per loan, but no upload screen, no validate-all-first step and no resume."
br_ids: [BR-LMS-166]
brd_section: 7.7
doctypes: [Loan Repayment, Bulk Repayment Log]
verdict: partial
analysis_status: verified
dev_items: [D9]
fields: [Bulk Repayment Log.Status, Bulk Repayment Log.Trace ID, Bulk Repayment Log.Failed Repayment]
options: [Bulk Repayment Log.Status=Success, Bulk Repayment Log.Status=Failure]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:3403"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-166"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-166"
  - "sources/verification/verification_report.md#BR-LMS-166"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-166"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-166"
related: [concept.BR-LMS-166, bridge.BR-LMS-162]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. There is a bulk posting method and a log per loan, but no upload screen, no validate-all-first step and no resume.

## Business need

Bulk payments need validation before posting, a result per row, and the ability to resume (BR-LMS-166, BRD 7.7.1, PDF page 51). See `concept.BR-LMS-166`.

## Frappe Lending today

A method called `post_bulk_payments` takes a list of payments and posts them in a background job. It is available as a web call (POST) and has no screen. Each loan gets a **Bulk Repayment Log** with a **Status** (Success or Failure), the failed repayment, a trace ID and the error traceback. Frappe's general **Data Import** tool also exists.

## Match or gap, and why

This is **partly covered**. The pieces that exist: bulk posting and a result for each loan. The pieces that do not: a place to upload the file, a "validate every row first" step, and a resume.

In the live test, three rows were posted. Two succeeded, and one with an invalid repayment type failed and was logged with its error. Only one check runs before posting, which is whether each loan exists: a file naming a loan that does not exist is rejected whole with an HTTP 404 error, before anything posts. Every other row error only appears during posting, so a half-posted file is possible. After each loan, even a failed one, the job also raises any missing bills (demands) and interest accruals up to today and runs a repayment repost (redoing the loan's repayment postings).

## What to do today

Check the file by hand before sending it: loan numbers, repayment types, amounts, value dates and duplicate references. Send it in small batches. Afterwards read the Bulk Repayment Log for any Failure rows.

## Planned fix

D9 (the batch run and exception framework) adds a two-step upload: validate the file first, then post. The verification added ND-7: a bulk payment file screen with resume, per-file totals and no catch-up for failed rows.
