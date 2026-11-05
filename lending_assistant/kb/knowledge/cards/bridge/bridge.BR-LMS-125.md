---
id: bridge.BR-LMS-125
type: bridge
title: Never overwrite an old plan
summary: "Partly covered. The old plan is kept with a new status, but it has no link to the plan that replaced it."
br_ids: [BR-LMS-125]
brd_section: 7.3
doctypes: [Loan Repayment Schedule, Loan Restructure]
verdict: partial
analysis_status: verified
dev_items: [D6]
fields: [Loan Repayment Schedule.Status, Loan Repayment Schedule.Loan Restructure]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:599", "lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.json:168"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-125"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-125"
  - "sources/verification/verification_report.md#BR-LMS-125"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-125"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-125"
related: [concept.BR-LMS-125, brd_section.7.3, devitem.D6, decision.restructure, glossary.schedule-version]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The old plan is kept with a new status, but it has no link to the plan that replaced it.

## Business need

The bank wants old schedules kept as superseded versions, linked to the new version and to the causing event (BR-LMS-125, BRD 7.3, PDF page 48). See `concept.BR-LMS-125`.

## Frappe Lending today

When a restructure is submitted, the old **Loan Repayment Schedule** is set to Restructured, or to Rescheduled for a Pre Payment or Advance Payment (`loan_restructure.py` lines 599-602). When a new tranche is drawn, earlier schedules are set to Outdated (`loan_disbursement.py` line 307). The new schedule links to its restructure through **Loan Restructure** (`loan_repayment_schedule.json` line 168).

## Match or gap, and why

This is **partly covered**. In the test, the old plan was kept with its rows unchanged and a new status (verification_report.md:446). There was no "replaced by" link: the old schedule had no pointer to the new one or to the restructure, so the chain has to be rebuilt by loan and date. On the direct-schedule path described under BR-LMS-126, the old plan was not marked replaced at all. After a restructure the Loan form's own paid-to-date totals restart, and the old values remain only on the Loan Restructure record (verification_report.md:563-570). The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Find the earlier plans by loan and status (Restructured, Rescheduled, Outdated) and read the reason from the Loan Restructure record.

## Planned fix

Dev item D6 (`devitem.D6`) adds a version number, a link to the plan that replaced it, and the trigger of the change.
