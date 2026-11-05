---
id: glossary.gl
type: glossary
title: GL (general ledger)
summary: "The bank's main accounting book, where the money effects of loan activity are recorded as debits and credits."
br_ids: []
brd_section: 1.5
doctypes: []
dev_items: []
terms: [gl, general ledger, ledger]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
related: [glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** The bank's main accounting book, where the money effects of loan activity are recorded as debits and credits.

## Plain meaning

The BRD defines GL as the general ledger (BRD 1.5). The plain-English guide calls it the main accounting book where postings land.

## Example

When Rahim's loan is paid out, the ledger records a debit on the loan account and a credit on the bank account.

## Why it matters here

Two ledgers matter here. The core banking system (the CBS) holds the bank's real accounts and GL. Frappe Lending posts to the ledger of the ERPNext company it runs on, and the verification says its accounting ties to that ledger.

## See also

`glossary.cbs`, `glossary.cr-dr`.
