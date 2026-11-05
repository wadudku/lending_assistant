---
id: bridge.BR-LMS-168
type: bridge
title: How much to close today?
summary: "Partly covered. The Loan Repayment form quotes a payoff by repayment type and date, but the figure shown and what a closure books can differ. The original analysis said covered."
br_ids: [BR-LMS-168]
brd_section: 7.7
doctypes: [Loan Repayment]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Repayment.Payable Amount, Loan Repayment.Amount Paid, Loan Repayment.Value Date]
options: [Loan Repayment.Repayment Type=Loan Closure, Loan Repayment.Repayment Type=Partial Settlement, Loan Repayment.Repayment Type=Full Settlement]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-168"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-168"
  - "sources/verification/verification_report.md#BR-LMS-168"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-168"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-168"
  - "sources/verification/analysis_corrections.md#3.-requirement-by-requirement-table-verdict-changes-21"
related: [concept.BR-LMS-168, decision.waiver, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The Loan Repayment form quotes a payoff by repayment type and date, but the figure shown and what a closure books can differ. The original analysis said covered.

## Business need

The system must quote the payoff on demand and support approved settlements against it (BR-LMS-168, BRD 7.7.1, PDF page 51). See `concept.BR-LMS-168`.

## Frappe Lending today

There is no separate "Get Dues" screen. The payoff is the **Loan Repayment** form: choose the loan, the **Repayment Type** and a **Value Date**, and a method called `calculate_amounts` fills the pending and payable principal, interest, penalty and charges. The figure is as at the chosen date and differs by type: in the test, Partial Settlement, Full Settlement and Loan Closure gave three different amounts for the same loan.

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it to partly covered (J9). The calculation exists, but the figure the user reads is not always what is booked.

- In the verification's Loan Closure, the closure's own payable was 101,186.03, and a payment of 101,150.68 (the figure from the bills already raised) was accepted. The 35.35 gap was posted to Interest Waiver automatically, with no approval and no waiver record (DEF-38). The figure shown before the closure and the interest the closure books differ; the report did not isolate which of the two is wrong.
- The report later extended DEF-38: the closure check counts only interest already accrued (booked day by day), so interest since the last accrual can be lost with no waiver at all (527.00 on a closure back-dated 28 days).
- For a Full Settlement the figure leaves out unbooked interest, which the settlement then bills (DEF-34).
- For Write Off Settlement and Write Off Recovery, the payable shown before saving differs from the saved record (DEF-42).
- Amount Paid is not reliably pre-filled with the payable.

## What to do today

Quote from the Loan Repayment form for the right type and date, and re-check the figure just before submitting. Before a closure, make sure interest has been accrued up to the value date. After a closure, look in the accounting entries for an Interest Waiver line and get any such amount approved outside the system.

## Planned fix

No development item is assigned in the verified list. The verification proposes ND-36 (one payoff calculation for the form, the closure check and the booked interest, with any waiver as a separate approved record) and ND-38 (one figure for the write-off recovery form and the saved record). Approval of settlements and waivers belongs to D8.
