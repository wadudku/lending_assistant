---
id: bridge.BR-LMS-132
type: bridge
title: "\"What is owed on this date\" view"
summary: "Partly covered. A due-details API and a Loan Outstanding Report give amounts as at a date, but the report has no penalty or charge columns."
br_ids: [BR-LMS-132]
brd_section: 7.4
doctypes: [Loan Repayment, Loan]
verdict: partial
analysis_status: verified
dev_items: [D7]
lending_version: 16.5.1
code_refs: ["lending/api.py:79", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:2956"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-132"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-132"
  - "sources/verification/verification_report.md#BR-LMS-132"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-132"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-132"
related: [concept.BR-LMS-132, brd_section.7.4, devitem.D7, glossary.demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A due-details API and a Loan Outstanding Report give amounts as at a date, but the report has no penalty or charge columns.

## Business need

The bank wants staff to see the overdue and current breakdown of a loan at any date, without posting (BR-LMS-132, BRD 7.4, PDF page 48). See `concept.BR-LMS-132`.

## Frappe Lending today

Two whitelisted calls return dues: `get_due_details` (`api.py` line 79) and `get_bulk_due_details` (`loan_repayment.py` line 2956). The staff report Loan Outstanding Report has an As On Date filter and a Loan filter. A draft **Loan Repayment** also shows the amounts due.

## Match or gap, and why

This is **partly covered**. In the test, the report showed interest overdue of 632.87 on one date, and principal of 3,942.03 plus interest of 1,180.84 on a later one (verification_report.md:237). It has no penalty or charges columns, and its days-past-due and instalment counts were current values, not values as at the chosen date (121 and 4, even for the earlier date). There is no single staff screen of "owed on date X" by component. The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Use the Loan Outstanding Report for principal and interest as at a date, and a draft Loan Repayment for the full amounts due. Do not use the report's days-past-due value for a past date.

## Planned fix

Dev item D7 (`devitem.D7`) adds a staff due-details screen.
