---
id: concept.BR-GOV-010
type: concept
title: Four kinds of date are kept apart and never mixed
summary: "Effective date, posting date, value date and the system timestamp are recorded as four different things and are never treated as one."
br_ids: [BR-GOV-010]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-GOV-010, glossary.effective-date, glossary.posting-date, glossary.value-date]
version: 1
status: approved
approved_by: Owner
---
**In short:** Effective date, posting date, value date and the system timestamp are recorded as four different things and are never treated as one.

## What the rule says

BR-GOV-010 (Must, BRD 3.4, PDF page 19) says effective date, posting date, value date and system timestamp are recorded and used as distinct concepts, and are never conflated.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a payment can take effect on one day, be entered on another, and earn interest from a third, and mixing them gives wrong interest and wrong reports.

## Example

A customer pays on the 28th but the clerk enters it on the 30th. The value date is the 28th (interest stops from then), the posting date is the 30th (when it enters the books), and the system timestamp is the exact moment it was typed in.

## Terms to know

- **Effective date:** the date a change takes effect. See `glossary.effective-date`.
- **Posting date:** the date an entry is recorded in the books. See `glossary.posting-date`.
- **Value date:** the date from which interest counts. See `glossary.value-date`.
- **System timestamp:** the exact time the system saved the record.
