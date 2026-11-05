---
id: concept.BR-INT-052
type: concept
title: "A failed notification is retried and reported, and never blocks a loan action"
summary: "A failed notification is retried and reported, and never blocks or reverses a loan action."
br_ids: [BR-INT-052]
brd_section: 9.7
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-052"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [bridge.BR-INT-052]
version: 1
status: approved
approved_by: Owner
---
**In short:** A failed notification is retried and reported, and never blocks or reverses a loan action.

## What the rule says

BR-INT-052 (Must, BRD 9.7, PDF page 65) says notification failure is retried and reported. It never blocks or reverses a loan action. The inventory in 9.1 marks the SMS gateway “non-blocking for notices” (PDF page 60), which is the same idea from the other side: a notice that cannot be sent must not stop the work.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a message is only a courtesy to the borrower, and a loan payout or repayment should not be undone because an SMS could not be sent.

## Example

A payout goes through, but the SMS gateway is down. The payout stays. The message is retried later, and the failure appears in a report for the operations team.

## Terms to know

- **Retried:** sent again after a failure.
- **Reversal:** undoing an action already done.
