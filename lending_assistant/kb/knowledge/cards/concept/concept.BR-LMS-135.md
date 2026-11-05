---
id: concept.BR-LMS-135
type: concept
title: Bill-raising runs as a batch that can restart
summary: "Raising bills for all loans is a batch that gives a result for each loan, so a partial failure can be finished without redoing the loans already done."
br_ids: [BR-LMS-135]
brd_section: 7.4
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-135"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-135"
  - "sources/verification/verification_report.md#BR-LMS-135"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-135"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-135"
related: [bridge.BR-LMS-135, brd_section.7.4, devitem.D9, glossary.batch, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Raising bills for all loans is a batch that gives a result for each loan, so a partial failure can be finished without redoing the loans already done.

## What the rule says

BR-LMS-135 (priority Must, BRD 7.4, PDF page 49) says demand generation is a resumable batch process with per-loan outcomes, so that a partial failure can be completed without reprocessing loans already handled.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bank runs this for tens of thousands of loans, and one failure must neither stop the whole run nor cause the same bill to be raised twice.

## Example

The batch for 50,000 loans crashes at loan 30,001. The restart handles only the remaining 20,000, and the report lists which loans failed and why.

## Terms to know

- **Batch:** a run that processes many loans one after another. See `glossary.batch`.
- **Per-loan outcome:** a recorded result, success or failure, for each loan.
- **Resumable:** a stopped run can continue where it ended. See `glossary.idempotency` for the related idea of safe re-running.
