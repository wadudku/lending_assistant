---
id: concept.BR-INT-063
type: concept
title: Every automated transaction can be traced to who caused it
summary: Every automated transaction is attributable to the user or process that started it; the audit trail records both that actor and the service account used.
br_ids: [BR-INT-063]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-063"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-063, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every automated transaction is attributable to the user or process that started it; the audit trail records both that actor and the service account used.

## What the rule says

BR-INT-063 (Must, BRD 9.3, PDF page 63) says every automated transaction is attributable to the platform user or system process that started it. The audit trail records both the initiating actor and the service account used.

## Why the bank wants it

The BRD gives the reason in the row: “so that a Core Banking System entry made by the service account can always be traced to the person or process that caused it” (PDF page 63).

## Example

The core banking system shows a payout made by the service account. The platform's audit trail shows that the officer Rahim approved it at 10:42 and that the service account carried it out. The two together answer who caused the entry.

## Terms to know

- **Attributable:** can be linked to a named person or process.
- **Initiating actor:** the user or process that started the action.
- **Audit trail:** the record of who did what and when.
