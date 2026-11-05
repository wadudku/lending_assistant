---
id: decision.waiver
type: decision
title: "Decision: waiving an amount owed"
summary: A waiver forgives part of what a borrower owes. The BRD wants two people and an amount limit by role. Frappe Lending lets one Loan Manager do it alone.
br_ids: [BR-GOV-008, BR-GOV-028, BR-LMS-185, BR-LMS-201, BR-LMS-205]
brd_section: 7.9
doctypes: [Loan Repayment, Loan Balance Adjustment]
dev_items: [D8]
decision: waiver
actions: ["Loan Repayment:waive"]
options: [Loan Repayment.Repayment Type=Interest Waiver, Loan Repayment.Repayment Type=Penalty Waiver, Loan Repayment.Repayment Type=Charges Waiver]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment/loan_repayment.json, lending/loan_management/doctype/loan_repayment/loan_repayment.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-185"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/verification/reqs.json#BR-LMS-185"
  - "sources/verification/reqs.json#BR-LMS-201"
  - "sources/verification/verification_report.md#BR-LMS-185"
  - "sources/verification/verification_report.md#BR-LMS-201"
  - "sources/verification/FINAL_REPORT.md#D8"
  - "sources/verification/reqs.json#BR-LMS-200"
  - "sources/verification/verification_report.md#BR-LMS-200"
related: [bridge.BR-LMS-165, screen.loan_repayment]
version: 5
status: approved
approved_by: Owner
---
**In short:** A waiver forgives part of what a borrower owes. The BRD wants two people and an amount limit by role. Frappe Lending lets one Loan Manager do it alone.

## The rule

A waiver is the bank forgiving part of an amount owed, such as interest, penalty or charges. BR-GOV-008 says every controlled financial change, including waiver, needs maker-checker approval by two different users. BR-GOV-028 says delegated authority limits for waiver, settlement and write-off are set by role and amount band and enforced at the point of action: a case above the user's limit escalates and that user cannot act on it. BR-LMS-185 and BR-LMS-205 add that each waiver records before and after amounts, the reason, the maker, the checker, the approval date and a reference. BR-LMS-201 applies the same approval to settlements and write-offs.

## Options

Frappe Lending offers three waiver types in **Repayment Type**: Interest Waiver, Penalty Waiver and Charges Waiver. Two paths also create waivers by themselves, with no approval:

- Submitting a Full Settlement creates Interest, Penalty and Charges Waiver repayments for what is still payable, and a settlement **Loan Write Off** for the unpaid principal (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:279-284`, `lending/loan_management/doctype/loan_repayment/loan_repayment.py:1290-1336`). Imported and bulk-posted repayments skip this (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:184-187`, `lending/loan_management/doctype/loan_repayment/loan_repayment.py:209-210`). A Partial Settlement creates no settlement waivers.
- A repayment short by no more than the loan product's Auto Write Off Amount creates an automatic waiver (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:394`, `lending/loan_management/doctype/loan_repayment/loan_repayment.py:1438-1473`), unless it is back-dated (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:384-392`) or, as above, imported or bulk-posted. Only the types listed at `lending/loan_management/doctype/loan_repayment/loan_repayment.py:1169-1182` also close the loan (Write Off Settlement: `lending/loan_management/doctype/loan_repayment/loan_repayment.py:1153-1161`). DEF-39 tested this with a Normal Repayment, which closed the loan.

Separately, a **Loan Balance Adjustment** can credit the waiver account directly. For a waiver entered by hand, the only built-in limit found is that it cannot be larger than the overdue amount.

## Who approves

The BRD says two different users, and limits that are configurable by role and amount band (BR-GOV-028), but it does not set the roles or the amounts; the bank has to supply them. In Frappe Lending today nobody else is required: no workflow or authorisation rule exists on Loan Repayment, Loan Write Off or Loan Balance Adjustment, and the installed Loan Repayment doctype gives Loan Manager both create and submit, so the same Loan Manager can create and submit a waiver.

## How Frappe Lending does it today

The verified result is partly covered for BR-LMS-185 and BR-LMS-201. In the tests a waiver of 500 was submitted by one user with no approver and no before and after record. A Loan Balance Adjustment accepted any contra account, and a draft adjustment of 10,000,000 against Cash was accepted. D8 (the approval and audit pack) with ND-23 adds a workflow where maker and checker are different users, approval limits by role and amount, a mandatory reason and reference, and before and after amounts on the record. Until then, treat every waiver as needing a second person outside the system. See `bridge.BR-LMS-165` and `screen.loan_repayment`.
