---
id: concept.BR-LOS-004
type: concept
title: Every status change leaves a permanent audit record
summary: "Each status change writes an audit record that cannot be altered and shows the application, old and new status, who or what made the change, when, and the reason."
br_ids: [BR-LOS-004]
brd_section: 5.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-001"
related: [bridge.BR-LOS-004, concept.BR-GOV-009, concept.BR-LOS-001]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each status change writes an audit record that cannot be altered and shows the application, old and new status, who or what made the change, when, and the reason.

## What the rule says

BR-LOS-004 (Must, BRD 5.2, PDF page 27) says every status change writes an immutable audit record capturing application reference, previous status, new status, actor identity or system process, timestamp, reason code where applicable and free-text reason where captured. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank must be able to show later who moved an application and why, and a record that can be edited would not prove that.

## Example

A reviewer moves an application from IN_SAMPLING to ADMIN_REJECTED with the reason code “documents unreadable”. The audit record holds the application number, both statuses, the reviewer's identity, the time and the reason. No one can edit it afterwards.

## Terms to know

- **Audit record:** a permanent entry that shows what happened, to what, by whom and when.
- **Immutable:** cannot be changed after it is written.
- **Actor:** the person or system process that made the change.
- **Reason code:** a short coded reason picked from a list.
