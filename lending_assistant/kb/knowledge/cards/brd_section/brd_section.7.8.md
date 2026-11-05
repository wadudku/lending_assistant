---
id: brd_section.7.8
type: brd_section
title: BRD 7.8 Collateral and security servicing
summary: "Section 7.8 says collateral must be recorded, valued, watched for shortfall and released only after checks and approval."
br_ids: []
brd_section: 7.8
doctypes: []
dev_items: [D20]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.8"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.8-collateral-and-security-servicing"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.8-collateral-and-security-servicing"
  - "sources/verification/reqs.json#BR-LMS-172"
related: [devitem.D20, glossary.ltv, lifecycle.CLOSED]
version: 2
status: approved
approved_by: Owner
---
**In short:** Section 7.8 says collateral must be recorded, valued, watched for shortfall and released only after checks and approval.

## What this section says

BRD 7.8 (PDF pages 52 and 53, 6 requirements, BR-LMS-170 to BR-LMS-175) covers servicing of the security behind a loan. There is a security master with type, description, valuation, price history, haircut and eligible value (170). A pledge moves from requested to pledged, then to release requested and then released, repossessed or cancelled, and each step is authorised and recorded (171). Shortfall is monitored by comparing eligible collateral with secured exposure, on a schedule and on demand (172). Remediation is tracked with an owner and a due date (173). Security is released only after exposure validation and approval (174). Exposure and event reports are produced (175). BR-LMS-170 and 171 share their numbers with two repayment requirements in 7.7.1, so this card calls the collateral ones 170c and 171c.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that collateral is what the bank falls back on if the borrower cannot pay, so its value must stay current and a release must be checked against what is still owed. BR-LMS-174 states the release rule itself (PDF page 52).

## How it meets Frappe Lending

Of the 6 requirements, the verified result on 16.5.1 is 1 covered (175); 5 partly covered (170c, 171c, 172, 173, 174). Verification moved 4 of these verdicts: 170c, 171c, 172, 174. Dev item: D20 (small items), which covers BR-LMS-173.

## Related cards

Dev item: `devitem.D20`. Terms: `glossary.ltv`. States that end with a release: `lifecycle.CLOSED`.
