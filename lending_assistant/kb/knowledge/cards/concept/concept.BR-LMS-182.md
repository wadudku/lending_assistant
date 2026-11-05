---
id: concept.BR-LMS-182
type: concept
title: Changing the terms for a struggling borrower (restructuring)
summary: "The platform can change the terms of a loan for a borrower who cannot keep up, by moving dates or the term or by changing the money terms, and it records what kind of change it was."
br_ids: [BR-LMS-182]
brd_section: 7.9
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-182"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-182"
  - "sources/verification/verification_report.md#BR-LMS-182"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-182"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-182"
related: [bridge.BR-LMS-182, brd_section.7.9, glossary.restructuring, glossary.rescheduling, decision.restructure]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform can change the terms of a loan for a borrower who cannot keep up, by moving dates or the term or by changing the money terms, and it records what kind of change it was.

## What the rule says

BR-LMS-182 in section 7.9 (Must, BRD PDF page 53) says the platform shall support loan restructuring. That includes rescheduling of dates and tenor and broader modification of financial terms, with the restructure type recorded.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a restructure changes a loan the bank has already approved, so the bank and the regulator need to know which kind of change it was.

## Example

Rahim's income drops. The loan is extended from 12 to 18 months and the EMI falls. The record says "Reschedule".

## Terms to know

- **Restructuring:** changing a loan's terms. See `glossary.restructuring`.
- **Rescheduling:** moving dates or the term only. See `glossary.rescheduling`.
- **Restructure type:** the label that records which kind of change it was.
