---
id: brd_section.9.1
type: brd_section
title: BRD 9.1 Integration inventory
summary: "Section 9.1 is a table of five outside parties the platform depends on, how each is reached, what it is for and how critical it is."
br_ids: []
brd_section: 9.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p60"
related: [brd_section.9, brd_section.9.2, brd_section.7, glossary.cbs, glossary.rpa, glossary.cib, glossary.ecdb]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 9.1 is a table of five outside parties the platform depends on, how each is reached, what it is for and how critical it is.

## What this section says

BRD 9.1 (PDF page 60) is a table of five counterparties. The Core Banking System is reached by robotic process automation, for account enquiry and title check, loan account opening, disbursement, accounting event posting, statement and balance retrieval and closure verification; it is blocking, with no submission, no funding and no servicing posting without it. The Credit Information Bureau is reached by robotic process automation, for borrower credit history inquiry from a designated host; blocking, with no approval without it. The Election Commission Database is reached by a service interface, for identity verification and portrait retrieval on every submitted application; blocking at verification. The SMS gateway is reached by a service interface, for one-time passcode delivery and borrower notification; blocking for login and non-blocking for notices. The collection channel is “to be determined with the Bank”, for direct debit or automated collection initiation and result where available; non-blocking in Phase 1. The section holds no requirement row.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank wants to see in one place which outside systems the platform cannot work without, and which can fail without stopping the work.

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section was not analysed, so the team makes no statement about it. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.9`. Next: `brd_section.9.2`. Terms: `glossary.cbs`, `glossary.rpa`.
