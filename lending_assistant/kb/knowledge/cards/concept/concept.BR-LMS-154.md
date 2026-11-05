---
id: concept.BR-LMS-154
type: concept
title: A practice run first
summary: "Before a repricing is run for real, a dry run shows each loan's old and new figures, every failure and every excluded loan with its reason."
br_ids: [BR-LMS-154]
brd_section: 7.6
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-154"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-154"
  - "sources/verification/verification_report.md#BR-LMS-154"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-154"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-154"
related: [bridge.BR-LMS-154, brd_section.7.6, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** Before a repricing is run for real, a dry run shows each loan's old and new figures, every failure and every excluded loan with its reason.

## What the rule says

BR-LMS-154 (priority Must, BRD 7.6, PDF page 50) says a dry run is produced before execution. It shows, per loan, the old and new rate, instalment, tenor and total interest, together with every validation failure and every excluded loan with its exclusion reason.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bulk change cannot easily be undone, so people need to see its effect on every loan before anything is changed.

## Example

"5,000 selected: 4,920 OK; 80 left out (52 fixed rate, 20 frozen, 8 closed)." Staff review the list before running it for real.

## Terms to know

- **Dry run:** a trial that shows the result and changes nothing.
- **Validation failure:** a loan that cannot be processed, with the reason.
- **Exclusion reason:** why a loan was left out.
