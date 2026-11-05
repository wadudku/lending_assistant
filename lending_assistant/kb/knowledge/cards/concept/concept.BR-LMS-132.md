---
id: concept.BR-LMS-132
type: concept
title: "\"What is owed on this date\" view"
summary: "Staff can see, for any date, what a loan owes in overdue and current amounts by component, without posting anything."
br_ids: [BR-LMS-132]
brd_section: 7.4
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-132"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-132"
  - "sources/verification/verification_report.md#BR-LMS-132"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-132"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-132"
related: [bridge.BR-LMS-132, brd_section.7.4, devitem.D7, glossary.demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** Staff can see, for any date, what a loan owes in overdue and current amounts by component, without posting anything.

## What the rule says

BR-LMS-132 (priority Must, BRD 7.4, PDF page 48) says staff can obtain a due-details view that returns the overdue and current component breakdown for a loan at any date, without posting anything.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a borrower or a collector asks "what do I owe on this day?" and the answer has to come from the loan system without changing it.

## Example

Rahim calls on 20 August. Staff see: overdue EMI 2 of 8,979 (interest about 1,05x, principal about 7,92x), plus penalty 44, and nothing else due yet.

## Terms to know

- **Due details:** what is overdue and what is current, split by component.
- **As-on date:** the date for which the amounts are worked out.
- **Non-posting:** nothing is saved or posted.
