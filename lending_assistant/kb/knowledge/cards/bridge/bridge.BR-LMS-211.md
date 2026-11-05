---
id: bridge.BR-LMS-211
type: bridge
title: "Which products each partner joins, and its share"
summary: "Covered. A Loan Product lists its partners in a Co Lending tab, the partner is chosen on the Loan, and the share works. The share is one figure on the partner, not one per product."
br_ids: [BR-LMS-211]
brd_section: 7.12
doctypes: [Loan Product, Loan Partner, Loan]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Partner.Repayment Schedule Type]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:346-366"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-211"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-211"
  - "sources/verification/verification_report.md#BR-LMS-211"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-211"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-211"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-211, bridge.BR-LMS-210, bridge.BR-LMS-212]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A Loan Product lists its partners in a Co Lending tab, the partner is chosen on the Loan, and the share works. The share is one figure on the partner, not one per product.

## Business need

Each partner's products must be defined with the share of loan amount and of collection that applies (BR-LMS-211 in section 7.12, BRD PDF page 55). See `concept.BR-LMS-211`.

## Frappe Lending today

The **Loan Product** has a Co Lending tab with a table of partners; each row holds only the link to a **Loan Partner** (`lending/loan_management/doctype/loan_product/loan_product.json`, `lending/loan_management/doctype/loan_product_loan_partner/loan_product_loan_partner.json`). The partner is then chosen on the **Loan**. The share of the loan is the partner's **Partner Loan Share Percentage**, and the way collections are split is its **Repayment Schedule Type**: EMI (PMT) based, Collection at partner's percentage, or POS reduction plus interest at partner ROI (`lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:346-366`). For charges, the partner has **Loan Partner Shareable** rows that give a share per charge item. In the test, a product linked the partner, the loan chose it, and the disbursement posted the partner's 20% (20,000 of 100,000) to a receivable and a funds clearing account, while the bank still paid out the full 100,000.

## Match or gap, and why

This is **covered**, and the verification confirmed the verdict with a caveat (J10).

- The share is a single figure on the partner. The product row has only the partner link. A different share for another product needs another Loan Partner record. That is configuration, not code.
- In the test the partner's own funding, the cash it puts in, was not posted. The app's partner postings are made only where partner accounting is read: disbursement, repayment and charge invoices.

## What to do today

Create one Loan Partner for each combination of partner and share, and link it to the product. Record the partner's cash funding outside the system.

## Planned fix

No development item is assigned. The final report proposes ND-42 (a partner share per product, small).
