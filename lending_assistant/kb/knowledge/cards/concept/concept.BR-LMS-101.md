---
id: concept.BR-LMS-101
type: concept
title: One record holds everything about a loan
summary: "Every loan has one place where staff can find the borrower, product, terms, balances, repayment plan, bills, payments, accounting entries, grade and history."
br_ids: [BR-LMS-101]
brd_section: 7.1
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-101"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-101"
  - "sources/verification/verification_report.md#BR-LMS-101"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-101"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-101"
related: [bridge.BR-LMS-101, brd_section.7.1, glossary.demand, glossary.asset-classification, lifecycle.ACTIVE]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every loan has one place where staff can find the borrower, product, terms, balances, repayment plan, bills, payments, accounting entries, grade and history.

## What the rule says

BR-LMS-101 (priority Must, BRD 7.1, PDF page 46) says the LMS is the servicing system of record for every funded loan. In one retrievable record it holds the borrower, the product, the terms, the balances, the repayment schedule, the demands (the bills raised), the postings, the classification (the health grade) and the history.

## Why the bank wants it

The BRD does not give a reason inside BR-LMS-101. The opening of BRD Section 7 states the principle behind it: the loan book must be correct, explicable and reproducible, and every balance must be traceable to a posting (PDF page 46). One record per loan is how a user can follow a balance back to what caused it without asking another system.

## Example

A staff member opens Rahim's loan. On the one record they see his EMI plan, the 3 bills raised so far, the 2 payments he made, the accounting entries and his current grade (Standard). They do not open another system to answer a question from Rahim.

## Terms to know

- **System of record:** the one place whose figures count as the truth for the loan.
- **Demand:** a bill raised for an amount due on a date. See `glossary.demand`.
- **Classification:** the loan's health grade, such as Standard or NPA. See `glossary.asset-classification`.
- **Posting:** an accounting entry made for a loan event.
