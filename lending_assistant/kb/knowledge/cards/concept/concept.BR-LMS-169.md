---
id: concept.BR-LMS-169
type: concept
title: Fix wrong payment postings safely
summary: "When payments were posted wrongly, they are reprocessed through a controlled, approved, restartable repost that keeps the original entries."
br_ids: [BR-LMS-169]
brd_section: 7.7
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-169"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-169"
  - "sources/verification/verification_report.md#BR-LMS-169"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-169"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-169"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-009"
related: [bridge.BR-LMS-169]
version: 1
status: approved
approved_by: Owner
---
**In short:** When payments were posted wrongly, they are reprocessed through a controlled, approved, restartable repost that keeps the original entries.

## What the rule says

BR-LMS-169 (Must, BRD 7.7.1, PDF page 51) says that where a correction is required, repayment postings are reprocessed through a controlled, resumable, approved repost that retains the original entries.

## Why the bank wants it

The BRD gives the reason in two guiding principles. Repayment, schedule and accounting histories are immutable, and a correction is a controlled reversal and re-entry that preserves the original, never a silent amendment or deletion (BR-GOV-009, PDF page 19). Every corrective posting needs maker-checker approval by two different users (BR-GOV-008, PDF page 19). The BRD doesn't say why the repost must be resumable; the usual reason is that a large repost can run for a long time and must survive a failure without starting again.

## Example

A payment was applied with the wrong value date. The repost redoes the split from 5 July onward. The old entries remain, marked as reversed, next to the new ones.

## Terms to know

- **Repost:** redoing postings from a date, keeping the old entries.
- **Reversal:** an entry that cancels an earlier one without erasing it.
- **Maker-checker:** one person prepares, another approves.
- **Resumable:** a stopped job continues instead of starting again.
