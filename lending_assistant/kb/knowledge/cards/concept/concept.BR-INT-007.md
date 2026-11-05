---
id: concept.BR-INT-007
type: concept
title: Post the accounting effects to the core banking system and keep the reference
summary: "The platform records approved demand, accrual, charge, restructure, settlement and write-off accounting effects in the core banking system and keeps the voucher or journal reference."
br_ids: [BR-INT-007]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-007"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-INT-007, glossary.cbs, glossary.batch]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform records approved demand, accrual, charge, restructure, settlement and write-off accounting effects in the core banking system and keeps the voucher or journal reference.

## What the rule says

BR-INT-007 (Must, BRD 9.2.1, PDF page 62) says the platform records six kinds of approved accounting effect into the core banking system: demand, accrual, charge, restructure, settlement and write-off. It does so individually or as an agreed batch, and keeps the resulting voucher or journal reference against the loan.

## Why the bank wants it

The BRD gives the reason in section 9.2, which says the core banking system has no interface: “There is therefore no transactional interface through which the platform can enquire on an account, open a loan account, disburse funds or post an accounting event.” (PDF page 60) Why the voucher or journal reference is kept is not given; the usual reason is that finance can then trace a loan event to its entry in the books.

## Example

At the end of the day the platform sends one batch holding the day's interest accruals and charges. The core banking system returns journal number J-8841 for the batch. The platform keeps J-8841 against each loan in the batch.

## Terms to know

- **Accrual:** interest counted day by day before it is billed.
- **Voucher or journal reference:** the number of the entry in the bank's books.
- **Batch:** many items sent together. See `glossary.batch`.
