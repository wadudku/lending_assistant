---
id: concept.BR-LMS-121
type: concept
title: Each row shows the split
summary: "Every line of the repayment plan shows the instalment and how much of it is principal and how much is interest, with the balance left after it."
br_ids: [BR-LMS-121]
brd_section: 7.3
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-121"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-121"
  - "sources/verification/verification_report.md#BR-LMS-121"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-121"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-121"
related: [bridge.BR-LMS-121, brd_section.7.3, glossary.emi]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every line of the repayment plan shows the instalment and how much of it is principal and how much is interest, with the balance left after it.

## What the rule says

BR-LMS-121 (priority Must, BRD 7.3, PDF page 48) says each schedule line stores the instalment amount and its principal, interest and closing balance components.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the split is what lets staff and the borrower see how much of each payment reduces the debt and how much is the cost of borrowing, and what is still owed afterwards.

## Example

Row 1 of a plan: instalment 8,979, made up of 1,151 interest and 7,828 principal. The balance left is 92,172.

## Terms to know

- **Instalment:** the amount due on the row's date.
- **Closing balance:** the principal still owed after that row is paid.
- **Principal / interest:** the debt itself and the charge for borrowing it.
