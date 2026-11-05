---
id: bridge.BR-LMS-157
type: bridge
title: The repricing batch is safe to run and rerun
summary: "Gap. There is no repricing batch, and in the test a second stale restructure for the same change was applied on top of the first."
br_ids: [BR-LMS-157]
brd_section: 7.6
doctypes: [Loan Restructure]
verdict: gap
analysis_status: verified
dev_items: [D11]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:108"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-157"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-157"
  - "sources/verification/verification_report.md#BR-LMS-157"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-157"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-157"
related: [concept.BR-LMS-157, brd_section.7.6, devitem.D11, bridge.BR-LMS-135, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. There is no repricing batch, and in the test a second stale restructure for the same change was applied on top of the first.

## Business need

The bank wants a repricing batch that is idempotent, transactional per loan, resumable and auditable (BR-LMS-157, BRD 7.6, PDF page 50). See `concept.BR-LMS-157`.

## Frappe Lending today

There is no repricing batch. A **Loan Restructure** has one check against a repeat: another restructure for the same loan that is Initiated is refused (`loan_restructure.py` lines 108-112).

## Match or gap, and why

This is a **gap**. In the test, a second draft restructure for the same 15% change was submitted and approved after the first, and a third schedule became Active, the loan's restructure count stayed at 1 (DEF-19), and the accrued interest was added to principal again (DEF-18) (verification_report.md, BR-LMS-157, J5). So a rerun was not prevented. The coverage analysis rated it a gap, and verification confirmed that. The ordinary batch of bill-raising has its own per-loan error handling (see `bridge.BR-LMS-135`), but that is not a repricing batch.

## What to do today

Delete stale draft restructures before approving a new one, and approve at most one restructure per loan for a given change.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch.
