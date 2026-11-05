---
id: concept.BR-GOV-054
type: concept
title: Reconciliation runs and closures are kept in the audit trail
summary: Every reconciliation run and every closure record is retained in the immutable audit trail.
br_ids: [BR-GOV-054]
brd_section: 8.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-054"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p59"
related: [bridge.BR-GOV-054]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every reconciliation run and every closure record is retained in the immutable audit trail.

## What the rule says

BR-GOV-054 (Must, BRD 8.4, PDF page 59) says every reconciliation run and every closure record is retained in the immutable audit trail.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an auditor needs to see that the checks were run and how each difference was resolved, and a trail that can be altered would not prove it.

## Example

An auditor asks to see the reconciliation of 14 March. The audit trail shows that the run took place, how many breaks it found and, for each, who closed it, when and with what note. None of those entries can be changed.

## Terms to know

- **Audit trail:** the record of who did what and when.
- **Immutable:** cannot be changed or deleted after it is written.
