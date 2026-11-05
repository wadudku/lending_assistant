---
id: bridge.BR-LMS-203
type: bridge
title: Money collected after a write-off
summary: "Covered. Write Off Recovery and Write Off Settlement are the only repayment types accepted on a written-off loan, apart from waivers the system creates, and the money is credited to a recovery account on the original loan. A recovery is not capped, and an amount beyond the open principal is booked as a new interest demand."
br_ids: [BR-LMS-203]
brd_section: 7.11
doctypes: [Loan Repayment, Loan Write Off]
verdict: covered
analysis_status: verified
dev_items: []
options: [Loan Repayment.Repayment Type=Write Off Recovery, Loan Repayment.Repayment Type=Write Off Settlement]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:1021-1028"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-203"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-203"
  - "sources/verification/verification_report.md#BR-LMS-203"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-203"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-203"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-203, decision.write-off, bridge.BR-LMS-202, bridge.BR-LMS-200]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. Write Off Recovery and Write Off Settlement are the only repayment types accepted on a written-off loan, apart from waivers the system creates, and the money is credited to a recovery account on the original loan. A recovery is not capped, and an amount beyond the open principal is booked as a new interest demand.

## Business need

Money recovered after a write-off must be recorded as a write-off recovery against the original loan, treated by policy (BR-LMS-203 in section 7.11, BRD PDF page 54). See `concept.BR-LMS-203`. The write-off paths are in `decision.write-off`.

## Frappe Lending today

On a Written Off loan, a **Loan Repayment** must be of type Write Off Recovery or Write Off Settlement, or be a waiver created by the system. Any other type is refused with "Repayment type can only be Write Off Recovery or Write Off Settlement". The same two types are also refused unless the loan is Written Off or Settled ("please write off the loan first") (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1021-1028`). In the test, a Normal Repayment on a written-off loan was refused. A Write Off Recovery of 15,000 reduced the principal demands from 39,949.95 to 24,949.95 and posted to the bank and to Bad Debt Recovery, and the loan stayed Written Off with its written-off amount unchanged.

## Match or gap, and why

This is **covered**, and the verification confirmed the verdict with caveats (J8).

- A recovery is not capped. A second recovery of 30,000 cleared the 24,949.95 of principal and booked the other 5,050.05 as a new Interest demand, with the full 30,000 credited to Bad Debt Recovery (DEF-36).
- A Write Off Settlement of 40,000 paid the oldest principal demands in due order (six of 12) and left seven principal demands with 60,000 outstanding. The loan became Settled and kept its NPA flag. The form showed a payable figure that the saved record did not use (DEF-42).
- The treatment "in accordance with policy" is the bank's to define; the BRD gives no policy, and the app books all recovery to one account.

## What to do today

Use Write Off Recovery for money received. Check how much of the recovery was applied to demands, and book any surplus by hand.

## Planned fix

No development item is assigned. The final report proposes ND-34 (the recovery rule, medium) and ND-38 (one write-off recovery figure, small).
