---
id: concept.BR-LMS-001
type: concept
title: "A loan has exactly one current status, with its full history"
summary: "Every loan has exactly one current servicing status at a time, and the platform keeps the whole history of earlier statuses with the date and reason for each change."
br_ids: [BR-LMS-001]
brd_section: 5.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
related: [bridge.BR-LMS-001, brd_section.5.3, lifecycle.ACTIVE, lifecycle.OVERDUE, lifecycle.NPA, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every loan has exactly one current servicing status at a time, and the platform keeps the whole history of earlier statuses with the date and reason for each change.

## What the rule says

BR-LMS-001 (Must, BRD 5.3, PDF page 27) says the LMS maintains exactly one current servicing status for every loan, and retains the full history of prior statuses with the date and reason for each transition. BRD 5.3 names twelve states: BOOKED, ACTIVE, PARTIALLY_DISBURSED, OVERDUE, SMA, NPA, RESTRUCTURED, FROZEN, CLOSURE_REQUESTED, CLOSED, SETTLED and WRITTEN_OFF.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that collections, finance, risk and the regulator all ask what state a loan is in and how it got there, and one status with its history gives a single answer and an audit trail. See `brd_section.5.3`.

## Example

A loan is ACTIVE, then misses a payment and becomes OVERDUE, then is paid up and returns to ACTIVE. At every moment there is exactly one current status, and the history shows the three periods with the date and reason for each change.

## Terms to know

- **Servicing status:** the state of a loan while the bank is looking after it. See `lifecycle.OVERDUE` and `lifecycle.NPA` for two of them.
- **Transition:** a change from one status to another.
- **Status history:** the list of earlier statuses with date and reason.
