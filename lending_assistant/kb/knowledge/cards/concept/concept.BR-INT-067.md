---
id: concept.BR-INT-067
type: concept
title: "An operations view of automation work, with controlled retry, cancel and escalate"
summary: "The platform presents an operations view of pending, in progress, completed and failed automation transactions, where an item can be retried, cancelled or escalated under maker-checker."
br_ids: [BR-INT-067]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-067"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-067, glossary.rpa, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform presents an operations view of pending, in progress, completed and failed automation transactions, where an item can be retried, cancelled or escalated under maker-checker.

## What the rule says

BR-INT-067 (Must, BRD 9.3, PDF page 63) says the platform presents an automation operations view showing pending, in progress, completed and failed transactions. An individual item can be retried, cancelled or escalated, under maker-checker.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that operators need to see what is waiting or stuck and act on single items without touching the rest.

## Example

The view shows 40 pending, 3 in progress, 120 completed and 2 failed. An operator proposes a retry for one failed item; a second person approves it before it runs.

## Terms to know

- **Operations view:** a screen for the people who run the automation.
- **Escalate:** pass an item to a more senior person.
- **Maker-checker:** one person proposes and another approves. See `glossary.maker-checker`.
