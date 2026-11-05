---
id: glossary.income-suspense
type: glossary
title: Income suspense
summary: A ledger treatment that stops counting certain unpaid interest as normal earnings. It waits in a holding account until the money is actually recovered.
br_ids: [BR-LMS-144, BR-LMS-194]
brd_section: 7.5
doctypes: [Loan]
dev_items: []
terms: [income suspense, suspense, interest in suspense]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-144"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-194"
related: [lifecycle.NPA]
version: 1
status: approved
approved_by: Owner
---
**In short:** A ledger treatment that stops counting certain unpaid interest as normal earnings. It waits in a holding account until the money is actually recovered.

## Plain meaning

The BRD defines income suspense as a ledger treatment that stops recognising certain unpaid income as normal earnings (BRD 1.5). The interest is still owed, but the bank does not show it as profit yet.

## Example

Rahim's loan becomes non-performing with 4,000 of interest unpaid. The 4,000 is moved to a suspense account. If Rahim later pays it, the 4,000 moves back to income.

## Why it matters here

BR-LMS-144 asks that normal income stops and qualifying unpaid interest and charges move to suspense in line with Bangladesh Bank rules. BR-LMS-194 asks that they return to income only on actual recovery. See `lifecycle.NPA` for what Frappe Lending does.

## See also

`lifecycle.NPA`, `glossary.npa`.
