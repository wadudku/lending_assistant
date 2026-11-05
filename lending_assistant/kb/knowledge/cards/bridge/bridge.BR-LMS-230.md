---
id: bridge.BR-LMS-230
type: bridge
title: Check everything is cleared before closing
summary: "Partly covered. A Loan Closure checks the amount paid, but it accepts a shortfall up to the product's Auto Write Off Amount and a future closure date, and the Request Loan Closure button works out a lower figure."
br_ids: [BR-LMS-230]
brd_section: 7.14
doctypes: [Loan, Loan Repayment, Loan Product]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Product.Excess Amount Acceptance Limit]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:1046-1050", "lending/loan_management/doctype/loan/loan.py:875-901", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:1360-1420"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-230"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-230"
  - "sources/verification/verification_report.md#BR-LMS-230"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-230"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-230"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-230, decision.waiver, decision.write-off, lifecycle.CLOSED, lifecycle.CLOSURE_REQUESTED, bridge.BR-LMS-204]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Loan Closure checks the amount paid, but it accepts a shortfall up to the product's Auto Write Off Amount and a future closure date, and the Request Loan Closure button works out a lower figure.

## Business need

Before closing, the platform must check that principal, interest, penalty, charges and every tracked receivable are cleared or formally resolved, and must say what is left (BR-LMS-230 in section 7.14, BRD PDF page 55). See `concept.BR-LMS-230`.

## Frappe Lending today

Three code paths decide whether a payment may close a loan. First, a **Loan Repayment** of type Loan Closure refuses an amount below the payable amount minus the product's Auto Write Off Amount (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1046-1050`). Second, the Request Loan Closure button calls `request_loan_closure` (`lending/loan_management/doctype/loan/loan.py:875-901`). It adds the pending principal, the interest and the penalty and takes off any excess paid. If the result is smaller than the Auto Write Off Amount, or the loan is Settled, it creates and submits a Loan Write Off for it; otherwise it refuses any amount above 0. Third, any repayment closes the loan on its own when the shortfall is within the Auto Write Off Amount (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1360-1420`). The status is set for nine repayment types, Normal Repayment and Loan Closure among them (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1169-1187`). This is DEF-39 (see `bridge.BR-LMS-234`). Paths that close a loan without a payment (refund, security release, Close Loan button, credit-line job) are in `lifecycle.CLOSED`. In the test (Loan G) the closure repayment needed 51,086.25, with unbooked interest and penalty, and the generic 50,575.34 was refused.

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J9).

- In the test a closure short by 35.35 (101,150.68 against 101,186.03) was accepted, and the gap went to Interest Waiver with no approval (DEF-38).
- A Loan Closure with a value date of 6 December was accepted on 3 November (DEF-40).
- The closure button works out its own figure without the closure type, which leaves out unbooked interest and penalty. Its sum has no charges in it. The message gives one amount, not the item that blocks.
- A repayment only updates the values of the pledged securities (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:287`, `lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.py:181-216`). None of these three checks for a pledge that is still open, and in the test the loan closed with collateral still pledged (DEF-39).
- A Loan Closure also left a principal demand over-paid (DEF-41).

## What to do today

Before a closure, print the payoff from the Loan Closure figure (not the generic one) and check by hand that no charges, open demands or pledged collateral remain. Do not close with a value date after today.

## Planned fix

Dev item ND-35 (closure control: a request, checks, no future date, a closure date set once, medium) and ND-36 (one payoff calculation, small) are proposed in the final report. Question Q9 to NRB asks what shortfall the system may waive without a person.
