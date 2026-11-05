---
id: concept.BR-INT-065
type: concept
title: On an unexpected screen the automation stops safely
summary: "Before entering any value the automation checks it is on the screen it is meant to see; on anything unexpected it aborts the transaction safely, raises an exception and stops."
br_ids: [BR-INT-065]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-065"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-065, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Before entering any value the automation checks it is on the screen it is meant to see; on anything unexpected it aborts the transaction safely, raises an exception and stops.

## What the rule says

BR-INT-065 (Must, BRD 9.3, PDF page 63) says the automation validates that each screen it reaches is the screen it expected, before it enters any value. On an unexpected screen, an unexpected message or a changed field layout it aborts the transaction safely, raises an exception and stops, and does not carry on assuming.

## Why the bank wants it

The BRD gives the reason in section 9.2: “A field moved, a screen reordered, a new warning dialogue or a changed menu path can stop the automation.” (PDF page 61).

## Example

The automation expects the payout screen but a new warning dialogue appears. It does not type the amount. It cancels the transaction, raises an exception with a note of what it saw, and stops.

## Terms to know

- **Abort safely:** stop without leaving a half-finished transaction.
- **Field layout:** where each input sits on a screen.
