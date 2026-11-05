---
id: concept.BR-INT-005
type: concept
title: Every instruction carries a unique reference the bank's record keeps
summary: "Every instruction carries a platform-made unique reference written into a durable field of the core banking system record, so the platform can later tell whether it ran."
br_ids: [BR-INT-005]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-005"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [bridge.BR-INT-005, concept.BR-GOV-002, glossary.cbs, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every instruction carries a platform-made unique reference written into a durable field of the core banking system record, so the platform can later tell whether it ran.

## What the rule says

BR-INT-005 (Must, BRD 9.2.1, PDF page 61) says every instruction carries a platform-generated unique reference. It is written into a durable field of the core banking system record, such as narration or reference or an equivalent, agreed with the bank.

## Why the bank wants it

The BRD gives the reason in the row: “so that the platform can later determine whether its own instruction executed” (PDF page 61).

## Example

The platform sends a payout with the reference K-001, written into the narration of the transaction. Later the reply is lost. The platform looks in the core banking system for K-001; if it finds the payout, it knows the instruction ran.

## Terms to know

- **Unique reference:** a label no other instruction has.
- **Durable field:** a field whose content stays on the record and can be read later.
- **Narration:** the free-text line on a bank transaction.
