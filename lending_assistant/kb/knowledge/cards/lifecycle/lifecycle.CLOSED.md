---
id: lifecycle.CLOSED
type: lifecycle
title: Loan state CLOSED
summary: "In the BRD, CLOSED is a loan with everything cleared, security released and a final statement issued. In Frappe Lending Closed is a status that several different paths can set, and the final statement is a separate report."
br_ids: [BR-LMS-232, BR-LMS-234, BR-LMS-235]
brd_section: 5.3
doctypes: [Loan]
dev_items: [D2, D8, D20]
lifecycle_state: CLOSED
fields: [Loan.Status, Loan.Closure Date]
options: [Loan.Status=Closed]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:1186", "lending/loan_management/doctype/loan_security_release/loan_security_release.py:167"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-232"
  - "sources/verification/reqs.json#BR-LMS-234"
  - "sources/verification/reqs.json#BR-LMS-235"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-232"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-234"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-235"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D8"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D20"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, devitem.D2, devitem.D8, devitem.D20]
version: 2
status: approved
approved_by: Owner
---
**In short:** In the BRD, CLOSED is a loan with everything cleared, security released and a final statement issued. In Frappe Lending Closed is a status that several different paths can set, and the final statement is a separate report.

## The BRD state

BRD 5.3 (PDF page 27) defines CLOSED as: all obligations cleared; security released; final statement issued.

## The Frappe Lending equivalent

Frappe Lending has a **Status** value Closed, and the coverage analysis rates the match as covered, with the final statement a separate item. The code sets Closed on these paths (the list comes from a search for every place that sets the status; see the completeness row in the claim audit): a repayment of one of the listed types that is flagged to close the loan (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1186`); a Write Off Settlement paid to within the product's write-off amount, when the repayment is flagged to close the loan (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1155-1159`); the closure request function when asked to close at once (`lending/loan_management/doctype/loan/loan.py:904`); an unsecured term loan already in Loan Closure Requested (`lending/loan_management/doctype/loan/loan.py:949`); a Loan Security Release when no quantity is pledged (`lending/loan_management/doctype/loan_security_release/loan_security_release.py:167`); a Loan Refund of an excess payment that brings the excess to zero (`lending/loan_management/doctype/loan_refund/loan_refund.py:90-92`, `lending/loan_management/doctype/loan_refund/loan_refund.py:114-116`; this is the path for BR-LMS-186); a Loan Write Off for an employee loan repaid from salary has a branch that sets Closed (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:289`), but in 16.5.1 it does not run: the loan is read without its fields (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:274-278`), so the check at `lending/loan_management/doctype/loan_write_off/loan_write_off.py:280` always returns; and the daily job for a line of credit past its end date (`lending/hooks.py:192`). Imported repayments have their own branch (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1142`).

## Why they differ

Each path above sets Closed on its own conditions, so the BRD's three conditions (cleared, released, statement issued) are not tested in one place. The release path closes the loan when no quantity is pledged, with today's date rather than the release document's date; in the test it did so for a loan that was already closed and overwrote its closure date (BR-LMS-232, verified partly covered). In the test, the approval step for closure had not been configured (BR-LMS-234). The closure letter and notification do not exist, although the Loan Statement of Account report does (BR-LMS-235).

## How a loan enters and leaves it

A loan enters Closed by one of the paths listed above. A closed loan can go back: cancelling a security release that had closed the loan puts it back to Loan Closure Requested (`lending/loan_management/doctype/loan_security_release/loan_security_release.py:158`). The Servicing Status proposal (D2) would rank CLOSED below WRITTEN_OFF and SETTLED.
