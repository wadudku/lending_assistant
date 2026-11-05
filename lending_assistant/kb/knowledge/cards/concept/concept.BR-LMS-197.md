---
id: concept.BR-LMS-197
type: concept
title: "Grade, provision and income rules are owned and versioned"
summary: "The rules for grade bands, provision percentages and income treatment belong to Credit Risk and Finance. They are versioned, dated and approved by a second person, and every grade or provision records which version of the rules it used."
br_ids: [BR-LMS-197]
brd_section: 7.10
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-197"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-197"
  - "sources/verification/verification_report.md#BR-LMS-197"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-197"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-197"
related: [bridge.BR-LMS-197, brd_section.7.10, glossary.maker-checker, glossary.income-suspense, concept.BR-LMS-191, concept.BR-LMS-193]
version: 1
status: approved
approved_by: Owner
---
**In short:** The rules for grade bands, provision percentages and income treatment belong to Credit Risk and Finance. They are versioned, dated and approved by a second person, and every grade or provision records which version of the rules it used.

## What the rule says

BR-LMS-197 in section 7.10 (Must, BRD PDF page 54) says classification bands, provisioning percentages and income-recognition rules shall be configuration owned by Credit Risk and Finance, versioned, effective-dated and subject to maker-checker. Every classification and provision shall record the rule version applied.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a change to the bands or rates changes every grade and every reserve, so the bank must control who can change them and be able to show which rules produced an old figure.

## Example

A loan is recorded as "graded under rule set 2026-v2 (SMA from 60 days)". When the rules change in 2027, the old grades still show 2026-v2.

## Terms to know

- **Versioned:** each change creates a new numbered set, and the old set stays.
- **Effective-dated:** a set has a start date.
- **Maker-checker:** one person proposes a change, another approves. See `glossary.maker-checker`.
- **Income-recognition rules:** when interest counts as income. See `glossary.income-suspense`.
