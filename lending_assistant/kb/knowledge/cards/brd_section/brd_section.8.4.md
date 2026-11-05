---
id: brd_section.8.4
type: brd_section
title: BRD 8.4 Reconciliation
summary: "Section 8.4 asks for a daily comparison with the core banking system, ownership and documented closure of every difference, an internal consistency check and an audit trail."
br_ids: []
brd_section: 8.4
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#8.4"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p59"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-050"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-051"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-052"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-053"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-054"
related: [brd_section.8, brd_section.7, glossary.cbs, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 8.4 asks for a daily comparison with the core banking system, ownership and documented closure of every difference, an internal consistency check and an audit trail.

## What this section says

BRD 8.4 (PDF page 59) has 5 requirements, all Must. BR-GOV-050: a daily reconciliation of the platform's application and loan status against the Core Banking System, for every post-approval record, with an exception report. BR-GOV-051: five kinds of difference it must find, from loans booked externally to orphaned idempotency keys. BR-GOV-052: each break has an owner and a documented closure, and open breaks age visibly and are reported to management. BR-GOV-053: internal reconciliation across schedule, demand, accrual, repayment allocation and accounting posting. BR-GOV-054: every run and closure record kept in the immutable audit trail.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the platform and the core banking system each hold part of the record, so the bank wants differences found daily and closed with a reason.

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section holds 5 requirement rows and none was analysed, so the team makes no statement about them. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.8`. Terms: `glossary.cbs`, `glossary.idempotency`.
