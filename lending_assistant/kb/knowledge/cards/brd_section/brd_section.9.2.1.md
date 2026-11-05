---
id: brd_section.9.2.1
type: brd_section
title: BRD 9.2.1 Core Banking System operations
summary: "Section 9.2.1 lists 12 operations the platform performs on the core banking system, from account enquiry and loan account opening to a single adapter."
br_ids: []
brd_section: 9.2.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.2.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-005"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-007"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-009"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-011"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-012"
related: [brd_section.9.2, brd_section.9, brd_section.7, glossary.cbs, glossary.rpa, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 9.2.1 lists 12 operations the platform performs on the core banking system, from account enquiry and loan account opening to a single adapter.

## What this section says

BRD 9.2.1 (PDF pages 61 and 62) has 12 requirements, BR-INT-001 to BR-INT-012, all Must. 001 account enquiry; 002 queued enquiry at an agreed rate; 003 opening a loan account; 004 disbursement; 005 a unique reference in a durable field; 006 the compensating control for idempotency; 007 recording accounting effects; 008 controlled reversal; 009 retrieving statement, balance and status; 010 re-reading the state before any retry; 011 logging every interaction with customer content masked; 012 reaching the core banking system through a single adapter.

## Why the bank wants it

The BRD gives its reason in 9.2: there is no interface, so the platform must do these things by driving the system's screens (PDF page 60). Rows 005, 006, 009 and 012 also state a reason of their own.

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section holds 12 requirement rows and none was analysed, so the team makes no statement about them. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.9.2`. Terms: `glossary.cbs`, `glossary.rpa`, `glossary.idempotency`.
