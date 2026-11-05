---
id: concept.BR-INT-064
type: concept
title: Each automation run keeps evidence of what it did
summary: "Each automation run keeps evidence of the screens traversed, the values entered and the values read back, enough to reconstruct the transaction for audit or dispute."
br_ids: [BR-INT-064]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-064"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-064, glossary.rpa, brd_section.4.3]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each automation run keeps evidence of the screens traversed, the values entered and the values read back, enough to reconstruct the transaction for audit or dispute.

## What the rule says

BR-INT-064 (Must, BRD 9.3, PDF page 63) says each automation run retains evidence of what it did: the screens traversed, the values entered and the values read back. The evidence is sufficient to reconstruct the transaction for audit or dispute, and sensitive content in it is protected under the access rules of Section 4.3.

## Why the bank wants it

The BRD gives the reason in the row: the evidence is “sufficient to reconstruct the transaction for audit or dispute” (PDF page 63).

## Example

A borrower disputes a payout. The stored evidence for that run shows each screen visited, the amount and account typed in, and the confirmation read back, so the bank can show exactly what was done.

## Terms to know

- **Evidence:** a stored record of what the automation saw and did.
- **Read back:** a value read from the screen after acting.
- **Dispute:** a challenge to a transaction by a borrower or other party.
