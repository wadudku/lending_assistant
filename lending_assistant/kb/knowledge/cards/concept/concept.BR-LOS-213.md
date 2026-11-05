---
id: concept.BR-LOS-213
type: concept
title: "An exceptions workspace lists every item needing action, with an owner, age and closure record"
summary: "An exceptions workspace lists every item that needs intervention, five kinds named by the BRD, each with an owner, an ageing indicator and a documented closure record."
br_ids: [BR-LOS-213]
brd_section: 6.10.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-213"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.1"
related: [bridge.BR-LOS-213, concept.BR-LOS-203, concept.BR-LOS-212]
version: 1
status: approved
approved_by: Owner
---
**In short:** An exceptions workspace lists every item that needs intervention, five kinds named by the BRD, each with an owner, an ageing indicator and a documented closure record.

## What the rule says

BR-LOS-213 (Must, BRD 6.10.1, PDF page 44) says the platform "shall present an exceptions workspace listing every item requiring intervention". The BRD names five kinds: booking failures, reconciliation breaks, stale validations, handoff rejections and system-flagged anomalies. Each item has "an owner, an ageing indicator and a documented closure record".

## Why the bank wants it

The BRD doesn't say why; the usual reason is that failed or unclear items would otherwise go unseen, and an owner, an age and a closure record show who is responsible and how long each has waited.

## Example

A handoff to servicing is rejected. The item appears in the exceptions workspace with an owner and an ageing indicator. When it is dealt with, a closure record is written.

## Terms to know

- **Ageing indicator:** the BRD's term for one of the three things each item has; it does not define it further.
- **Reconciliation break:** one of the five kinds of item the BRD lists; it does not define it.
