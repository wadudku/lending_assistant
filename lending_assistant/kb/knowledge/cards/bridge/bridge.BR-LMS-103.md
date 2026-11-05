---
id: bridge.BR-LMS-103
type: bridge
title: "Rules come from the product, not from each loan"
summary: "Covered. The product supplies the rules, but the interest rate and the penalty rate on a loan can still be typed over (in the test, with no warning)."
br_ids: [BR-LMS-103]
brd_section: 7.1
doctypes: [Loan, Loan Product]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan.Rate of Interest (%) / Year, Loan.Penalty Charges Rate]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.json:194", "lending/loan_management/doctype/loan/loan.json:676"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-103"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-103"
  - "sources/verification/verification_report.md#BR-LMS-103"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-103"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-103"
related: [concept.BR-LMS-103, brd_section.7.1, brd_section.7.2, devitem.D1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The product supplies the rules, but the interest rate and the penalty rate on a loan can still be typed over (in the test, with no warning).

## Business need

The bank wants servicing rules, schedule method, rate, charges and accounting mappings to come from the product, not from entry on each loan (BR-LMS-103, BRD 7.1, PDF page 46). See `concept.BR-LMS-103`.

## Frappe Lending today

The **Loan Product** supplies the schedule type, the rate, the penalty rate, the grace days, the charges, the payment-order sequences and the accounts, and the **Loan** fetches them. Two fields are fetched only when empty: **Rate of Interest (%) / Year** (`loan.json` lines 194-195) and **Penalty Charges Rate** (`loan.json` lines 676-677). A typed value therefore wins over the product.

## Match or gap, and why

This is **covered**, with one limit. The product supplies the rules the BRD names (schedule method, rate, charges and accounts; verification_report.md:89). In the test, a draft loan on the 14% product was saved with a rate of 2%, with no error and no warning (verification_report.md:89). Both rate fields are editable, and the Loan write permission is granted to the Loan Manager role with no workflow on Loan. Locking the two fields is a configuration change (Customize Form and a role), not new code. The coverage analysis also noted that the rates can be overridden. A deviation approval for such a change is a listed new development item (ND-5).

## What to do today

Treat the product as the source and do not type a rate on the loan. To block the override, an administrator can set the two fields to a higher permission level in Customize Form and give that level to a controlled role.

## Planned fix

A control on rate deviation is logged as ND-5 in the verification report and is part of the scope of dev item D1 (`devitem.D1`).
