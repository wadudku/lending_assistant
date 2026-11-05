---
id: glossary.npa
type: glossary
title: NPA (non-performing asset)
summary: "A loan that has become a bad loan: overdue beyond the bank's limit, so its unpaid interest stops counting as income."
br_ids: [BR-LMS-144]
brd_section: 7.10
doctypes: [Loan]
dev_items: []
terms: [npa, non-performing asset, non performing loan, bad loan]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-144"
related: [lifecycle.NPA, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** A loan that has become a bad loan: overdue beyond the bank's limit, so its unpaid interest stops counting as income.

## Plain meaning

The BRD defines NPA as non-performing asset (BRD 1.5). The plain-English guide calls it a bad loan, overdue past the NPA limit (for example 90 days past due), whose unpaid interest goes to suspense.

## Example

Rahim's instalments are unpaid for 100 days and the product's NPA limit is 90. The loan is classed non-performing, and the bank moves his unpaid interest to suspense.

## Why it matters here

BR-LMS-144 asks for income to stop and qualifying interest to move to suspense. See `lifecycle.NPA` for how the BRD state compares with the NPA flag in Frappe Lending.

## See also

`lifecycle.NPA`, `glossary.income-suspense`, `glossary.dpd`.
