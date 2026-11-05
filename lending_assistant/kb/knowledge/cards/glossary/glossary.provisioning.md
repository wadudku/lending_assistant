---
id: glossary.provisioning
type: glossary
title: Provisioning
summary: "Money the bank sets aside against expected loan losses, based on a loan's class and how well it is secured."
br_ids: [BR-LMS-193]
brd_section: 7.10
doctypes: [Loan]
dev_items: []
terms: [provisioning, provision, loan loss provision]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-193"
related: [glossary.asset-classification, devitem.D14]
version: 1
status: approved
approved_by: Owner
---
**In short:** Money the bank sets aside against expected loan losses, based on a loan's class and how well it is secured.

## Plain meaning

The BRD defines provisioning as the expense or reserve recognised against expected loss, based on classification and security (BRD 1.5).

## Example

Rahim's loan is graded Sub-Standard and has little collateral. The bank applies the rate for that class and security type to the amount at risk and books the result as a provision.

## Why it matters here

BR-LMS-193 asks for provisions by class and by secured, semi-secured or unsecured status, with configurable percentages and the basis kept for each run. The verified result is a gap: Frappe Lending has the rate table and nothing that calculates or stores provisions.

## See also

`devitem.D14`, `glossary.asset-classification`.
