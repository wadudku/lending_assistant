---
id: concept.BR-LMS-143
type: concept
title: "Undo and redo interest for a period, with approval"
summary: "Where a correction is needed, interest for a date range can be reversed and posted again for many loans, with approval, and the reversed entries stay visible."
br_ids: [BR-LMS-143]
brd_section: 7.5
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-143"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-143"
  - "sources/verification/verification_report.md#BR-LMS-143"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-143"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-143"
related: [bridge.BR-LMS-143, brd_section.7.5, glossary.batch, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** Where a correction is needed, interest for a date range can be reversed and posted again for many loans, with approval, and the reversed entries stay visible.

## What the rule says

BR-LMS-143 (priority Must, BRD 7.5, PDF page 49) says that where a correction is required, the platform supports an approved batch reversal and repost of accruals across a specified date range, retaining the reversed entries.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a wrong rate or a missed run affects many loans at once, and the fix has to leave a record of what was wrong and who approved the correction.

## Example

The rate was set to 15% instead of 14% from 1 to 31 August for 200 loans. August's interest is reversed and re-posted at 14%. The wrong entries remain, marked as reversed.

## Terms to know

- **Reversal:** a new entry that cancels an earlier one.
- **Repost:** calculating and posting the entries again.
- **Batch:** many loans in one run. See `glossary.batch`.
- **Approval:** a second person accepts the correction. See `glossary.maker-checker`.
