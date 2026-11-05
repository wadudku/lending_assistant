---
id: glossary.asset-classification
type: glossary
title: Asset classification (loan grade)
summary: "The risk category a loan is placed in, worked out from days past due and, where the bank wishes, a person's judgement."
br_ids: [BR-LMS-191]
brd_section: 7.10
doctypes: [Loan]
dev_items: []
terms: [asset classification, classification, loan grade, health grade]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
  - "sources/verification/reqs.json#BR-LMS-191"
related: [glossary.dpd, lifecycle.NPA, devitem.D15]
version: 1
status: approved
approved_by: Owner
---
**In short:** The risk category a loan is placed in, worked out from days past due and, where the bank wishes, a person's judgement.

## Plain meaning

The BRD defines asset classification as the risk category assigned to a loan using days past due together with qualitative assessment (BRD 1.5). The plain-English guide gives example bands: Standard 0 to 59 days, SMA 60 to 89, Sub-Standard 90 to 179.

## Example

Rahim's instalment is 65 days late. Under the guide's example bands he falls in the SMA band. A credit officer may add a reason and an approver to override the grade by hand.

## Why it matters here

BR-LMS-191 asks for a grade from DPD bands plus a qualitative override with a reason and an approver. The verified result is partly covered: Frappe Lending grades loans by band, but the only override is the Manual NPA tick, with no reason or approver.

## See also

`glossary.dpd`, `lifecycle.NPA`, `devitem.D15`.
