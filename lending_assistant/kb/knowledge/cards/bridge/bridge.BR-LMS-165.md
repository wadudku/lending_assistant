---
id: bridge.BR-LMS-165
type: bridge
title: All the payment types the bank needs
summary: "Covered. The Repayment Type list has 20 options, including every type the BRD names. Pre Payment and Advance Payment also reshape the schedule."
br_ids: [BR-LMS-165]
brd_section: 7.7
doctypes: [Loan Repayment]
verdict: covered
analysis_status: verified
dev_items: []
options: [Loan Repayment.Repayment Type=Normal Repayment, Loan Repayment.Repayment Type=Pre Payment, Loan Repayment.Repayment Type=Advance Payment, Loan Repayment.Repayment Type=Interest Waiver, Loan Repayment.Repayment Type=Subsidy Adjustments, Loan Repayment.Repayment Type=Write Off Recovery]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-165"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-165"
  - "sources/verification/verification_report.md#BR-LMS-165"
  - "sources/verification/verification_report.md#BR-LMS-180"
  - "sources/verification/verification_report.md#BR-LMS-183"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-165"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-165"
  - "sources/verification/analysis_corrections.md#5.-lifecycle-comparison"
related: [concept.BR-LMS-165, bridge.BR-LMS-162, decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The Repayment Type list has 20 options, including every type the BRD names. Pre Payment and Advance Payment also reshape the schedule.

## Business need

The loan system must support every kind of money movement the bank uses (BR-LMS-165, BRD 7.7.1, PDF page 51). See `concept.BR-LMS-165`.

## Frappe Lending today

The **Repayment Type** field on **Loan Repayment** is a list of 20 options: Normal Repayment, three waivers (Interest, Penalty, Charges), Principal Adjustment, Interest Carry Forward, Write Off Recovery, Security Deposit Adjustment, Advance Payment, Pre Payment, Subsidy Adjustments, Loan Closure, Partial Settlement, Full Settlement, Write Off Settlement, Charge Payment and four capitalisation types. The team read the list from the live form and used Normal Repayment and Pre Payment in tests.

## Match or gap, and why

This is **covered**. Each type the BRD names has a counterpart: advance and pre-payment, waiver, adjustment, capitalisation, settlement, subsidy and write-off recovery. The list has more types than the BRD names.

A caution for newcomers: Pre Payment and Advance Payment are not simple payments. In 16.5.1 they create and approve a Loan Restructure (a change of the loan's terms) automatically, and the old schedule becomes Rescheduled. That is why a duplicate Pre Payment is dangerous (see `bridge.BR-LMS-162`). Waivers and write-off treatment also need approvals that Frappe Lending does not enforce (see `decision.waiver`).

## What to do today

Pick the type by what really happened, not by what is easiest. Check the Repayment Details afterwards to see what the type did. Treat Pre Payment, Advance Payment and every waiver or settlement type as sensitive.

## Planned fix

None for the list itself. Approval control on waiver and settlement types is part of D8 (the approval and audit pack).
