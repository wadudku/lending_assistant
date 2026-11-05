---
id: concept.BR-LMS-125
type: concept
title: Never overwrite an old plan
summary: "When a repayment plan is replaced, the old one is kept as a superseded version, linked to the new plan and to the event that caused the change."
br_ids: [BR-LMS-125]
brd_section: 7.3
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-125"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-125"
  - "sources/verification/verification_report.md#BR-LMS-125"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-125"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-125"
related: [bridge.BR-LMS-125, brd_section.7.3, devitem.D6, glossary.schedule-version, glossary.restructuring]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a repayment plan is replaced, the old one is kept as a superseded version, linked to the new plan and to the event that caused the change.

## What the rule says

BR-LMS-125 (priority Must, BRD 7.3, PDF page 48) says prior schedules are preserved as superseded versions. Each is linked to the new authoritative version and to the event that caused the replacement.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank must be able to show what a borrower was told to pay at any earlier time, and why it changed. This follows the BRD's principle that every figure must be explicable and reproducible (BRD 7 opening, PDF page 46).

## Example

Plan v1 (12 months) is replaced by plan v2 (18 months) because of a restructure. v1 can still be opened and shows "superseded by v2, reason: the restructure".

## Terms to know

- **Superseded:** replaced by a newer version but kept.
- **Authoritative version:** the plan currently in force.
- **Schedule version:** see `glossary.schedule-version`.
