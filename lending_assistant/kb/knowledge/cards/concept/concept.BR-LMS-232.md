---
id: concept.BR-LMS-232
type: concept
title: Release collateral at closure
summary: "At closure, collateral is released after approval, and the release is recorded in the collateral ledger."
br_ids: [BR-LMS-232]
brd_section: 7.14
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-232"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-232"
  - "sources/verification/verification_report.md#BR-LMS-232"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-232"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-232"
related: [bridge.BR-LMS-232, brd_section.7.14, glossary.fd-fdr, glossary.maker-checker, concept.BR-LMS-230]
version: 1
status: approved
approved_by: Owner
---
**In short:** At closure, collateral is released after approval, and the release is recorded in the collateral ledger.

## What the rule says

BR-LMS-232 in section 7.14 (Must, BRD PDF page 56) says eligible collateral shall be released after approval, and the release recorded in the security ledger.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank must hand the borrower's asset back only when it is entitled to, and must be able to show later what was released, when and on whose say.

## Example

FDR-001 is released to Rahim on 5 June 2027, approved by the branch manager. The release is entered in the security ledger with that date, and the loan's closure date stays as it was, because the release does not change the date on which the loan was paid off.

## Terms to know

- **Collateral release:** giving a pledged asset back to the borrower. See `glossary.fd-fdr` for fixed deposits.
- **Approval:** a person with authority agrees to the release.
- **Security ledger:** the dated record of what was pledged and what was released.
