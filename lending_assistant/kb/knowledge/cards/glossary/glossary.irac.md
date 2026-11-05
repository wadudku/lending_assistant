---
id: glossary.irac
type: glossary
title: IRAC (income recognition and asset classification)
summary: An Indian rule set for when to count interest as income and how to grade loans. Frappe Lending uses this name for its provisioning table.
br_ids: [BR-LMS-193]
brd_section: 7.10
doctypes: [Loan]
dev_items: []
terms: [irac, rbi, irac provisioning table]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-193"
related: [glossary.provisioning, devitem.D14]
version: 1
status: approved
approved_by: Owner
---
**In short:** An Indian rule set for when to count interest as income and how to grade loans. Frappe Lending uses this name for its provisioning table.

## Plain meaning

The plain-English guide defines IRAC as the Indian (RBI) rule set for when to count interest as income and how to grade loans, and says Frappe uses this name for its provisioning table. It describes RBI, the Reserve Bank of India, as India's central bank, whose rules are the source of Frappe Lending's defaults.

## Example

When the team reads the provisioning rates in Frappe Lending, the table is called IRAC. It is a Frappe Lending name.

## Why it matters here

The verification found that only the rate table exists in Frappe Lending, and nothing calculates or stores provisions (BR-LMS-193). The planned provisioning item reads its rates from this table.

## See also

`glossary.provisioning`, `glossary.bb`, `devitem.D14`.
