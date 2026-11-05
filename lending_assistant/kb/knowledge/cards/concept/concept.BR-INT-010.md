---
id: concept.BR-INT-010
type: concept
title: "After a failure or odd result, read the real state before trying again"
summary: "Where an instruction fails, is interrupted or gives an unrecognised result, the platform re-reads the core banking system for the definitive state before any retry or status change."
br_ids: [BR-INT-010]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [bridge.BR-INT-010, concept.BR-GOV-002, glossary.cbs, glossary.idempotency, concept.BR-GOV-003]
version: 1
status: approved
approved_by: Owner
---
**In short:** Where an instruction fails, is interrupted or gives an unrecognised result, the platform re-reads the core banking system for the definitive state before any retry or status change.

## What the rule says

BR-INT-010 (Must, BRD 9.2.1, PDF page 62) says that where an instruction fails, is interrupted, or produces an unrecognised result, the platform re-reads the core banking system for the definitive state before any retry or status change. BR-GOV-003 (BRD 3.4, PDF page 19) is the same principle stated for every outside system.

## Why the bank wants it

The BRD gives the reason (BRD 9.2, PDF page 61): “The Core Banking System offers no idempotency key”, so the platform reads the state before and after acting and stops “on any ambiguity”.

## Example

A payout times out. The platform does not send it again. It reads the core banking system for the reference it used; the payout is there, so the platform records it as done. Only if the payout were absent would it try again.

## Terms to know

- **Definitive state:** what the core banking system shows really happened.
- **Retry:** sending an instruction again.
- **Unrecognised result:** a reply the platform does not understand.
