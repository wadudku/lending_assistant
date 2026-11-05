---
id: bridge.BR-LMS-131
type: bridge
title: Attach fees to the loan
summary: "Partly covered. Fees can be attached by hand, but in the test a fee set to be added to the first repayment was not billed. The coverage analysis rated it covered."
br_ids: [BR-LMS-131]
brd_section: 7.4
doctypes: [Loan, Loan Disbursement, Loan Repayment, Loan Demand]
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-131"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-131"
  - "sources/verification/verification_report.md#BR-LMS-131"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-131"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-131"
related: [concept.BR-LMS-131, brd_section.7.4, bridge.BR-LMS-113, glossary.prepayment, glossary.demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Fees can be attached by hand, but in the test a fee set to be added to the first repayment was not billed. The coverage analysis rated it covered.

## Business need

The bank wants product, repayment, prepayment, restructuring and approved ad-hoc charges attached to the loan as configured (BR-LMS-131, BRD 7.4, PDF page 48). See `concept.BR-LMS-131`.

## Frappe Lending today

A disbursement charge can be typed on the loan. A prepayment charge can be typed in the repayment's own **Prepayment Charges** table. A restructure has its own charges. A Sales Invoice linked to a loan raises a **Charges** demand. The fee rules on the product are not applied by themselves (see `bridge.BR-LMS-113`).

## Match or gap, and why

This is **partly covered**. The coverage analysis rated it covered; verification found a defect (verification_report.md:51, 188, DEF-4). In the test, a disbursement charge of 500 set to "Add to first repayment" showed up in row 1 of the schedule and reduced its principal by 500, but the instalment run billed only interest and principal, so no Charges demand was raised. The same 500 had already been invoiced and deducted at disbursement. A daily penalty demand of 0.02 accrued on the unbilled 500. In the test, a prepayment fee worked only by hand: a row in the repayment's Prepayment Charges table created a Sales Invoice and a Charges demand (verification_report.md:511). No rule triggers a prepayment fee automatically (ND-1). The API for ad-hoc charges fails when loan accounting is on (DEF-2, see `bridge.BR-LMS-113`).

## What to do today

Do not use the "Add to first repayment" treatment. Raise fees as a Sales Invoice linked to the loan, so a Charges demand is created, and type prepayment fees in the repayment's Prepayment Charges table.

## Planned fix

ND-1 in the verification report asks for charges to be raised by the product rule. DEF-4 is logged in the verification report. This row has no D item.
