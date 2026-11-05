---
id: bridge.BR-LMS-186
type: bridge
title: "Refund overpayments, with approval"
summary: "Partly covered. A Loan Refund pays back an excess amount and keeps a reference number, and an over-refund is refused, but there is no approval step. The original analysis said covered."
br_ids: [BR-LMS-186]
brd_section: 7.9
doctypes: [Loan Refund, Loan]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Refund.Reference Number, Loan Refund.Is Excess Amount Refund, Loan Refund.Is Security Amount Refund]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_refund/loan_refund.py:47", "lending/loan_management/doctype/loan_refund/loan_refund.py:90-92"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-186"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-186"
  - "sources/verification/verification_report.md#BR-LMS-186"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-186"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-186"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [concept.BR-LMS-186, lifecycle.CLOSED, devitem.D8, bridge.BR-LMS-187]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Loan Refund pays back an excess amount and keeps a reference number, and an over-refund is refused, but there is no approval step. The original analysis said covered.

## Business need

An eligible excess payment must be refundable under approval, with the refund recorded against the loan and its external reference (BR-LMS-186 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-186`.

## Frappe Lending today

A **Loan Refund** has a refund amount, a refund account, a **Reference Number** and two ticks: **Is Excess Amount Refund** and **Is Security Amount Refund**. On submit, an excess refund lowers the loan's excess amount paid and posts the entry. A refund larger than the excess is refused ("Excess amount refund cannot be more than excess amount paid") (`lending/loan_management/doctype/loan_refund/loan_refund.py:94`). In the test, a refund of 1,000 took the excess from 3,332.13 to 2,332.13 and posted to the ledger, and a refund of 5,000 was refused.

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J9).

- Loan Refund has no approval step. The lending app ships no workflow for it, and the doctype has no approver field. The Loan Manager role can create, submit and cancel it, so one user did all three in the test.
- A second check of the refund against the total net paid (`validate_refund_amount`) is in the code but its call is commented out (`lending/loan_management/doctype/loan_refund/loan_refund.py:47`).
- When an excess refund takes the excess to zero, the code sets the loan to Closed with the refund's value date, whatever status the loan had (`lending/loan_management/doctype/loan_refund/loan_refund.py:90-92`). In the test, a full excess refund turned a Settled loan into Closed (DEF-43). The other places that set Closed are listed in `lifecycle.CLOSED`.

## What to do today

Have a second person approve each refund before the first one submits it, and write the bank reference in the Reference Number field. Do not refund the last of an excess on a Settled loan without first deciding that you want it Closed.

## Planned fix

No development item is assigned. Approval comes under D8 (approval and audit pack). The final report proposes ND-39 (a refund must not close the loan, small).
