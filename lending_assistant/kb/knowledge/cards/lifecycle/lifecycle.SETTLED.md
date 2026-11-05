---
id: lifecycle.SETTLED
type: lifecycle
title: Loan state SETTLED
summary: "In the BRD, SETTLED is a loan closed under an approved settlement, which may include waivers. In Frappe Lending it is a status set by a Full Settlement or a short Write Off Settlement, with no approval step."
br_ids: [BR-LMS-200, BR-LMS-201, BR-LMS-205]
brd_section: 5.3
doctypes: [Loan, Loan Repayment]
dev_items: [D2, D8, D18]
lifecycle_state: SETTLED
fields: [Loan.Status, Loan.Settlement Date]
options: [Loan.Status=Settled]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:1194", "lending/loan_management/doctype/loan/loan.py:1574"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-200"
  - "sources/verification/reqs.json#BR-LMS-201"
  - "sources/verification/reqs.json#BR-LMS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-200"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-205"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D8"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D18"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, decision.waiver, devitem.D18, devitem.D8, devitem.D2]
version: 2
status: approved
approved_by: Owner
---
**In short:** In the BRD, SETTLED is a loan closed under an approved settlement, which may include waivers. In Frappe Lending it is a status set by a Full Settlement or a short Write Off Settlement, with no approval step.

## The BRD state

BRD 5.3 (PDF page 27) defines SETTLED as: closed under an approved settlement, which may include waivers. BR-LMS-201 asks for maker-checker approval within the delegated authority for settlement, waiver and write-off.

## The Frappe Lending equivalent

Frappe Lending has a **Status** value Settled, and the coverage analysis rates the match as covered. In the repayment code, a Full Settlement sets Settled and the settlement date (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1194`); an imported Full Settlement does the same in its own branch (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1147`); and a Write Off Settlement that does not pay the loan off in full also ends in Settled (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1165`). A Full Settlement also creates the interest, penalty and charges waivers and a settlement write-off for the unpaid principal (see `decision.waiver`). The nightly classification treats a Settled loan first, writing off its suspense entries and charges (`lending/loan_management/doctype/loan/loan.py:1574`).

## Why they differ

The status matches. The controls do not. In the test, there was no settlement offer record, nothing held for approval and no limit by role or amount (BR-LMS-200, BR-LMS-201, BR-LMS-205). The make-up of the figure is shown only on the repayment form, and the posting had defects: a Full Settlement that cleared all the principal left the loan flagged NPA with its suspense, and an unbooked interest demand stayed open (DEF-33, DEF-34). The planned settlement proposal (D18) and the approval pack (D8) cover these.

## How a loan enters and leaves it

A loan enters Settled on a submitted settlement repayment of the types above. In the test, Settled loans that were flagged NPA kept the flag: the classification code handles a Settled loan first (`lending/loan_management/doctype/loan/loan.py:1574`) and, as the verification report shows, never reached the code that clears it. See `lifecycle.NPA`.

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
