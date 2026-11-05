---
id: concept.BR-LMS-123
type: concept
title: Keep a partner's plan for co-lent loans
summary: "When a loan is co-lent, the system keeps a second repayment plan for the partner's share, alongside the borrower's plan."
br_ids: [BR-LMS-123]
brd_section: 7.3
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-123"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-123"
  - "sources/verification/verification_report.md#BR-LMS-123"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-123"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-123"
related: [bridge.BR-LMS-123, brd_section.7.3, glossary.partner, concept.BR-LMS-116]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a loan is co-lent, the system keeps a second repayment plan for the partner's share, alongside the borrower's plan.

## What the rule says

BR-LMS-123 (priority Must, BRD 7.3, PDF page 48) says that where a loan is co-lent, the schedule is split according to the partner's agreed economics, and a partner schedule is maintained alongside the borrower schedule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the partner is owed its own share of principal and interest on each date, which is different from what the borrower pays the bank.

## Example

Rahim's EMI is 8,979. The partner funded 80%, so a partner schedule shows its own principal and interest share for each month.

## Terms to know

- **Co-lending:** two lenders fund one loan.
- **Partner schedule:** the plan of what the partner receives.
- **Borrower schedule:** the plan of what the borrower pays. See `glossary.partner`.
