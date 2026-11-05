---
id: concept.BR-LMS-174
type: concept
title: Release collateral only after checks and approval
summary: Security may be given back only after the platform checks that the loan is still covered and someone approves the release.
br_ids: [BR-LMS-174]
brd_section: 7.8
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-174"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-174"
  - "sources/verification/verification_report.md#BR-LMS-174"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-174"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-174"
related: [bridge.BR-LMS-174, brd_section.7.8, glossary.maker-checker, glossary.ltv]
version: 1
status: approved
approved_by: Owner
---
**In short:** Security may be given back only after the platform checks that the loan is still covered and someone approves the release.

## What the rule says

BR-LMS-174 in section 7.8 (Must, BRD PDF page 52) says security shall be released only after exposure validation and approval.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that giving back collateral while money is still owed would leave the bank without the cover the loan was approved on.

## Example

Rahim asks for his fixed deposit back while 100,000 is still owed. The release is refused, because what is left would not cover the loan. If he asks only for the part the loan does not need, the request can go on to approval.

## Terms to know

- **Exposure validation:** checking that the loan is still covered after the release.
- **Release:** the bank gives the security back.
- **Approval:** a person with authority agrees to the release. See `glossary.maker-checker`.
