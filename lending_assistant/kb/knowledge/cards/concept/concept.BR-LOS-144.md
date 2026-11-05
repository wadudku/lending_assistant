---
id: concept.BR-LOS-144
type: concept
title: "Only a supervisor can reverse a review decision, and the original stays visible"
summary: "A sampling decision can be reversed only by a supervisor, under maker-checker, with a reason, and the original decision stays visible in the audit trail next to the reversal."
br_ids: [BR-LOS-144]
brd_section: 6.5.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-144"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-141"
related: [bridge.BR-LOS-144, glossary.maker-checker, concept.BR-LOS-141, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** A sampling decision can be reversed only by a supervisor, under maker-checker, with a reason, and the original decision stays visible in the audit trail next to the reversal.

## What the rule says

BR-LOS-144 (Must, BRD 6.5.1, PDF page 37) says a sampling decision is reversible only by a supervisor, under maker-checker, with a reason recorded. The original decision remains visible in the audit trail alongside the reversal. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a reviewer's decision should not be undone quietly, and the history must show both the first decision and the change.

## Example

A reviewer rejects an application. A supervisor proposes to reverse it, with a reason; a second authorised person approves. The history shows the rejection and the reversal one after the other.

## Terms to know

- **Reversal:** undoing an earlier decision with a new entry.
- **Supervisor:** a senior staff member.
- **Maker-checker:** one person proposes and another approves. See `glossary.maker-checker`.
- **Audit trail:** the history of what was done and by whom.
