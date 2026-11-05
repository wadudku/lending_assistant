---
id: concept.BR-LOS-204
type: concept
title: Before any retry the platform checks what really happened and never pays twice
summary: "Before a retry the platform re-reads the core banking system for the definitive state, never retries after an interrupted session, and records success without a second instruction if the first had executed."
br_ids: [BR-LOS-204]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-204"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [bridge.BR-LOS-204, glossary.idempotency, glossary.rpa, concept.BR-LOS-203]
version: 1
status: approved
approved_by: Owner
---
**In short:** Before a retry the platform re-reads the core banking system for the definitive state, never retries after an interrupted session, and records success without a second instruction if the first had executed.

## What the rule says

BR-LOS-204 (Must, BRD 6.9, PDF page 43) says "Before any retry the platform shall re-read the Core Banking System to establish the definitive state of the instruction." It "shall never retry on the basis of an incomplete or interrupted automation session". "Where an interrupted instruction is found to have executed, success shall be recorded without issuing a second instruction." So there are three rules: re-read before a retry, no retry from an interrupted session, and no second instruction when the first had executed.

## Why the bank wants it

The BRD gives the reason on PDF page 43: "The controlling risk is duplicate disbursement arising from an uncertain response to an instruction that has in fact already executed."

## Example

An automation session is interrupted during a disbursement and the platform is unsure what happened. Before doing anything else it re-reads the core banking system. The disbursement is found to have executed, so success is recorded and no second instruction is sent.

## Terms to know

- **Definitive state:** what the core banking system itself shows about the instruction, as the BRD puts it.
- **Interrupted session:** the BRD's term in "incomplete or interrupted automation session"; it does not define it.
