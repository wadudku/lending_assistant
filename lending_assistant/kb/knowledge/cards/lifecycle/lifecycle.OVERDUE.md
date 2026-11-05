---
id: lifecycle.OVERDUE
type: lifecycle
title: Loan state OVERDUE
summary: "In the BRD, OVERDUE is a loan state. In Frappe Lending it is not a status: a loan is overdue when its Days Past Due is above zero."
br_ids: []
brd_section: 5.3
doctypes: [Loan, Days Past Due Log]
dev_items: [D2]
lifecycle_state: OVERDUE
fields: [Loan.Days Past Due, Loan.Status, Days Past Due Log.Days Past Due]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1213"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-190"
  - "sources/verification/verification_report.md#BR-LMS-190"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-001"
related: [brd_section.5.3, lifecycle.NPA, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** In the BRD, OVERDUE is a loan state. In Frappe Lending it is not a status: a loan is overdue when its Days Past Due is above zero.

## The BRD state

BRD 5.3 (PDF page 27) defines OVERDUE as: one or more demands are unpaid beyond their due date, and days past due (DPD) are accruing. A demand is the bill raised on a due date. The BRD wants exactly one current status for every loan (BR-LMS-001), and OVERDUE is one of the twelve.

## The Frappe Lending equivalent

There is no OVERDUE status. The loan's **Status** stays, for example, Disbursed. The signal is the **Days Past Due** field on the **Loan**, which is above zero, and the **Days Past Due Log**, which holds one row for each day. This was verified live: a daily classification run wrote one log row per day with no gaps, and the due date counts as day 1. Value-dated repayments rewrite the log from the value date, so the history is replayed rather than frozen.

## Why they differ

Frappe Lending thinks in one status plus attributes. A loan can be Disbursed, overdue, NPA and frozen at once, which is closer to real life but gives no single label. The BRD asks for exactly one state with history. The team's proposal (D2) keeps Frappe's own status untouched and adds a Servicing Status field, worked out in a fixed priority order. In that order OVERDUE ranks below, among others, FROZEN, NPA, SMA and RESTRUCTURED, so a late loan reads OVERDUE only while none of the higher states applies.

## How a loan enters and leaves it

A loan enters OVERDUE when a demand is unpaid after its due date and the classification run sets Days Past Due above zero. It leaves when the overdue amounts are paid and the run sets it back to zero. Payment with an earlier value date rewrites the past. Beyond OVERDUE, the grade moves as DPD grows: SMA, then NPA (see `lifecycle.NPA`).
