---
id: concept.BR-LMS-133
type: concept
title: Never delete or quietly change a bill
summary: "A bill is never silently deleted or changed. A correction is a controlled reversal with a reason and an approver, and the original and the reversal both stay visible."
br_ids: [BR-LMS-133]
brd_section: 7.4
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-133"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-133"
  - "sources/verification/verification_report.md#BR-LMS-133"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-133"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-133"
related: [bridge.BR-LMS-133, brd_section.7.4, devitem.D8, glossary.demand, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** A bill is never silently deleted or changed. A correction is a controlled reversal with a reason and an approver, and the original and the reversal both stay visible.

## What the rule says

BR-LMS-133 (priority Must, BRD 7.4, PDF page 48) says a demand is never silently deleted or amended. A correction is made through a controlled reversal entry with a reason and an approver, and both the original and the reversal remain visible.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bill drives lateness, penalty and the loan's grade, so erasing one would also erase a borrower's record of delinquency without anyone being responsible. This follows the BRD's principle that every posting traces to an approved event (BRD 7 opening, PDF page 46).

## Example

A late fee of 500 was charged twice. The fix is a reversal of -500 with the reason "charged twice", approved by the branch manager. The wrong 500 still shows in the history, next to its reversal.

## Terms to know

- **Reversal:** a new entry that cancels an earlier one, instead of deleting it.
- **Approver:** the second person who accepts the correction. See `glossary.maker-checker`.
- **Demand:** see `glossary.demand`.
