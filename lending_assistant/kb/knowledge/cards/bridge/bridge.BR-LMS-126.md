---
id: bridge.BR-LMS-126
type: bridge
title: Only an approved change may rebuild a plan
summary: "Gap. In the test, a schedule was submitted with no restructure at all, and the loan ended with two Active plans. The coverage analysis rated it partly covered."
br_ids: [BR-LMS-126]
brd_section: 7.3
doctypes: [Loan Repayment Schedule, Loan Restructure]
verdict: gap
analysis_status: verified
dev_items: [D6]
fields: [Loan Repayment Schedule.Restructure Type]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:94", "lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:116", "lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.json:307"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-126"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-126"
  - "sources/verification/verification_report.md#BR-LMS-126"
  - "sources/verification/verification_report.md#new-development-items-found-in-verification-numbered-nd-n-linked-to-analysis-d-items-where-they-exist"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-126"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-126"
related: [concept.BR-LMS-126, brd_section.7.3, devitem.D6, decision.restructure, bridge.BR-LMS-125]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. In the test, a schedule was submitted with no restructure at all, and the loan ended with two Active plans. The coverage analysis rated it partly covered.

## Business need

The bank wants a plan rebuilt only because of an approved change, with the trigger recorded on the new version (BR-LMS-126, BRD 7.3, PDF page 48). See `concept.BR-LMS-126`.

## Frappe Lending today

The **Loan Repayment Schedule** has a **Restructure Type** (Normal Restructure, Advance Payment or Pre Payment) (`loan_repayment_schedule.json` lines 307-310). Its validate (`loan_repayment_schedule.py` lines 94-104) and on_submit (lines 116-118) do not check that the parent restructure is approved or that the loan has no other Active schedule; a search of `loan_repayment_schedule.py` for "Approved" finds nothing. The decision on who approves a restructure is in `decision.restructure`.

## Match or gap, and why

This is a **gap**. The coverage analysis rated it partly covered; verification found nothing stops a plan from being rebuilt without an approved event (verification_report.md:58, 447). In the test, two things got through. First, the draft schedule of an unsubmitted restructure was submitted by the test user while the restructure stayed Draft. Second, a new schedule at 18% with no restructure at all was inserted and submitted, so the loan had two Active schedules (at 14% and 18%). In the test, Pre Payment and Advance Payment restructures were approved automatically with no approver (verification_report.md:529). The schedule stores the trigger only as the restructure type (`loan_repayment_schedule.json` lines 307-310). There is no field for a rate change, moratorium or tenor change, and no link to the superseding version.

## What to do today

Restrict who can create and submit a Loan Repayment Schedule directly, and treat any schedule without a restructure as an error to correct. Check that a loan has one Active schedule only.

## Planned fix

Dev item D6 (`devitem.D6`) records the trigger and its document on the schedule. Verification added ND-19 to it: one Active schedule per loan and an approved parent event (verification_report.md:58 and 1436; `devitem.D6`).
