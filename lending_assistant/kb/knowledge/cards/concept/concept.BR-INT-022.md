---
id: concept.BR-INT-022
type: concept
title: A failed handoff stops both sides until the exception is closed
summary: "A failed or rejected handoff raises an exception on both sides, and neither side progresses the loan until the exception is closed."
br_ids: [BR-INT-022]
brd_section: 9.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-022"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-022, glossary.los, glossary.lms]
version: 1
status: approved
approved_by: Owner
---
**In short:** A failed or rejected handoff raises an exception on both sides, and neither side progresses the loan until the exception is closed.

## What the rule says

BR-INT-022 (Must, BRD 9.4, PDF page 64) says a failed or rejected handoff raises an exception on both sides, and neither side progresses the loan until the exception is closed. It sits with the other two rows of 9.4: BR-INT-020 asks for a complete, idempotent package, and BR-INT-021 asks for loan status to flow back to origination. Together the three describe the connection between the two systems.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that if one side moves on while the other holds a failed handoff, the two systems disagree about the loan.

## Example

Servicing rejects a handoff because the product code is unknown. Both origination and servicing show an exception for that loan. Neither pays out or bills it until someone fixes the code and closes the exception.

## Terms to know

- **Exception:** a flagged problem that a person must resolve.
- **Rejected handoff:** one the receiving side refuses.
