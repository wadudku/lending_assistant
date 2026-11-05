---
id: concept.BR-LOS-122
type: concept
title: One account number can have only one open application anywhere
summary: "An account number may hold only one non-terminal application across the whole platform, whichever partner sent it."
br_ids: [BR-LOS-122]
brd_section: 6.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-122"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-116"
related: [bridge.BR-LOS-122, concept.BR-LOS-116]
version: 1
status: approved
approved_by: Owner
---
**In short:** An account number may hold only one non-terminal application across the whole platform, whichever partner sent it.

## What the rule says

BR-LOS-122 (Must, BRD 6.3, PDF page 32) says one account number holds only one non-terminal application platform-wide. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a payout goes to one account, and two open applications for the same account could each lead to a payout. BRD 6.2.1 handles the same match when a file is uploaded.

## Example

Partner A has an open application for account 1234. Partner B uploads a row with the same account number. The second application is not accepted until the first one is finished or closed.

## Terms to know

- **Non-terminal:** still open; not yet finished or closed.
- **Platform-wide:** across all partners, not only one.
- **Account number:** the number of the borrower's bank account.
- **Duplicate:** a repeat of an earlier entry. See BR-LOS-116.
