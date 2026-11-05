---
id: bridge.BR-LMS-105
type: bridge
title: "Bring existing loans over from the old system, and prove the totals match"
summary: "Partly covered. A loan can be imported with opening balances, but there is no control-total check or sign-off, and the standard import mapping is wrong (DEF-6)."
br_ids: [BR-LMS-105]
brd_section: 7.1
doctypes: [Loan, Data Import, Loan Import Details]
verdict: partial
analysis_status: verified
dev_items: [D3]
fields: [Loan.Is Imported, Loan.Migration Date, Loan.Loan Import Details]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.json:724", "lending/loan_management/doctype/loan/loan.json:752", "lending/loan_management/doctype/loan/loan.py:252"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-105"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-105"
  - "sources/verification/verification_report.md#BR-LMS-105"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-105"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-105"
related: [concept.BR-LMS-105, brd_section.7.1, devitem.D3]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A loan can be imported with opening balances, but there is no control-total check or sign-off, and the standard import mapping is wrong (DEF-6).

## Business need

The bank must move its current loans over with their balances and source references, and must prove the totals against the old system before the loans go live (BR-LMS-105, BRD 7.1, PDF page 46). See `concept.BR-LMS-105`.

## Frappe Lending today

There is no separate import doctype in 16.5.1. Migration is done on the **Loan** itself, through the standard Data Import tool. A loan carries **Is Imported** (`loan.json` line 724), **Migration Date** (`loan.json` line 740) and a **Loan Import Details** table (`loan.json` line 752). The code stops with "Migration Date is mandatory for imported loans" when the date is missing (`loan.py` lines 252-253). The table holds the disbursement id, date and amount and the opening principal, interest, penalty, additional interest and charge outstanding. The coverage analysis names a separate import screen; verification found no such doctype in 16.5.1 or in develop (verification_report.md:1476).

## Match or gap, and why

This is **partly covered**. The loading function exists. In the test, there was no control-total check and no sign-off before the loan became active: a loan disbursed for 50,000 with an opening principal of 70,000 was accepted with no warning (verification_report.md:109). Repayment history is not imported. Verification also found the standard mapping wrong, in 16.5.1 and in develop (DEF-6): the opening principal outstanding is billed as one overdue demand on the migration date, the opening ledger entry debits the bank and credits the portfolio, and interest for the pre-migration period is accrued again (verification_report.md:893). Control totals only mean something once that mapping is defined.

## What to do today

Do not rely on the standard import for go-live. Prepare the control totals outside Frappe Lending and compare them by hand with the loaded loans before anyone runs the daily processes on them. Use a small batch first.

## Planned fix

Dev item D3 (`devitem.D3`) adds a migration batch with control totals and a sign-off gate. Verification made it larger because the opening-balance logic must also be patched (ND-4).
