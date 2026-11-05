---
id: bridge.BR-LMS-124
type: bridge
title: "\"What-if\" view with nothing saved"
summary: "Partly covered. A draft Loan Restructure shows a new plan before it is submitted, but each trial leaves draft records behind."
br_ids: [BR-LMS-124]
brd_section: 7.3
doctypes: [Loan Restructure, Loan Repayment Schedule, Loan Repayment]
verdict: partial
analysis_status: verified
dev_items: [D6]
lending_version: 16.5.1
code_refs: ["lending/api.py:16", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:173"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-124"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-124"
  - "sources/verification/verification_report.md#BR-LMS-124"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-124"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-124"
related: [concept.BR-LMS-124, brd_section.7.3, devitem.D6, decision.restructure, glossary.schedule-version]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A draft Loan Restructure shows a new plan before it is submitted, but each trial leaves draft records behind.

## Business need

The bank wants a simulation that shows the effect of a proposed change without committing it (BR-LMS-124, BRD 7.3, PDF page 48). See `concept.BR-LMS-124`.

## Frappe Lending today

For a new loan, the API `get_repayment_schedule` (`api.py` line 16) returns a proposed plan from the product, amount, rate and term. For an existing loan, a draft **Loan Restructure** builds a draft **Loan Repayment Schedule** that can be read before the restructure is submitted. Saving a draft Pre Payment repayment does the same through `create_update_loan_reschedule` (`loan_repayment.py` line 173).

## Match or gap, and why

This is **partly covered**. In the test, four draft restructures on one loan each built a draft schedule showing the new EMI, rows and total interest, and the loan itself was unchanged (verification_report.md:423). But it is not "nothing saved": each trial left a draft restructure and a draft schedule with status Initiated, and that draft schedule could be submitted on its own (see BR-LMS-126). The prepayment version left three draft records (verification_report.md:504). In 16.5.1 a Normal Restructure fails with a TypeError on products whose broken-period interest recovery is "Add to First EMI", which includes all four products of the test site (DEF-17, verification_report.md:1021-1024). The what-if worked in the test only on a copy of the product set to "Upfront Deduction" (verification_report.md:394). The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Use a draft restructure for the preview, read the numbers, then delete the draft restructure and its draft schedule. Do not submit either.

## Planned fix

Dev item D6 (`devitem.D6`) adds a Simulate button that runs the calculation without saving a record.
