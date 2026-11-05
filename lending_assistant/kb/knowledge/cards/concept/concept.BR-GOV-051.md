---
id: concept.BR-GOV-051
type: concept
title: What the daily comparison must find
summary: "Reconciliation finds, as a minimum, five kinds of difference: loans booked outside the platform, loans approved but absent externally, amount mismatches, status divergence and orphaned idempotency keys."
br_ids: [BR-GOV-051]
brd_section: 8.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-051"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p59"
related: [bridge.BR-GOV-051, glossary.cbs, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Reconciliation finds, as a minimum, five kinds of difference: loans booked outside the platform, loans approved but absent externally, amount mismatches, status divergence and orphaned idempotency keys.

## What the rule says

BR-GOV-051 (Must, BRD 8.4, PDF page 59) says reconciliation identifies, at minimum, five kinds of difference: loans booked externally but not on the platform; loans approved on the platform but absent externally; amount mismatches; status divergence; and orphaned idempotency keys.

## Why the bank wants it

The BRD doesn't say why these five; the usual reason is that they are the ways two systems can fall out of step: a loan in one but not the other, a different amount, a different status, or an instruction whose outcome was never recorded. For the key, see BR-GOV-002 (PDF page 19).

## Example

One loan appears in the core banking system but not on the platform. Another is approved on the platform and has no account in the core banking system. A third has 100,000 on the platform and 110,000 in the core banking system. Each is listed under its kind.

## Terms to know

- **Booked externally:** created in the core banking system without going through the platform.
- **Amount mismatch:** the two systems hold different amounts for the same loan.
- **Status divergence:** the two systems hold different statuses for the same loan.
- **Orphaned idempotency key:** a unique key sent with an instruction that has no matching result. See `glossary.idempotency`.
