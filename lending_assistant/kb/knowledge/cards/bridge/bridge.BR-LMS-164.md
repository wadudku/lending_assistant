---
id: bridge.BR-LMS-164
type: bridge
title: Split the payment in the set order and show it
summary: "Partly covered. The split is shown line by line, but a payment order (offset order) that uses the Interest component never pays interest. The original analysis said covered."
br_ids: [BR-LMS-164]
brd_section: 7.7
doctypes: [Loan Repayment, Loan Demand Offset Order]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Repayment.Repayment Details]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:1968"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-164"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-164"
  - "sources/verification/verification_report.md#BR-LMS-164"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-164"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-164"
  - "sources/verification/analysis_corrections.md#3.-requirement-by-requirement-table-verdict-changes-21"
related: [concept.BR-LMS-164, bridge.BR-LMS-163, glossary.allocation-order]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The split is shown line by line, but a payment order (offset order) that uses the Interest component never pays interest. The original analysis said covered.

## Business need

Payments must follow the bank's configured order, and the split must be visible (BR-LMS-164, BRD 7.7.1, PDF page 51). See `concept.BR-LMS-164`.

## Frappe Lending today

The **Repayment Details** table on **Loan Repayment** lists each bill (Loan Demand) the payment cleared. The order is set as a **Loan Demand Offset Order** (the allocation order, see `glossary.allocation-order`) on the product or the company, and the order used depends on the loan's asset class, its health group such as standard or non-performing. The component choices include Penalty, Charges, Interest and Principal, among others.

## Match or gap, and why

This is **partly covered**. The original analysis marked it covered, because the table and the order setting both exist. The live test changed the verdict (J3). With the site's own order (Penalty, Charges, Interest, Principal), a payment of 3,000 went to penalty 0.92 and then entirely to principal. The interest due and the penal interest billed as Additional Interest were skipped, so the borrower stayed overdue while the principal fell.

The cause is that the code pays interest only for a component called Normal, while the form offers Interest. In the verified tests on 16.5.1 only orders built from the EMI (Principal + Interest) component paid interest correctly. This is defect DEF-3 in the verification report, and the Penalty component also does not pay penal interest billed as Additional Interest.

## What to do today

Build offset orders from **EMI (Principal + Interest)** and **Additional Interest**, as the verification did. Do not use the plain Interest component. After a payment, open the Repayment Details and confirm interest was cleared.

## Planned fix

ND-10 in the verification report: map the Interest component (and let Penalty cover Additional Interest) in the allocation, or block components that do not work on the order form.
