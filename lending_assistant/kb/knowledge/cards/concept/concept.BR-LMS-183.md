---
id: concept.BR-LMS-183
type: concept
title: A restructure makes a new plan and keeps the old one
summary: "A restructure produces a new repayment plan, and the old plan is kept and marked as restructured and replaced."
br_ids: [BR-LMS-183]
brd_section: 7.9
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-183"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-183"
  - "sources/verification/verification_report.md#BR-LMS-183"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-183"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-183"
related: [bridge.BR-LMS-183, brd_section.7.9, glossary.schedule-version, concept.BR-LMS-182]
version: 1
status: approved
approved_by: Owner
---
**In short:** A restructure produces a new repayment plan, and the old plan is kept and marked as restructured and replaced.

## What the rule says

BR-LMS-183 in section 7.9 (Must, BRD PDF page 53) says restructuring shall generate a new schedule and preserve the prior schedule as restructured and superseded.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank must be able to show what the borrower owed under the old terms and what changed.

## Example

Plan version 1 (12 months) is kept as "Restructured". Plan version 2 (18 months) is now the active one. Later an auditor asks what Rahim owed under the old terms. The bank opens version 1 and answers from it, even though version 2 is the plan now in force.

## Terms to know

- **Schedule version:** one numbered repayment plan for a loan. See `glossary.schedule-version`.
- **Superseded:** replaced by a newer version but still on record.
- **Active:** the one plan that the loan is now following.
