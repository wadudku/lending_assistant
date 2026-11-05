---
id: concept.BR-LMS-196
type: concept
title: Freezing a loan
summary: "Some events stop normal processing, such as a borrower's death or a court order. The platform records the freeze and unfreeze dates, exactly what was stopped, and who authorised it."
br_ids: [BR-LMS-196]
brd_section: 7.10
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-196"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-196"
  - "sources/verification/verification_report.md#BR-LMS-196"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-196"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-196"
related: [bridge.BR-LMS-196, brd_section.7.10, glossary.maker-checker, decision.freeze, lifecycle.FROZEN]
version: 1
status: approved
approved_by: Owner
---
**In short:** Some events stop normal processing, such as a borrower's death or a court order. The platform records the freeze and unfreeze dates, exactly what was stopped, and who authorised it.

## What the rule says

BR-LMS-196 in section 7.10 (Must, BRD PDF page 54) says authorised freeze and unfreeze periods shall be recorded, with the processing suspended during the freeze stated explicitly and the authorising approval retained.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that stopping interest and bills on a loan is a decision with legal and money effects, so the bank must show who agreed, from when, and what stopped.

## Example

Rahim dies on 15 August. The loan is frozen from 15 August: no interest and no bills, authorised by the Head of Legal.

## Terms to know

- **Freeze:** suspending a loan's normal processing for a period.
- **Unfreeze:** ending the suspension.
- **Authorising approval:** the record of who allowed it. See `glossary.maker-checker`.
