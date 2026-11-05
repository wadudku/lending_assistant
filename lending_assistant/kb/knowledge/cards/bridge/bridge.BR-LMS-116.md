---
id: bridge.BR-LMS-116
type: bridge
title: Link co-lending partners to the product
summary: "Covered. The Loan Product has a Loan Partners field, and each Loan Partner holds its share and base rate. The Loan Partner record carries a beta flag."
br_ids: [BR-LMS-116]
brd_section: 7.2
doctypes: [Loan Product, Loan Partner]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Product.Loan Partners, Loan Partner.Partner Loan Share Percentage, Loan Partner.Partner Base Interest Rate]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_product/loan_product.json:301", "lending/loan_management/doctype/loan_partner/loan_partner.json:129"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-116"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-116"
  - "sources/verification/verification_report.md#BR-LMS-116"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-116"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-116"
related: [concept.BR-LMS-116, brd_section.7.2, glossary.partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The Loan Product has a Loan Partners field, and each Loan Partner holds its share and base rate. The Loan Partner record carries a beta flag.

## Business need

The bank wants a product that is funded on a shared basis to name its partners and their shares (BR-LMS-116, BRD 7.2, PDF page 47). See `concept.BR-LMS-116`.

## Frappe Lending today

The **Loan Product** has a **Loan Partners** field on its Co Lending tab, a multi-select of partners (`loan_product.json` lines 301-305). The **Loan Partner** holds the partner's share percentage (`loan_partner.json` line 129), base interest rate (line 135), schedule type, effective date and organization type. The doctype is marked beta in the file (`loan_partner.json` line 5).

## Match or gap, and why

This is **covered**. In the test, a partner with a 20% share and a 10% base rate was created and linked on a copy of the product, and the Loan form showed the partner field once that product was chosen (verification_report.md:140, 769). Two details from the tests: the Loan Partner also needs a schedule type, an effective date and an organization type, and the organization type is in a collapsed section, so the first save fails with a "Missing Fields" message. The beta flag matters for readiness of co-lending services (the later co-lending requirements).

## What to do today

Create the Loan Partner first, fill the schedule type, effective date and organization type, then link it on the Co Lending tab of the product.

## Planned fix

Nothing is needed for the link itself.
