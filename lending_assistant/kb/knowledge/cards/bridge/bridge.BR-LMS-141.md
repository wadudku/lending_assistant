---
id: bridge.BR-LMS-141
type: bridge
title: "Penalty interest, kept separate"
summary: "Partly covered. Penal interest is tracked in its own rows and accounts, but the amount billed is not the product's penal rate, and a payment inside the grace days can still pay penalty. The coverage analysis rated it covered."
br_ids: [BR-LMS-141]
brd_section: 7.5
doctypes: [Loan Product, Loan Interest Accrual, Loan Demand]
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_interest_accrual/loan_interest_accrual.json:179", "lending/loan_management/doctype/loan_interest_accrual/loan_interest_accrual.py:710"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-141"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-141"
  - "sources/verification/verification_report.md#BR-LMS-141"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-141"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-141"
related: [concept.BR-LMS-141, brd_section.7.5, bridge.BR-LMS-130, glossary.penal-interest, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Penal interest is tracked in its own rows and accounts, but the amount billed is not the product's penal rate, and a payment inside the grace days can still pay penalty. The coverage analysis rated it covered.

## Business need

The bank wants penal interest calculated and tracked apart from normal interest, at a configurable rate and basis (BR-LMS-141, BRD 7.5, PDF page 49). See `concept.BR-LMS-141`.

## Frappe Lending today

Penal accruals are **Loan Interest Accrual** rows with the interest type **Penal Interest** (`loan_interest_accrual.json` line 179). The **Loan Product** has the penalty rate (`loan_product.json` line 154), the grace days (line 160) and the accounts Penalty Income (line 141), Penalty Receivable (line 268), Penalty Accrued (line 404) and Penalty Suspense (line 414). The grace days delay the penal accrual, which then backfills from the due date.

## Match or gap, and why

This is **partly covered**. The coverage analysis rated it covered; verification found that "separate" holds for the ledger but not for what is billed (verification_report.md:54, 299). In the test, on a product with 14% interest and a 12% penal rate, the system accrued 12% on the overdue instalment (1.48 a day) but billed "Additional Interest" at the contract rate on the overdue principal (1.49 a day), raised no Penalty demand, and posted the penalty part as a negative 0.01 a day (DEF-10, `loan_interest_accrual.py` lines 710-810). Over 180 days the borrower was billed 950.21 while the penal accrual totalled 922.04. In the test, a payment value-dated inside the grace days but entered after a penal run still paid three days of Additional Interest first, which left the next instalment 4.47 short and a rolling arrear (DEF-11).

## What to do today

Check the Additional Interest demand against the penal accrual for the first overdue instalments. Do not enter a late-keyed payment inside the grace days after a penal run without checking the penalty it pays first.

## Planned fix

DEF-10 and DEF-11 are logged in the verification report with fix directions; the model for the penalty (a combined rate or a separate penalty on the overdue amount) is a decision for NRB. This row has no D item.
