---
id: concept.BR-LMS-106
type: concept
title: Each loan has a category for reports
summary: "Every loan carries a label such as Retail, SME or Agriculture so that management and regulatory reports can group loans."
br_ids: [BR-LMS-106]
brd_section: 7.1
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-106"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-106"
  - "sources/verification/verification_report.md#BR-LMS-106"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-106"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-106"
related: [bridge.BR-LMS-106, brd_section.7.1, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every loan carries a label such as Retail, SME or Agriculture so that management and regulatory reports can group loans.

## What the rule says

BR-LMS-106 (priority Must, BRD 7.1, PDF page 46) says each loan carries a reporting and servicing category. The category supports portfolio segmentation (splitting the loan book into groups) for management reports and for regulatory reports.

## Why the bank wants it

The BRD gives the reason in the rule: the category supports portfolio segmentation for management and regulatory reporting (BR-LMS-106, PDF page 46). In plain words, a question about one part of the book can only be answered if every loan says which part it belongs to.

## Example

A manager asks: "How much of our SME lending is more than 60 days late?" The answer is possible only if every loan carries a category, so SME loans can be separated from Retail ones.

## Terms to know

- **Category:** a label on the loan, such as Retail, SME or Agriculture.
- **Portfolio segmentation:** splitting the loan book into groups to measure each one.
- **Days past due:** how late a payment is. See `glossary.dpd`.
