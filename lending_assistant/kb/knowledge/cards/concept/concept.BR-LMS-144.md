---
id: concept.BR-LMS-144
type: concept
title: Stop counting interest as income on bad loans
summary: "When a loan becomes non-performing, interest and charges that are unpaid stop counting as income and move to a suspense account."
br_ids: [BR-LMS-144]
brd_section: 7.5
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-144"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-144"
  - "sources/verification/verification_report.md#BR-LMS-144"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-144"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-144"
related: [bridge.BR-LMS-144, brd_section.7.5, glossary.npa, glossary.income-suspense, glossary.asset-classification, lifecycle.NPA]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a loan becomes non-performing, interest and charges that are unpaid stop counting as income and move to a suspense account.

## What the rule says

BR-LMS-144 (priority Must, BRD 7.5, PDF page 49) says that on non-performing classification the platform applies the required income treatment. It stops normal income recognition and moves qualifying unpaid interest and charges to suspense, in accordance with Bangladesh Bank rules.

## Why the bank wants it

The BRD gives the reason in the rule: the treatment follows Bangladesh Bank rules (BR-LMS-144, PDF page 49). In plain words, interest a borrower has not paid on a bad loan cannot be shown as the bank's profit.

## Example

Rahim is 91 days late and owes 3,300 of interest he has not paid. That 3,300 moves out of income into suspense, so the bank's profit drops by 3,300 until he actually pays.

## Terms to know

- **NPA (non-performing asset):** a loan whose payments are seriously late. See `glossary.npa`.
- **Income suspense:** a holding account for unpaid interest that is not counted as income. See `glossary.income-suspense`.
- **Classification:** the loan's health grade. See `glossary.asset-classification`.
