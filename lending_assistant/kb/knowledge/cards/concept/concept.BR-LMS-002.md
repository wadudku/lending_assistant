---
id: concept.BR-LMS-002
type: concept
title: A status change never erases or overwrites earlier records
summary: "Changing a loan's status never deletes or overwrites an earlier classification, schedule version or posting; older records are kept and marked as superseded."
br_ids: [BR-LMS-002]
brd_section: 5.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-009"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-LMS-002, brd_section.5.3, glossary.schedule-version, glossary.asset-classification, concept.BR-GOV-009]
version: 1
status: approved
approved_by: Owner
---
**In short:** Changing a loan's status never deletes or overwrites an earlier classification, schedule version or posting; older records are kept and marked as superseded.

## What the rule says

BR-LMS-002 (Must, BRD 5.3, PDF page 28) says a status transition never deletes or overwrites a prior classification, schedule version or posting. Superseded records are retained and marked as superseded.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an audit must be able to see what was true before a change, and overwriting would destroy that. The same idea appears in BR-GOV-009 for repayment, schedule and accounting histories (PDF page 19).

## Example

A loan is restructured. The old schedule is not deleted. It is kept and marked as superseded, a new schedule becomes current, and the earlier classification stays on record next to the new one.

## Terms to know

- **Superseded:** replaced by a newer record but kept and marked as old.
- **Classification:** the grade a loan gets by how overdue it is. See `glossary.asset-classification`.
- **Schedule version:** one numbered copy of the instalment plan. See `glossary.schedule-version`.
- **Posting:** an entry in the books. See `glossary.posting-date`.
