---
id: glossary.value-date
type: glossary
title: Value date
summary: "The day the money really arrived, which is the date lateness and interest follow."
br_ids: []
brd_section: 1.5
doctypes: [Loan Repayment]
dev_items: []
terms: [value date, date of receipt]
fields: [Loan Repayment.Value Date]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#words-that-appear-everywhere-in-section-7"
  - "sources/verification/reqs.json#BR-LMS-160"
  - "sources/verification/reqs.json#BR-LMS-163"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-163"
related: [glossary.posting-date, concept.BR-LMS-163]
version: 2
status: approved
approved_by: Owner
---
**In short:** The day the money really arrived, which is the date lateness and interest follow.

## Plain meaning

The value date of a payment is the day the money actually reached the bank. The BRD defines it as the date on which the Core Banking System recognises the transaction (BRD 1.5).

## Example

Rahim pays at the branch on 5 July. Staff enter it on 12 July. The value date is 5 July. Days past due and penalty are counted as if the payment arrived on 5 July.

## Why it matters here

BR-LMS-163 says a payment is applied as at its value date. In Frappe Lending it is the **Value Date** field of **Loan Repayment**, and it is the only date the user can set (see `bridge.BR-LMS-163`).

## See also

`glossary.posting-date`, `concept.BR-LMS-163`, `concept.BR-LMS-160`.
