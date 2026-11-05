---
id: concept.BR-LMS-231
type: concept
title: Check the core bank before confirming closure
summary: "When the core banking system (CBS) keeps the books, the loan system checks the loan account and ledger in the CBS before it confirms the closure."
br_ids: [BR-LMS-231]
brd_section: 7.14
doctypes: []
verdict: gap_cbs
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-231"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-231"
  - "sources/verification/verification_report.md#BR-LMS-231"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-231"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-231"
related: [bridge.BR-LMS-231, brd_section.7.14, glossary.cbs, concept.BR-LMS-230]
version: 1
status: approved
approved_by: Owner
---
**In short:** When the core banking system (CBS) keeps the books, the loan system checks the loan account and ledger in the CBS before it confirms the closure.

## What the rule says

BR-LMS-231 in section 7.14 (Must, BRD PDF page 56) says that where the Core Banking System owns the books, the platform shall verify the external account and ledger position before closure is confirmed.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that if the CBS holds the ledger, a loan that shows 0 owed here can still be owing there, and closing it on one side only leaves the two out of step.

## Example

The loan system says 0 is owed, and the CBS loan account must also show 0. If it shows 44, the closure waits.

## Terms to know

- **Core Banking System (CBS):** the bank's main ledger. See `glossary.cbs`.
- **External position:** the balance the CBS holds for the same loan.
- **Confirmed:** the closure is final in the loan system.
