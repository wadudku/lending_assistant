---
id: bridge.BR-LMS-202
type: bridge
title: A write-off keeps the history
summary: "Covered. A Loan Write Off changes the loan's status and posts the loss, and the loan, its schedule, demands, accruals and logs all stay. After a write-off the loan keeps accruing and loses its grade."
br_ids: [BR-LMS-202]
brd_section: 7.11
doctypes: [Loan Write Off, Loan]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_write_off/loan_write_off.py:201-209"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-202"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-202"
  - "sources/verification/verification_report.md#BR-LMS-202"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-202"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-202"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-202, decision.write-off, lifecycle.WRITTEN_OFF, bridge.BR-LMS-195, bridge.BR-LMS-203]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A Loan Write Off changes the loan's status and posts the loss, and the loan, its schedule, demands, accruals and logs all stay. After a write-off the loan keeps accruing and loses its grade.

## Business need

A write-off must record its effect without destroying the loan's history, so that the loan, schedule versions, postings and classification history stay retrievable (BR-LMS-202 in section 7.11, BRD PDF page 54). See `concept.BR-LMS-202`. The ways a loan is written off are in `decision.write-off`; the state is `lifecycle.WRITTEN_OFF`.

## Frappe Lending today

Submitting a **Loan Write Off** records the amount written off on the **Loan** and, unless it is the one settlement write-off, sets the status to Written Off (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:201-209`). It posts the loss to the write-off account. The Loan Write Off code has no delete call, and the only delete call in the repayment code clears a repayment's own detail rows (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1696-1700`). In the test, a write-off of 100,000 posted a debit to Bad Debts Written Off and a credit to the portfolio. The system created an Interest Waiver of 5,612.92 and a Penalty Waiver of 1,368.69, and the suspense was written off against the waived receivable. The schedule stayed Active, and 461 demands, 632 accruals and the days past due and NPA logs were still there.

## Match or gap, and why

This is **covered**, and the verification confirmed the verdict with caveats (J8).

- After the write-off an accrual row was created (23.03, no ledger entry), so the loan keeps accruing.
- A forced classification run blanked the grade: 0 days past due, an empty class and the NPA flag on.
- Total Amount Paid counts the waivers as paid, and the principal demands stay open (DEF-36).
- The write-off form has no reference, reason or approver field (see `bridge.BR-LMS-205`).

## What to do today

Treat the loan's ledger and demands as the record after a write-off. Do not rely on the grade or on Total Amount Paid, and stop the loan's accrual and classification by hand if your policy needs it.

## Planned fix

No development item is assigned. The final report proposes ND-34 (write-off control: eligibility, approval, stop accruals and the recovery rule, medium).
