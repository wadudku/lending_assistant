---
id: bridge.BR-LMS-221
type: bridge
title: Credit-line limits and their change log
summary: "Partly covered. The three limit figures work and the movements made by booking, limit changes, disbursements and repayments are logged, but cancellations are not, the log has no reason or approver, does not log date changes, and its rows can be edited or deleted."
br_ids: [BR-LMS-221]
brd_section: 7.13
doctypes: [Loan, Loan Limit Change Log]
verdict: partial
analysis_status: verified
dev_items: [D8]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-221"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-221"
  - "sources/verification/verification_report.md#BR-LMS-221"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-221"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-221"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [concept.BR-LMS-221, bridge.BR-LMS-222, devitem.D8]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The three limit figures work and the movements made by booking, limit changes, disbursements and repayments are logged, but cancellations are not, the log has no reason or approver, does not log date changes, and its rows can be edited or deleted.

## Business need

For credit lines the platform must track the maximum, utilised and available limit and log every limit movement with its reason and approver (BR-LMS-221 in section 7.13, BRD PDF page 55). See `concept.BR-LMS-221`.

## Frappe Lending today

A line-of-credit **Loan** holds a maximum, a utilised and an available limit. A **Loan Limit Change Log** row holds the loan, the event, the date, the value type and the value change (`lending/loan_management/doctype/loan_limit_change_log/loan_limit_change_log.json`). A row is written when the loan is booked and on every save of the submitted loan (`lending/loan_management/doctype/loan/loan.py:418`, `lending/loan_management/doctype/loan/loan.py:518`), and when a disbursement or a repayment is submitted (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:197`, `lending/loan_management/doctype/loan_repayment/loan_repayment.py:288`). Cancelling a disbursement or a repayment moves the limits back but writes no row (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:330`, `lending/loan_management/doctype/loan_repayment/loan_repayment.py:1548`). In the test on a credit line with a limit of 100,000, a disbursement of 40,000 gave utilised 40,000 and available 60,000. Raising the limit to 150,000 gave available 110,000. Lowering it to 20,000 was refused ("New maximum limit amount cannot be lesser than the utilized limit amount"), and lowering it to 60,000 gave available 20,000. A Principal Adjustment of 10,000 gave utilised 30,000 and available 30,000.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J11).

- The log has no reason field and no approver field. A cut of 90,000 in the limit needed no approval.
- Two Limit Renewal rows of 0.0 were written for saves that changed nothing, and a change of only the end date was not logged as a movement.
- The System Manager can write and delete log rows (DEF-48).
- A Pre Payment of 10,000 on this loan raised an error in the test. It was not investigated.

## What to do today

Record the reason and the approver for each limit change in a register outside the system, and do not rely on the log as complete: compare it with the limit on the loan each month.

## Planned fix

Dev item D8 (approval and audit pack, sized large) covers this row. The final report proposes ND-47 (a limit change log with reason, approver and integrity, small).
