---
id: concept.BR-LMS-151
type: concept
title: The new rate starts on a set date
summary: "A repricing takes effect on an approved date: the old rate applies up to it and the new rate from it."
br_ids: [BR-LMS-151]
brd_section: 7.6
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-151"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-151"
  - "sources/verification/verification_report.md#BR-LMS-151"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-151"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-151"
related: [bridge.BR-LMS-151, brd_section.7.6, glossary.repricing, glossary.effective-date]
version: 1
status: approved
approved_by: Owner
---
**In short:** A repricing takes effect on an approved date: the old rate applies up to it and the new rate from it.

## What the rule says

BR-LMS-151 (priority Must, BRD 7.6, PDF page 49) says repricing is effective-dated: the old rate applies through the prior period and the new rate from the approved effective date.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that interest already earned at the old rate must not be recalculated, and the borrower must be able to see on which day the new rate began.

## Example

The rate moves from 14% to 15% from 1 January 2027. December's interest stays at 14% and January's is worked out at 15%.

## Terms to know

- **Effective date:** the day a change starts to apply.
- **Prior period:** the time before the effective date, still at the old rate.
- **Accrual:** interest counted day by day; each day uses the rate in force on that day. See `glossary.effective-date`.
- **Repricing:** see `glossary.repricing`.
