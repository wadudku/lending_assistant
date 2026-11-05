---
id: glossary.posting-date
type: glossary
title: Posting date
summary: The day an entry was recorded in the loan system. It can be later than the day the money moved.
br_ids: []
brd_section: 1.5
doctypes: [Loan Repayment]
dev_items: []
terms: [posting date, entry date]
fields: [Loan Repayment.Posting Date]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:120"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#words-that-appear-everywhere-in-section-7"
  - "sources/verification/reqs.json#BR-LMS-160"
related: [glossary.value-date, concept.BR-LMS-160]
version: 1
status: approved
approved_by: Owner
---
**In short:** The day an entry was recorded in the loan system. It can be later than the day the money moved.

## Plain meaning

The posting date is the date an accounting or business entry is recorded in the loan system (BRD 1.5). It is about bookkeeping, not about when the borrower paid.

## Example

Rahim paid on 5 July and staff entered it on 6 July. The posting date is 6 July and the value date is 5 July.

## Why it matters here

In Frappe Lending the **Posting Date** of a **Loan Repayment** is set by the system to the current time whenever the document is validated (a Data Import skips this), so users cannot back-date it. The accounting entries carry that date (see `bridge.BR-LMS-160`).

## See also

`glossary.value-date`, `concept.BR-LMS-160`.
