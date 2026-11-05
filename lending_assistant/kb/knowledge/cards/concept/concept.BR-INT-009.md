---
id: concept.BR-INT-009
type: concept
title: "Retrieve statement, balance and loan account status from the core banking system"
summary: "The platform retrieves account statement, balance and loan account status, by a scheduled extract where live retrieval is impractical at volume."
br_ids: [BR-INT-009]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-009"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-INT-009, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform retrieves account statement, balance and loan account status, by a scheduled extract where live retrieval is impractical at volume.

## What the rule says

BR-INT-009 (Must, BRD 9.2.1, PDF page 62) says the platform retrieves the account statement, the balance and the loan account status. Where interactive retrieval is impractical at volume, a scheduled extract is agreed with the bank.

## Why the bank wants it

The BRD gives the reason in the row: the retrieval is “to support disbursed-account views, servicing reconciliation and closure verification” (PDF page 62).

## Example

Each night a scheduled extract brings the balance and status of every loan account. The next morning a servicing officer sees the disbursed account's balance, and the reconciliation compares it with the platform's figure.

## Terms to know

- **Statement:** the list of transactions on an account.
- **Scheduled extract:** a file produced at set times.
- **Interactive retrieval:** asking the system for each item at the moment it is needed.
