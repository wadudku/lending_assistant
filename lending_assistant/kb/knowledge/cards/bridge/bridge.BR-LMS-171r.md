---
id: bridge.BR-LMS-171r
type: bridge
title: Match every payment end to end
summary: "Gap (needs the CBS link). There is no end-to-end payment match report, and the unique CBS reference it would rely on is not enforced."
br_ids: [BR-LMS-171]
brd_section: 7.7
doctypes: [Loan Repayment]
verdict: gap_cbs
analysis_status: verified
dev_items: [D10]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-171r"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-171r"
  - "sources/verification/verification_report.md#BR-LMS-171r"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-171"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-171"
related: [concept.BR-LMS-171r, bridge.BR-LMS-170r, devitem.D13, bridge.BR-LMS-162]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap (needs the CBS link). There is no end-to-end payment match report, and the unique CBS reference it would rely on is not enforced.

## Business need

Every repayment must reconcile against its CBS reference, its allocation and its accounting posting, with unmatched items reported (BR-LMS-171 in section 7.7, BRD PDF page 51). See `concept.BR-LMS-171r`. The collateral requirement with the same number, in section 7.8, has its own card.

## Frappe Lending today

No end-to-end payment match report exists in 16.5.1 (checked from the installed metadata). The pieces to compare do exist in separate places: the repayment, its Repayment Details and its accounting entries.

## Match or gap, and why

This is a **gap (needs the CBS link)**. Without a CBS feed there is nothing to compare the repayment to. Two facts from the verification make a future report harder. Repayments post their accounting entries on the day of entry, while their value dates can be weeks earlier, so a match must use value date and reference together. References are also not unique (`bridge.BR-LMS-162`). The same dating problem affects disbursements, interest accruals (the daily interest bookings) and bills (demands), so a period-end reconciliation shows income and receivables in the wrong month (ND-12).

## What to do today

Reconcile by hand from the CBS statement, using the value date and the reference, never the accounting date. Keep a record of breaks and who cleared them.

## Planned fix

D10 (reconciliation reports) adds a repayment-versus-CBS-reference report, and unmatched items become exceptions. It needs the CBS feed (D13, `devitem.D13`) and the accounting-date fix ND-12, which lists this requirement.
