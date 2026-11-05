---
id: concept.BR-LOS-116
type: concept
title: "Duplicates are caught at three levels, each with its own treatment"
summary: "Duplicates are looked for within the uploaded batch, against the partner's earlier batches and across all partners, each treated differently."
br_ids: [BR-LOS-116]
brd_section: 6.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-116"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-113"
related: [bridge.BR-LOS-116, glossary.partner, glossary.batch, glossary.nid]
version: 1
status: approved
approved_by: Owner
---
**In short:** Duplicates are looked for within the uploaded batch, against the partner's earlier batches and across all partners, each treated differently.

## What the rule says

BR-LOS-116 (Must, BRD 6.2, PDF page 30) says duplicate detection operates at three scopes, each with its own treatment, set out in BRD 6.2.1. Within the uploaded batch (matched on NID, account number and mobile number), all matching rows are flagged and the partner resolves them before submission. Against the partner's earlier batches (NID, account number), the row is flagged, and blocked where an earlier application is still in a non-terminal status. Across all partners, platform-wide (NID, account number), it is blocked and referred to the Bank, and the other partner's identity is not disclosed. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason for the cross-partner case: two partners may legitimately hold a relationship with the same person, and telling Partner A that Partner B submitted the same person would leak commercially sensitive information. The platform blocks the second application with a neutral message and refers it to the Bank, which can see both sides (PDF page 30).

## Example

Partner B uploads a row whose NID already belongs to an open application from Partner A. Partner B sees only a neutral “cannot be accepted, referred to the Bank”. Partner A is not named. A Bank officer sees both and decides.

## Terms to know

- **NID:** the national identity number.
- **Scope:** how far the match is looked for: batch, partner or all partners.
- **Non-terminal:** still open; not yet finished or closed.
- **Referred to the Bank:** passed to Bank staff to decide.
