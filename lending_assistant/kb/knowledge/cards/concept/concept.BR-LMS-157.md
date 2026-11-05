---
id: concept.BR-LMS-157
type: concept
title: The repricing batch is safe to run and rerun
summary: "The repricing batch can be run again safely: it is idempotent, works loan by loan, can be resumed, and records a status for each row."
br_ids: [BR-LMS-157]
brd_section: 7.6
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-157"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-157"
  - "sources/verification/verification_report.md#BR-LMS-157"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-157"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-157"
related: [bridge.BR-LMS-157, brd_section.7.6, glossary.idempotency, glossary.batch]
version: 1
status: approved
approved_by: Owner
---
**In short:** The repricing batch can be run again safely: it is idempotent, works loan by loan, can be resumed, and records a status for each row.

## What the rule says

BR-LMS-157 (priority Must, BRD 7.6, PDF page 50) says the repricing batch is idempotent, transactional per loan, resumable and auditable with row-level status.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a big batch can stop halfway, and running it again must finish the job without changing a loan twice.

## Example

The run stops at loan 3,000 of 5,000. Restarting it finishes loans 3,001 to 5,000, and loans 1 to 3,000 are not repriced again.

## Terms to know

- **Idempotent:** running it twice has the same result as running it once. See `glossary.idempotency`.
- **Transactional per loan:** each loan succeeds or fails on its own.
- **Row-level status:** a recorded result for each loan.
