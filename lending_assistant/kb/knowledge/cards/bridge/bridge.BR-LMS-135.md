---
id: bridge.BR-LMS-135
type: bridge
title: Bill-raising runs as a batch that can restart
summary: "Partly covered. A failure on one loan is logged and rolled back, and a re-run does not duplicate bills, but there is no per-loan result list and no resume action."
br_ids: [BR-LMS-135]
brd_section: 7.4
doctypes: [Process Loan Demand, Loan Demand]
verdict: partial
analysis_status: verified
dev_items: [D9]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_demand/loan_demand.py:394"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-135"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-135"
  - "sources/verification/verification_report.md#BR-LMS-135"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-135"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-135"
related: [concept.BR-LMS-135, brd_section.7.4, devitem.D9, glossary.batch, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A failure on one loan is logged and rolled back, and a re-run does not duplicate bills, but there is no per-loan result list and no resume action.

## Business need

The bank wants bill-raising to be a resumable batch with a recorded outcome for each loan (BR-LMS-135, BRD 7.4, PDF page 49). See `concept.BR-LMS-135`.

## Frappe Lending today

Each run is a submitted **Process Loan Demand** document. When a run covers more than one loan, an error on one loan is caught, written to the Error Log under the title "Term Loan Demand Generation Error", and rolled back, and the next loan is still tried (`loan_demand.py` lines 394-407). When a run is scoped to one loan, the error is raised to the caller instead (`loan_demand.py` lines 403-404).

## Match or gap, and why

This is **partly covered**. In the test, running the same date again created no new demands (9 before, 9 after) (verification_report.md:190). With a blank Interest Accrued Account on a copy of the product, a batch of two loans billed nothing, each failure was logged and rolled back, and the other loan was not blocked; after the account was restored, a re-run billed each loan once (verification_report.md:812). The Process Loan Demand document has no per-loan result list and no resume action. The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

After a failed run, read the Error Log for the title above, fix the cause, and run Process Loan Demand again for the same date; the loans already billed are skipped.

## Planned fix

Dev item D9 (`devitem.D9`) adds a per-loan result list and a resume action to the batch.
