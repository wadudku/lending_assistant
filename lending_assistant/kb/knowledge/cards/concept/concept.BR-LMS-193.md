---
id: concept.BR-LMS-193
type: concept
title: Set money aside for expected losses (provisioning)
summary: "The platform works out how much the bank must set aside against loans that may not be repaid. The rate depends on the grade and on whether the loan is secured, semi-secured or unsecured, and the basis of each calculation is kept."
br_ids: [BR-LMS-193]
brd_section: 7.10
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-193"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-193"
  - "sources/verification/verification_report.md#BR-LMS-193"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-193"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-193"
related: [bridge.BR-LMS-193, brd_section.7.10, glossary.provisioning, glossary.irac, concept.BR-LMS-191]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform works out how much the bank must set aside against loans that may not be repaid. The rate depends on the grade and on whether the loan is secured, semi-secured or unsecured, and the basis of each calculation is kept.

## What the rule says

BR-LMS-193 in section 7.10 (Must, BRD PDF page 54) says the platform shall calculate provisions by classification and by secured, semi-secured and unsecured status, using configurable percentages. It shall retain the calculation basis for every provisioning run.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a regulator requires banks to hold a reserve against bad loans, and the bank must be able to show how each reserve figure was reached.

## Example

Rahim's unsecured loan is graded SS with 92,172 outstanding. At 20%, the bank sets aside 18,434.

## Terms to know

- **Provision:** money set aside against a loan that may not be repaid. See `glossary.provisioning`.
- **IRAC:** the regulator's rules on recognising income and grading loans. See `glossary.irac`.
- **Basis:** the balance, grade, rate and date a provision was worked out from.
