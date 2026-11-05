---
id: bridge.BR-LMS-234
type: bridge
title: Closure needs approval
summary: "Partly covered. A Loan Closure Requested status exists, but nothing approves the step. Several routes close a loan with no request at all, and no approver is recorded."
br_ids: [BR-LMS-234]
brd_section: 7.14
doctypes: [Loan, Loan Repayment]
verdict: partial
analysis_status: verified
dev_items: [D8]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:875-912", "lending/loan_management/doctype/loan/loan.py:937-951"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-234"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-234"
  - "sources/verification/verification_report.md#BR-LMS-234"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-234"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-234"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [concept.BR-LMS-234, lifecycle.CLOSURE_REQUESTED, lifecycle.CLOSED, decision.waiver, bridge.BR-LMS-222, bridge.BR-LMS-230, bridge.BR-LMS-232, devitem.D8]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Loan Closure Requested status exists, but nothing approves the step. Several routes close a loan with no request at all, and no approver is recorded.

## Business need

Closure must follow an authorised workflow from closure requested to closed, with the authorising user and time kept (BR-LMS-234 in section 7.14, BRD PDF page 56). See `concept.BR-LMS-234`.

## Frappe Lending today

The Request Loan Closure button sets the **Loan** status to Loan Closure Requested with a direct database update, for any user who can write to the loan (`lending/loan_management/doctype/loan/loan.py:875-912`). For an unsecured term loan in that status, a Close Loan button sets it to Closed (`lending/loan_management/doctype/loan/loan.py:937-951`). For a secured loan, approving a Loan Security Release closes it (see BR-LMS-232). Each call checks only that the user can write to the loan, and the Loan has no approver field. The Loan keeps a change history (track changes is on), which keeps the user and time of saved edits. These two status changes are direct database updates and not saves, and the verification did not look at whether they show in the history.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict with more cases (J9).

- A Normal Repayment 25.00 short of the payable set the loan to Closed with no closure request, because the shortfall was within the Auto Write Off Amount. The system then created a Penalty Waiver of 25.00 with no approver (DEF-39).
- A Loan Closure repayment closes the loan on submit: no request, approval or second person (L7-1, G, H).
- The daily credit-line job closes loans with no repayment, request or approval (see BR-LMS-222).
- `request_loan_closure` is a whitelisted call (`lending/loan_management/doctype/loan/loan.py:874-875`). Called directly with its auto-close argument, it sets the loan to Closed with no request step (`lending/loan_management/doctype/loan/loan.py:903-906`). The form button does not pass that argument.
- A Loan Refund and a Write Off Settlement can also close a loan; the full list of paths that set Closed is in `lifecycle.CLOSED`.
- The BRD's authorised path needs a workflow, which is a setup in Frappe and not in the loan app.

## What to do today

Set up a Frappe Workflow on the Loan with an approver role, and treat a Loan Closure repayment as needing the same sign-off outside the system until a control exists. Record the approver's name and time in a register.

## Planned fix

Dev item D8 (approval and audit pack, sized large) covers this row, and ND-35 (closure control) is proposed in the final report. Question Q9 to NRB asks who must approve a closure.
