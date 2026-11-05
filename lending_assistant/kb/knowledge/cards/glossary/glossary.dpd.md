---
id: glossary.dpd
type: glossary
title: DPD (days past due)
summary: How many days an amount has been overdue. It drives the loan's grade and whether it becomes a non-performing loan.
br_ids: []
brd_section: 1.5
doctypes: [Loan, Days Past Due Log]
dev_items: []
terms: [dpd, days past due, days late]
fields: [Loan.Days Past Due, Days Past Due Log.Days Past Due]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/verification/reqs.json#BR-LMS-190"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-190"
  - "sources/verification/verification_report.md#BR-LMS-163"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
related: [lifecycle.OVERDUE, lifecycle.NPA]
version: 1
status: approved
approved_by: Owner
---
**In short:** How many days an amount has been overdue. It drives the loan's grade and whether it becomes a non-performing loan.

## Plain meaning

DPD means days past due: the number of days an amount has remained overdue (BRD 1.5). A loan paid on time has 0.

## Example

Rahim's instalment was due on 5 July and is still unpaid on 12 July. In the verified tests the due date counts as day 1, so the loan shows 8 days past due on 12 July.

## Why it matters here

DPD decides the health grade and when a loan becomes NPA (BR-LMS-190, BR-LMS-191). Frappe Lending keeps the current value in the **Days Past Due** field of the **Loan**, and one row a day in the **Days Past Due Log**. See `lifecycle.OVERDUE`.

## See also

`lifecycle.OVERDUE`, `lifecycle.NPA`, `concept.BR-LMS-163`.
