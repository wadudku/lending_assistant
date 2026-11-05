---
id: concept.BR-GOV-003
type: concept
title: "After a failed call, ask the other system before retrying"
summary: "When a call to an outside system fails or times out, the platform does not guess what happened; it asks that system for the real state before any retry or status change."
br_ids: [BR-GOV-003]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-GOV-003, glossary.cbs, glossary.idempotency, concept.BR-GOV-002]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a call to an outside system fails or times out, the platform does not guess what happened; it asks that system for the real state before any retry or status change.

## What the rule says

BR-GOV-003 (Must, BRD 3.4, PDF page 19) says that where a call to an external system fails or times out, the platform does not infer an outcome. It queries the external system for the definitive state before any retry or status change. The BRD adds: “Absence of a response is not a response.” BRD 3.4 lists it among the guiding principles that are binding on the design.

## Why the bank wants it

The BRD doesn't say why in this row. The nearby rules explain the risk: the CBS cannot recognise a repeated instruction by itself, so a blind retry of a payout that actually went through could pay twice (BR-GOV-002 and BR-INT-006, PDF pages 19 and 62).

## Example

The platform sends a payout instruction and gets no reply. It does not mark the payout failed, and it does not send it again. It first asks the bank's core system whether that instruction was carried out, and acts on the answer.

## Terms to know

- **Timeout:** waiting longer than allowed without getting an answer.
- **Definitive state:** the confirmed outcome as recorded by the other system, not a guess.
- **Retry:** sending the same instruction again.
- **External system:** any system outside the platform, such as the CBS.
