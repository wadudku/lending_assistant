---
id: concept.BR-LMS-220
type: concept
title: Move loans between branches in bulk
summary: "Loans can be moved from one branch to another in bulk, and each loan keeps its own record and its full history."
br_ids: [BR-LMS-220]
brd_section: 7.13
doctypes: []
verdict: covered
analysis_status: code_reading
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-220"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-220"
  - "sources/verification/verification_report.md#BR-LMS-220"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-220"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-220"
related: [bridge.BR-LMS-220, brd_section.7.13]
version: 1
status: approved
approved_by: Owner
---
**In short:** Loans can be moved from one branch to another in bulk, and each loan keeps its own record and its full history.

## What the rule says

BR-LMS-220 in section 7.13 (Must, BRD PDF page 55) says the platform shall support bulk transfer of servicing ownership between branches, preserving the same loan record and its complete history.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that branches open, close and merge, and the loans must follow without being re-created, so that every number, schedule and posting stays traceable.

## Example

The Uttara branch closes, so its 3,000 loans move to the Gulshan branch. Each loan keeps its number and its history.

## Terms to know

- **Servicing ownership:** which branch looks after the loan.
- **Bulk transfer:** many loans moved in one action.
- **Same record:** the loan keeps its name and number, and nothing is copied.
