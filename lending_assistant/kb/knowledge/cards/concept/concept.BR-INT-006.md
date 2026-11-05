---
id: concept.BR-INT-006
type: concept
title: A compensating control stands in for idempotency
summary: "Because the core banking system cannot recognise a repeated instruction, the platform checks the state first, runs the instruction with its reference, verifies afterwards and blocks on any doubt."
br_ids: [BR-INT-006]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-INT-006, concept.BR-GOV-002, glossary.cbs, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Because the core banking system cannot recognise a repeated instruction, the platform checks the state first, runs the instruction with its reference, verifies afterwards and blocks on any doubt.

## What the rule says

BR-INT-006 (Must, BRD 9.2.1, PDF page 62) says the platform implements a compensating control agreed with the bank: a state query before execution, execution carrying the unique reference, a verification after execution, and a blocking exception on any ambiguity. The control is documented and tested as a risk mitigation and is not represented as equivalent to transactional idempotency.

## Why the bank wants it

The BRD gives the reason at the start of the row: “Because the Core Banking System does not support idempotency natively” (PDF page 62). Section 9.2 adds that this is “a mitigation, not an equivalent” (PDF page 61).

## Example

Before paying out, the platform asks whether the reference K-002 already exists; it does not. It sends the payout with K-002, then reads the record back and finds K-002 with the right amount. If the read-back showed a different amount, the loan would be blocked as an exception.

## Terms to know

- **Idempotency:** an instruction run twice has the effect of running once. See `glossary.idempotency`.
- **Compensating control:** a set of checks that makes up for something the system lacks.
- **Blocking exception:** an exception that stops the step until it is resolved.
