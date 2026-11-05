---
id: bridge.BR-LMS-143
type: bridge
title: "Undo and redo interest for a period, with approval"
summary: "Partly covered. Loan Accrual Repost restores missing ledger entries but does not reverse and redo interest, and it has no approval step. The coverage analysis rated it covered."
br_ids: [BR-LMS-143]
brd_section: 7.5
doctypes: [Loan Accrual Repost, Loan Interest Accrual]
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_accrual_repost/loan_accrual_repost.py:30", "lending/loan_management/doctype/loan_accrual_repost/loan_accrual_repost.json:78"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-143"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-143"
  - "sources/verification/verification_report.md#BR-LMS-143"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-143"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-143"
related: [concept.BR-LMS-143, brd_section.7.5, bridge.BR-LMS-140, glossary.maker-checker, glossary.batch]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Loan Accrual Repost restores missing ledger entries but does not reverse and redo interest, and it has no approval step. The coverage analysis rated it covered.

## Business need

The bank wants an approved batch reversal and repost of accruals over a date range, with the reversed entries kept (BR-LMS-143, BRD 7.5, PDF page 49). See `concept.BR-LMS-143`.

## Frappe Lending today

**Loan Accrual Repost** has a from date, a to date and a table of loans, and only the System Manager role (`loan_accrual_repost.json` line 78). On submit it runs at once, or in the background for more than 10 loans (`loan_accrual_repost.py` lines 30-34). For a Disbursed or Active loan it creates the ledger entries of a submitted accrual that has none (`loan_accrual_repost.py` lines 90-96), and it reads only Normal Interest accruals (line 104), so penal interest is not covered. It has no status, reason or workflow field.

## Match or gap, and why

This is **partly covered**. The coverage analysis rated it covered; verification found that it does not recalculate interest; it only repairs missing ledger entries (and, for a Written Off or Settled loan, reverses those on or after the write-off date; `loan_accrual_repost.py` lines 39 and 63) (verification_report.md:69, 824, DEF-46). In the test on a loan with 34 accruals, a repost with nothing wrong changed nothing, and after one accrual's ledger entries were set to cancelled it restored them and kept the cancelled pair. In the test, cancelling one accrual worked, but neither a later accrual run nor a run for that day re-created it, so 38.36 of interest was lost. The "undo and redo at the right rate" route does not exist, and approval is absent. At the J11 review the team decided the verdict stays partly covered: the repost repairs the ledger, and the redo is missing.

## What to do today

Restrict Loan Accrual Repost to a few users. After any correction, compare accrued and billed interest by hand, since a cancelled accrual is not re-created.

## Planned fix

DEF-46 and ND-46 in the verification report record the missing redo and approval. This row has no D item.
