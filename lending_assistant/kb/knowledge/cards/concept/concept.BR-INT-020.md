---
id: concept.BR-INT-020
type: concept
title: The handoff to servicing carries the full package and is idempotent
summary: The handoff of a confirmed funded loan from origination to servicing carries the complete package specified in BR-LOS-010 and is idempotent.
br_ids: [BR-INT-020]
brd_section: 9.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-020"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-020, glossary.los, glossary.lms, glossary.idempotency, concept.BR-LOS-010]
version: 1
status: approved
approved_by: Owner
---
**In short:** The handoff of a confirmed funded loan from origination to servicing carries the complete package specified in BR-LOS-010 and is idempotent.

## What the rule says

BR-INT-020 (Must, BRD 9.4, PDF page 64) says the handoff of a confirmed funded loan from origination to servicing carries the complete package specified in BR-LOS-010, and is idempotent.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that servicing can only run a loan correctly if it receives everything it needs once, and a repeated handoff must not create the loan twice.

## Example

Origination hands over a funded loan with its terms, borrower, account and payout details. The message is sent twice because of a network fault. Servicing ends up with one loan, not two.

## Terms to know

- **Handoff:** passing a funded loan from origination to servicing.
- **Package:** the set of data the BRD lists as required for the handoff.
- **Idempotent:** a repeat has no second effect. See `glossary.idempotency`.
