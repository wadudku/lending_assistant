---
id: concept.BR-LMS-214
type: concept
title: Partner reports
summary: "Reports for each partner show the share paid out, the share collected, the share still owed, the late loans in the partner's portfolio and how much of the guarantee has been used."
br_ids: [BR-LMS-214]
brd_section: 7.12
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-214"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-214"
  - "sources/verification/verification_report.md#BR-LMS-214"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-214"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-214"
related: [bridge.BR-LMS-214, brd_section.7.12, glossary.partner, glossary.dpd, glossary.fldg, concept.BR-LMS-210]
version: 1
status: approved
approved_by: Owner
---
**In short:** Reports for each partner show the share paid out, the share collected, the share still owed, the late loans in the partner's portfolio and how much of the guarantee has been used.

## What the rule says

BR-LMS-214 in section 7.12 (Should, BRD PDF page 55) says partner economics shall be reportable: disbursed share, collected share, outstanding share, delinquency within the partner's portfolio and guarantee utilisation.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that each partner has a stake in the loans and a right to know how they are doing, and the bank has to answer the partner with figures.

## Example

ABC Finance: 50 million disbursed share, 3% of loans more than 30 days late, 20% of the guarantee used.

## Terms to know

- **Disbursed share:** the part of the lending that the partner funded.
- **Outstanding share:** the part of the partner's money still owed by borrowers.
- **Delinquency:** loans that are late. See `glossary.dpd`.
- **Guarantee utilisation:** how much of the first-loss cover has been drawn. See `glossary.fldg`.
