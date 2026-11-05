---
id: lifecycle.CLOSURE_REQUESTED
type: lifecycle
title: Loan state CLOSURE_REQUESTED
summary: "In the BRD, CLOSURE_REQUESTED is a payoff that has been asked for and is being checked. Frappe Lending has a status of the same meaning, but its own check of the payoff figure can differ from the closure repayment's."
br_ids: [BR-LMS-230, BR-LMS-234]
brd_section: 5.3
doctypes: [Loan]
dev_items: [D2, D8]
lifecycle_state: CLOSURE_REQUESTED
fields: [Loan.Status]
options: [Loan.Status=Loan Closure Requested]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:907", "lending/loan_management/doctype/loan/loan.py:945"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-230"
  - "sources/verification/reqs.json#BR-LMS-234"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-230"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-234"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D8"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, devitem.D8, devitem.D2]
version: 1
status: approved
approved_by: Owner
---
**In short:** In the BRD, CLOSURE_REQUESTED is a payoff that has been asked for and is being checked. Frappe Lending has a status of the same meaning, but its own check of the payoff figure can differ from the closure repayment's.

## The BRD state

BRD 5.3 (PDF page 27) defines CLOSURE_REQUESTED as: payoff requested and under validation. BR-LMS-234 asks that closure needs approval.

## The Frappe Lending equivalent

Frappe Lending has a **Status** value Loan Closure Requested. The closure request function sets it (`lending/loan_management/doctype/loan/loan.py:907`), unless it is asked to close at once. First it works out the amount still owed. If the shortfall is below the product's write-off amount, or the loan is Settled, it creates and submits a write-off; if the amount is above that, it refuses (`lending/loan_management/doctype/loan/loan.py:901`). The coverage analysis rates the match as covered, and the verified result for BR-LMS-234 is partly covered, because the approval step still has to be configured.

## Why they differ

The status matches the BRD. The check does not always match the closure repayment. The verification found that the request function computes its own figure without the unbooked interest and penalty that the Loan Closure repayment includes (BR-LMS-230, changed to partly covered). In the test on one loan, the request function accepted a figure that the Loan Closure repayment's own validation then rejected as too low.

## How a loan enters and leaves it

A loan enters the state when the request function is called without auto-close (`lending/loan_management/doctype/loan/loan.py:907`). An unsecured term loan in this state is then moved to Closed by a second function (`lending/loan_management/doctype/loan/loan.py:945`). For a secured loan, a Loan Security Release closes the loan once no pledged quantity is left, and cancelling a release that had closed the loan returns it to this state (`lending/loan_management/doctype/loan_security_release/loan_security_release.py:158`).
