---
id: concept.BR-LMS-117
type: concept
title: "Product rules have versions, start dates and approval"
summary: "Product rules must never change silently. Each change gets a version and a start date and needs a second person to approve it, and each loan remembers the version it was booked under."
br_ids: [BR-LMS-117]
brd_section: 7.2
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-117"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-117"
  - "sources/verification/verification_report.md#BR-LMS-117"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-117"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-117"
related: [bridge.BR-LMS-117, brd_section.7.2, devitem.D5, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** Product rules must never change silently. Each change gets a version and a start date and needs a second person to approve it, and each loan remembers the version it was booked under.

## What the rule says

BR-LMS-117 (priority Must, BRD 7.2, PDF page 47) says all product configuration is versioned and effective-dated under maker-checker. Every loan records the configuration version under which it was booked and the version under which each later event was processed.

## Why the bank wants it

The BRD gives the aim in its opening for 7.2: products can be introduced or amended by authorised business users under maker-checker without a software release (PDF page 46). Section 7 also says every posting must trace to an approved event and a rule version (PDF page 46). A rule change that is not versioned or approved would break that trace.

## Example

The penalty rate moves from 12% to 18% from 1 January 2027, approved by a checker. Rahim's loan shows "booked under version 3 (12%)", and January's penalty shows "processed under version 4 (18%)".

## Terms to know

- **Version:** a numbered state of the product's rules.
- **Effective date:** the day a change starts to apply.
- **Maker-checker:** one person prepares, another approves. See `glossary.maker-checker`.
- **Configuration version on events:** the version stamped on each bill, accrual or payment.
