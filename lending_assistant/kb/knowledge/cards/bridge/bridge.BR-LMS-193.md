---
id: bridge.BR-LMS-193
type: bridge
title: Set money aside for expected losses (provisioning)
summary: "Gap. The Company holds a table of provision rates by grade and security type, but nothing in the app reads a rate, calculates a provision or stores a basis."
br_ids: [BR-LMS-193]
brd_section: 7.10
doctypes: [Company, Loan IRAC Provisioning Configuration]
verdict: gap
analysis_status: verified
dev_items: [D14]
fields: [Loan IRAC Provisioning Configuration.Provision Rate, Loan IRAC Provisioning Configuration.Security Type]
options: [Loan IRAC Provisioning Configuration.Security Type=Secured, Loan IRAC Provisioning Configuration.Security Type=Unsecured, Loan IRAC Provisioning Configuration.Security Type=Semi-Secured]
lending_version: 16.5.1
code_refs: ["lending/overrides/company.py:18-27"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-193"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-193"
  - "sources/verification/verification_report.md#BR-LMS-193"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-193"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-193"
  - "sources/verification/FINAL_REPORT.md#D14"
related: [concept.BR-LMS-193, concept.BR-LMS-191, devitem.D14]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. The Company holds a table of provision rates by grade and security type, but nothing in the app reads a rate, calculates a provision or stores a basis.

## Business need

The platform must calculate provisions by grade and by secured, semi-secured and unsecured status, and keep the basis of every run (BR-LMS-193 in section 7.10, BRD PDF page 54). See `concept.BR-LMS-193`.

## Frappe Lending today

The **Company** has a table called IRAC Provisioning Configuration. Each row of the **Loan IRAC Provisioning Configuration** has a classification, a **Security Type** of Secured, Unsecured or Semi-Secured, and a **Provision Rate** (`lending/loan_management/doctype/loan_irac_provisioning_configuration/loan_irac_provisioning_configuration.json`). The Company save only checks that no classification and security type pair appears twice (`lending/overrides/company.py:18-27`). The rates are not used anywhere else.

## Match or gap, and why

This is a **gap**, and the verification confirmed it with live data (J4).

- The Provision Rate field is never read by any code, and the app has no provisioning document, run or calculation.
- In the test, a loan graded SS and then DF for months had no entry on any provision account, no journal entry mentioning provision, and nothing on the Short-term or Long-term Provisions accounts for the whole company.
- So the rate table is a place to keep numbers, and the bank has no stored basis for any provision.

## What to do today

Work out provisions outside the system from the Loan Outstanding report and the grade, using the rate table as the source of rates, and post a journal by hand. Keep the working sheet for each month.

## Planned fix

Dev item D14 (provisioning engine, sized medium) covers this row.
