---
id: decision.write-off
type: decision
title: "Decision: writing off a loan balance"
summary: "A write-off removes an unrecoverable balance from the books while keeping the loan's history. The BRD wants a threshold, two people and limits by amount. Frappe Lending can write off automatically with no approver."
br_ids: [BR-LMS-195, BR-LMS-201, BR-LMS-202, BR-LMS-203, BR-LMS-204, BR-LMS-205, BR-GOV-028]
brd_section: 7.11
doctypes: [Loan Write Off, Loan Repayment, Loan]
dev_items: [D8]
decision: write-off
actions: ["Loan Write Off:submit"]
options: [Loan Repayment.Repayment Type=Write Off Recovery, Loan Repayment.Repayment Type=Write Off Settlement]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1361", "lending/loan_management/doctype/loan_write_off/loan_write_off.py:204"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-195"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-202"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-203"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-204"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
  - "sources/verification/reqs.json#BR-LMS-195"
  - "sources/verification/reqs.json#BR-LMS-201"
  - "sources/verification/reqs.json#BR-LMS-202"
  - "sources/verification/reqs.json#BR-LMS-203"
  - "sources/verification/reqs.json#BR-LMS-204"
  - "sources/verification/reqs.json#BR-LMS-205"
  - "sources/verification/FINAL_REPORT.md#D8"
  - "sources/verification/verification_report.md#BR-LMS-195"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [decision.waiver, glossary.write-off, lifecycle.WRITTEN_OFF, devitem.D8]
version: 2
status: approved
approved_by: Owner
---
**In short:** A write-off removes an unrecoverable balance from the books while keeping the loan's history. The BRD wants a threshold, two people and limits by amount. Frappe Lending can write off automatically with no approver.

## The rule

BR-LMS-195 says eligibility for a write-off is checked against a separately configured threshold, distinct from the classification bands. BR-LMS-201 requires maker-checker approval within the delegated authority for the amount and the role, and BR-GOV-028 says those limits are configurable by role and amount band and enforced at the point of action. BR-LMS-202 requires the loan, its schedules, postings and classification history to stay retrievable. BR-LMS-203 says money recovered later is booked against the original loan. BR-LMS-204 says the accounting effects are sent to the core banking system with the journal reference kept, and BR-LMS-205 requires before and after amounts, reason, maker, checker, approval date and any external reference. The BRD does not set the threshold, the roles or the amounts.

## Options

Frappe Lending has four ways to write off. First, the nightly classification creates and submits a Loan Write Off when the days past due exceed the Company's threshold (`lending/loan_management/doctype/loan/loan.py:1361`, `lending/loan_management/doctype/loan/loan.py:1489`); it does so only if a threshold is set, skips a loan that is already Written Off (`lending/loan_management/doctype/loan/loan.py:1488`) and returns early for a frozen loan after its freeze date unless told to ignore the freeze (`lending/loan_management/doctype/loan/loan.py:1305`). Second, a person submits a **Loan Write Off** by hand. Third, a Full Settlement creates a settlement write-off for the unpaid principal. Fourth, a closure request creates and submits one when the residual is below the product's write-off amount or the loan is Settled (`lending/loan_management/doctype/loan/loan.py:896-899`). After a write-off, money comes in as Write Off Recovery or Write Off Settlement repayments. Submitting a write-off sets the loan to Written Off, except for a single settlement write-off (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:204`).

## Who approves

The BRD wants a maker and a different checker, within a limit. The installed Loan Write Off doctype gives the Loan Manager role create, submit and cancel together, and in the test there was no workflow, no Authorization Rule and no amount or role limit on Loan Write Off. The automatic write-off is submitted by the system with no approver, and the form has no reference, reason or approver field (DEF-35).

## How Frappe Lending does it today

The verified results are covered for BR-LMS-195, 202 and 203, partly covered for BR-LMS-201 and 205, and a gap that needs the CBS link for BR-LMS-204. In the test, the threshold is one per Company with no product value; a manual write-off had no eligibility check (a loan with 0 days past due was written off); and after a write-off the loan kept accruing and lost its grade (DEF-36). The planned approval pack (D8, with ND-34 for eligibility, approval and the stop of accruals) adds maker-checker, reason and before and after amounts. See `glossary.write-off`, `decision.waiver` and `lifecycle.WRITTEN_OFF`.

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
