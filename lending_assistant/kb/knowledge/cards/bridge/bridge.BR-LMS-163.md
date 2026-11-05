---
id: bridge.BR-LMS-163
type: bridge
title: Use the date the money actually arrived
summary: Covered. A back-dated repayment cancels penalty after the value date and rewrites the days-past-due history from that date.
br_ids: [BR-LMS-163]
brd_section: 7.7
doctypes: [Loan Repayment, Days Past Due Log]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Repayment.Value Date, Days Past Due Log.Days Past Due]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-163"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-163"
  - "sources/verification/verification_report.md#BR-LMS-163"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-163"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-163"
related: [concept.BR-LMS-163, bridge.BR-LMS-164, glossary.value-date, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A back-dated repayment cancels penalty after the value date and rewrites the days-past-due history from that date.

## Business need

A late-entered payment must be treated as if it arrived on its value date, with days past due, penalty and grade recalculated (BR-LMS-163, BRD 7.7.1, PDF page 51). See `concept.BR-LMS-163`.

## Frappe Lending today

**Loan Repayment** has a **Value Date**. When a repayment is entered with a value date in the past, Frappe Lending cancels the penalty that built up after that date (the penal accruals: the daily penalty amounts) and the penalty bills raised for it (Loan Demand records, the system's bills), and rebuilds the **Days Past Due Log** from the value date.

## Match or gap, and why

This is **covered**, and it was proved live. A loan had reached 8 days past due. A repayment entered later with an earlier value date cancelled all 7 penalty accruals and all 7 penalty bills, rewrote the log from the value date with 0 days past due, and set the loan back to 0.

Two limits are worth knowing. First, the result is only right if the payment is actually split to the overdue interest. With the site's own payment order, interest stayed unpaid and the days past due were rewritten as 1 to 121, which is the problem in `bridge.BR-LMS-164`. Second, the accounting entries are still dated with the day of entry, not the value date.

## What to do today

Always type the real arrival day into **Value Date**. After a back-dated entry, open the Days Past Due Log for the loan and check that it was rewritten as expected. Check the payment order first (see `bridge.BR-LMS-164`).

## Planned fix

None for this requirement. The payment-order problem is ND-10 in the verification report, and the accounting-date problem is ND-12.
