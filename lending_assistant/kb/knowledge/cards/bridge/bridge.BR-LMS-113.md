---
id: bridge.BR-LMS-113
type: bridge
title: Rules for fees and charges
summary: "Partly covered. The product can name a fee and its accounts, but its percentage, amount and basis are not read by the code, so the rule raises no fee. The coverage analysis rated it covered."
br_ids: [BR-LMS-113]
brd_section: 7.2
doctypes: [Loan Product, Loan Charges, Loan]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Charges.Charge Based On, Loan Charges.Percentage, Loan Charges.Amount]
lending_version: 16.5.1
code_refs: ["lending/api.py:141", "lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:889", "lending/loan_management/doctype/loan_charges/loan_charges.py:18"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-113"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-113"
  - "sources/verification/verification_report.md#BR-LMS-113"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-113"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-113"
related: [concept.BR-LMS-113, brd_section.7.2, glossary.waiver, decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The product can name a fee and its accounts, but its percentage, amount and basis are not read by the code, so the rule raises no fee. The coverage analysis rated it covered.

## Business need

The bank wants each charge to define when it applies, how it is calculated and which accounts it maps to (BR-LMS-113, BRD 7.2, PDF page 47). See `concept.BR-LMS-113`.

## Frappe Lending today

The **Loan Product** has a **Charges** table (**Loan Charges**) with a charge type, **Charge Based On** (Percentage or Fixed Amount), a percentage or amount, and accounts for income, receivable, waiver, write-off and suspense. The accounts are used when a charge is raised, either as a loan charge at disbursement or as a Sales Invoice linked to the loan. There is no field for when the charge applies. The product row's `charge_based_on`, `percentage` and `amount` are not read by any Python or JavaScript code outside tests in 16.5.1. A grep over the whole app for `charge_based_on` finds only the type line `loan_charges.py` line 18 and the doctype JSON, and for `percentage` only the doctype JSON, the arguments of `apply_charge` (`api.py` lines 107, 125, 128), which take the rate from the caller, and an unrelated partner option. For `amount`, which is too common to grep, every query of the "Loan Charges" rows (`loan.py` lines 220 and 1987, `loan_repayment.py` lines 508 and 2494, `loan_write_off.py` lines 503 and 558, `loan_disbursement.py` line 916) reads only the charge type and the account fields. The charge amount at `loan.py` line 988 belongs to the loan's own charges table, not to the product row.

## Match or gap, and why

This is **partly covered**. The coverage analysis rated it covered; verification found that the rule had no effect in the test (verification_report.md:49, 133). In the test, a 1% charge row was added to a copy of the product, a loan was booked on it, and no charge, invoice or demand appeared. A fee appeared only when it was typed on the loan, and the invoice used the product's income account. In the test, the product's charge row was not even copied onto a draft loan (ND-1). The one API for ad-hoc charges, `apply_charge`, fails when loan accounting is on: it passes 8 arguments to a function that takes 7 (`api.py` line 141 and `loan_disbursement.py` lines 889-891, DEF-2). The same code is in develop, so there is no fix to wait for there.

## What to do today

Type each fee on the loan, or raise it as a Sales Invoice linked to the loan. Do not use `apply_charge` while loan accounting is on. Do not rely on the percentage in the product's charge row.

## Planned fix

ND-1 in the verification report asks for charges to be applied automatically from the percentage, amount and an event field. This row has no D item.
