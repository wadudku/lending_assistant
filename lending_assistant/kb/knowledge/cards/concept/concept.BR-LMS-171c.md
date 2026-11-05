---
id: concept.BR-LMS-171c
type: concept
title: The life of a pledge
summary: "A pledge moves through set steps from pledge requested to pledged, then release requested and released, repossessed or cancelled, and every step is authorised and recorded."
br_ids: [BR-LMS-171]
brd_section: 7.8
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-171c"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-171c"
  - "sources/verification/verification_report.md#BR-LMS-171c"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-171"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-171"
related: [bridge.BR-LMS-171c, brd_section.7.8, concept.BR-LMS-171r, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** A pledge moves through set steps from pledge requested to pledged, then release requested and released, repossessed or cancelled, and every step is authorised and recorded.

## What the rule says

BR-LMS-171 in section 7.8 (Must, BRD PDF page 52) says the pledge lifecycle runs from pledge requested to pledged, then release requested and then released, repossessed or cancelled. Each transition must be authorised and recorded. The BRD uses the number 171 twice. This is the collateral one (card suffix c). The other, in section 7.7, is about matching every payment end to end (`concept.BR-LMS-171r`).

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a pledge changes what the bank can claim, so each change needs a named approver and a trace that an auditor can follow.

## Example

On 5 June, FDR-001 is requested as security and then pledged. On 5 June of the next year, Rahim repays in full, the release is requested, and the security is released.

## Terms to know

- **Pledge:** the borrower puts a security at the bank's disposal for a loan.
- **Release:** the bank gives the security back.
- **Repossession:** the bank takes the security because the borrower has not paid.
- **Authorised:** approved by someone allowed to do so. See `glossary.maker-checker`.
