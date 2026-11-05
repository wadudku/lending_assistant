---
id: glossary.sma
type: glossary
title: SMA (special mention account)
summary: An early-warning grade for a loan that is late but not yet non-performing.
br_ids: [BR-LMS-191]
brd_section: 7.10
doctypes: [Loan]
dev_items: []
terms: [sma, special mention account, early-warning class]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
related: [glossary.asset-classification, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** An early-warning grade for a loan that is late but not yet non-performing.

## Plain meaning

The BRD defines SMA as a special mention account, an early-warning asset category preceding stronger non-performing classifications (BRD 1.5). The plain-English guide describes it as late, but not yet NPA, and gives example bands of 60 to 89 days past due.

## Example

In the guide's example bands, Rahim's loan at 65 days past due is SMA. At 90 days it would move on to Sub-Standard, the first non-performing class. The bank sets the real bands; they are configurable.

## Why it matters here

BR-LMS-191 asks for the grade from configured DPD bands, so the band limits are the bank's choice. See `lifecycle.SMA` for the BRD state against Frappe Lending.

## See also

`glossary.asset-classification`, `glossary.dpd`, `glossary.ss`.
