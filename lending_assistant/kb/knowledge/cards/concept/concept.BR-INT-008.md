---
id: concept.BR-INT-008
type: concept
title: Raise a controlled reversal of an earlier transaction
summary: "The platform can raise a controlled reversal of a prior transaction, keeping the original, recording the new reference, and handing a task to a human authoriser where the bank needs one."
br_ids: [BR-INT-008]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-INT-008, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform can raise a controlled reversal of a prior transaction, keeping the original, recording the new reference, and handing a task to a human authoriser where the bank needs one.

## What the rule says

BR-INT-008 (Must, BRD 9.2.1, PDF page 62) says the platform can raise a controlled reversal of a prior transaction. It preserves the original event and records the new reference the core banking system returns. Where the core banking system needs a human authoriser for a reversal, the platform raises the reversal as a task with its full supporting detail and records the outcome.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a wrong posting must be undone by a new, visible entry and not by erasing the old one, so the history stays complete.

## Example

A payout of 100,000 was posted twice. The platform raises a reversal of the second one. The core banking system needs an officer to authorise it, so a task is created with the loan, the two references and the reason. The officer authorises it, and the platform records the new reference.

## Terms to know

- **Reversal:** a new entry that cancels an earlier one.
- **Authoriser:** a person who approves an action in the core banking system.
