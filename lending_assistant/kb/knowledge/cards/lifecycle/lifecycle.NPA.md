---
id: lifecycle.NPA
type: lifecycle
title: Loan state NPA
summary: "In the BRD, NPA is a loan state that triggers income treatment. In Frappe Lending it is a flag on the loan, applied to all of the borrower's loans, with unpaid interest moved to suspense (held back from income)."
br_ids: []
brd_section: 5.3
doctypes: [Loan, Loan NPA Log, Loan Product]
dev_items: [D15]
lifecycle_state: NPA
fields: [Loan.Is NPA, Loan.Manual NPA, Loan NPA Log.NPA Date, Loan Product.Days Past Due Threshold for NPA]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1706", "lending/loan_management/doctype/loan/loan.py:1802"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-144"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-194"
  - "sources/verification/reqs.json#BR-LMS-194"
  - "sources/verification/verification_report.md#BR-LMS-194"
  - "sources/verification/reqs.json#BR-LMS-191"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/verification/reqs.json#BR-LMS-144"
  - "sources/verification/verification_report.md#BR-LMS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
related: [brd_section.5.3, lifecycle.OVERDUE, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** In the BRD, NPA is a loan state that triggers income treatment. In Frappe Lending it is a flag on the loan, applied to all of the borrower's loans, with unpaid interest moved to suspense (held back from income).

## The BRD state

BRD 5.3 (PDF page 27) defines NPA as: non-performing classification reached, and income treatment applies. NPA means non-performing asset, a bad loan. BR-LMS-144 requires that normal income stops being recognised and qualifying unpaid interest and charges move to suspense in line with Bangladesh Bank rules. BR-LMS-194 requires them to return to income only on actual recovery.

## The Frappe Lending equivalent

There is no NPA status. The loan has an **Is NPA** check and a **Manual NPA** check, and every change is logged in the **Loan NPA Log** (loan, NPA, manual NPA, event and date). The threshold is set on the product as **Days Past Due Threshold for NPA**. In the code, an NPA decision is applied to all the borrower's active loans together and to the customer (`loan.py` around line 1706). Unpaid interest and charges move to suspense accounts automatically: holding accounts where the interest waits instead of being counted as income.

## Why they differ

The BRD wants NPA as the one current state. Frappe Lending keeps NPA as a flag next to the grade, so the two can disagree: the verification found loans flagged NPA while graded Standard (DEF-7). Several controls the BRD implies are missing: the manual flag has no reason or approver, interest collected while the loan stays NPA is not released from suspense until the loan is upgraded (DEF-15), and unticking a manual NPA does not reverse its suspense (DEF-13).

## How a loan enters and leaves it

A loan enters NPA when the classification run finds days past due above the product threshold, or when someone ticks Manual NPA. It leaves after the overdue amounts are cleared, but the exit needs a further classification run, so a fully paid loan can stay NPA until the next run (DEF-7). The verified results are: covered for BR-LMS-144, and partly covered for BR-LMS-191 and BR-LMS-194.
