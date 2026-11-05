---
id: concept.BR-LMS-156
type: concept
title: Each repriced loan gets a new plan version
summary: "Each repriced loan receives a new schedule version, and the earlier version and the relationship between them are kept."
br_ids: [BR-LMS-156]
brd_section: 7.6
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-156"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-156"
  - "sources/verification/verification_report.md#BR-LMS-156"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-156"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-156"
related: [bridge.BR-LMS-156, brd_section.7.6, glossary.schedule-version, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each repriced loan receives a new schedule version, and the earlier version and the relationship between them are kept.

## What the rule says

BR-LMS-156 (priority Must, BRD 7.6, PDF page 50) says each repriced loan receives a new schedule version, with the earlier version and the version relationship retained.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank must be able to show the plan a borrower had before and after the rate change, and how the two are related.

## Example

Rahim's plan v2 (15%) replaces v1 (14%). v1 stays, marked "replaced by v2, repricing run RP-2027-01".

## Terms to know

- **Schedule version:** one state of the repayment plan. See `glossary.schedule-version`.
- **Version relationship:** the link from the old plan to the plan that replaced it.
- **Retained:** the earlier plan is not deleted or overwritten, so it can still be opened.
- **Repricing run:** the batch that changed the rate, named on the new version as the reason.
