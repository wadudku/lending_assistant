---
id: concept.BR-LMS-223
type: concept
title: Every batch has a clear status
summary: "Every batch job (interest, bills, grades, uploads) shows a clear state and a result for each row, and can be restarted without posting anything twice."
br_ids: [BR-LMS-223]
brd_section: 7.13
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-223"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-223"
  - "sources/verification/verification_report.md#BR-LMS-223"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-223"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-223"
related: [bridge.BR-LMS-223, brd_section.7.13, glossary.batch, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every batch job (interest, bills, grades, uploads) shows a clear state and a result for each row, and can be restarted without posting anything twice.

## What the rule says

BR-LMS-223 in section 7.13 (Must, BRD PDF page 55) says every batch process shall maintain an explicit state (draft, queued, in process, completed or cancelled) together with row-level outcomes, and shall be resumable without double posting.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a nightly batch touches thousands of loans, and when it stops half way the operators must see how far it got, what failed, and be able to finish it safely.

## Example

The interest batch shows "In process: 32,000 of 50,000 done, 3 failed".

## Terms to know

- **Batch:** a job that works through many loans in one run. See `glossary.batch`.
- **State:** where the batch stands: draft, queued, in process, completed or cancelled.
- **Row-level outcome:** the result for each loan in the batch.
- **Resumable:** can be restarted without repeating work already done. See `glossary.idempotency`.
