---
id: concept.BR-LMS-191
type: concept
title: Give each loan a health grade
summary: "Each loan gets a grade from how many days late it is, and an authorised person can override the grade by hand, with a reason and an approver."
br_ids: [BR-LMS-191]
brd_section: 7.10
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-191"
  - "sources/verification/verification_report.md#BR-LMS-191"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-191"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-191"
related: [bridge.BR-LMS-191, brd_section.7.10, glossary.asset-classification, glossary.sma, glossary.maker-checker, decision.override]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each loan gets a grade from how many days late it is, and an authorised person can override the grade by hand, with a reason and an approver.

## What the rule says

BR-LMS-191 in section 7.10 (Must, BRD PDF page 53) says the platform shall assign an asset classification using configured days-past-due bands. It shall also be able to record a qualitative override with a reason and an approver.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a pure day count can miss a loan that is already bad for another reason, such as a bankruptcy, and the bank wants the override to be a decision someone is accountable for.

## Example

At 60 days late Rahim's loan becomes SMA (early warning). Credit Risk moves another borrower straight to SS because he declared bankruptcy, recording the reason and the approver.

## Terms to know

- **Asset classification (grade):** the loan's health class. See `glossary.asset-classification`.
- **Band:** a range of days past due that maps to a grade, for example SMA from 60 to 89 days. See `glossary.sma`.
- **Override:** a person's decision that replaces the grade the bands would give.
- **Maker-checker:** one person proposes, another approves. See `glossary.maker-checker`.
