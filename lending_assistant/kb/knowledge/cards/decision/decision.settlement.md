---
id: decision.settlement
type: decision
title: "Decision: settling a loan for less than the full amount"
summary: "A settlement closes a loan for an agreed figure, which may include waivers. The BRD wants the make-up shown before approval and two people to approve. Frappe Lending shows the make-up on the repayment form and has no approval step."
br_ids: [BR-LMS-200, BR-LMS-201, BR-LMS-204, BR-LMS-205, BR-GOV-028]
brd_section: 7.11
doctypes: [Loan Repayment, Loan Write Off, Loan]
dev_items: [D18, D8]
decision: settlement
actions: ["Loan Repayment:settle"]
options: [Loan Repayment.Repayment Type=Partial Settlement, Loan Repayment.Repayment Type=Full Settlement, Loan Repayment.Repayment Type=Write Off Settlement]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment/loan_repayment.json, "lending/loan_management/doctype/loan_repayment/loan_repayment.py:279"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-200"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-204"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
  - "sources/verification/reqs.json#BR-LMS-200"
  - "sources/verification/reqs.json#BR-LMS-201"
  - "sources/verification/reqs.json#BR-LMS-204"
  - "sources/verification/reqs.json#BR-LMS-205"
  - "sources/verification/verification_report.md#BR-LMS-200"
  - "sources/verification/FINAL_REPORT.md#D8"
  - "sources/verification/FINAL_REPORT.md#D18"
related: [decision.waiver, lifecycle.SETTLED, devitem.D18, devitem.D8]
version: 2
status: approved
approved_by: Owner
---
**In short:** A settlement closes a loan for an agreed figure, which may include waivers. The BRD wants the make-up shown before approval and two people to approve. Frappe Lending shows the make-up on the repayment form and has no approval step.

## The rule

BR-LMS-200 says the platform calculates a settlement figure made of principal, interest, penalties, charges and any approved waivers, and presents that composition before approval. BR-LMS-201 requires maker-checker approval within the delegated authority for the amount and the role (BR-GOV-028 makes those limits configurable by role and amount band). BR-LMS-204 says the accounting effects go to the core banking system, and BR-LMS-205 requires before and after amounts, the reason, the maker, the checker, the approval date and any external reference. The BRD does not set the roles or the amounts.

## Options

In Frappe Lending a settlement is a **Loan Repayment** with a **Repayment Type** of Partial Settlement, Full Settlement or Write Off Settlement. A Full Settlement creates interest, penalty and charges waivers for what is payable and a settlement write-off for the unpaid principal (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:279` and the lines that follow it), and sets the loan to Settled. A Partial Settlement does not auto-waive the leftover interest and penalty (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:546`). Write Off Settlement and Write Off Recovery are accepted only on a loan that is Written Off or Settled (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1027`).

## Who approves

The BRD wants a maker and a different checker within a limit. In the test, there was no settlement proposal record, nothing held for approval and no limit by role or amount, and the installed Loan Repayment doctype gives the Loan Manager role both create and submit.

## How Frappe Lending does it today

The verified result for BR-LMS-200 is partly covered. The make-up is shown on the repayment form before submit. The posting had defects: with the test products' settlement order interest is skipped (DEF-3); a Full Settlement that clears all the principal leaves the loan flagged NPA with its suspense (DEF-33); and an unbooked interest demand stays open (DEF-34). The reqs.json text for BR-LMS-200 reads as if both settlement types create waivers; the code and the live results show only Full Settlement does, and this card follows them. The planned settlement proposal (D18, with ND-32, ND-33 and ND-38) and the approval pack (D8) fix these. See `decision.waiver` and `lifecycle.SETTLED`.

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
