---
id: howto.company.view_loan_settings
type: howto
title: How to read the company-level loan settings (view only)
summary: "Day-count convention, loan accounting switches, grade bands and provision rates are Company settings shared by every product; they are plain tables with no version, effective date or approval."
br_ids: [BR-LMS-111, BR-LMS-115, BR-LMS-197, BR-LMS-193]
brd_section: 7.2
doctypes: [Company]
dev_items: [D5, D13]
journeys: [J2, J4]
actions: ["Company:view"]
fields: [Company.Interest Day-Count Convention, Company.Enable Loan Accounting, Company.Consolidate Loan GL Monthly]
options: []
menus: [Lending > Setup > Company]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J2_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#4.1"
  - "sources/verification/walkthroughs/J2_walkthrough.md#4.2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#5.4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#5.1"
related: [bridge.BR-LMS-115, bridge.BR-LMS-197, bridge.BR-LMS-193, howto.loan_product.set_rates]
version: 1
status: approved
approved_by: Owner
---
**In short:** Day-count convention, loan accounting switches, grade bands and provision rates are Company settings shared by every product; they are plain tables with no version, effective date or approval.

## Before you start

⚠ This card is view only. The Company form is shared by every product, so do not edit it for a test. You need read permission on **Company**. The screenshots of this form are left out of the card because they show a tab name that the walkthrough and the verification report spell differently (conflict C145); names on the dev site are test records.

## Steps

1. Open Lending > Setup > Company and open the company. The loan settings are in the Loan Settings section of the form (close the Getting Started panel if it covers the form).
2. Read **Interest Day-Count Convention**. In the walkthrough it was Actual/365. It is a Company setting, so every product of the company uses it.
3. Read the accounting switches: **Enable Loan Accounting** (the loan system posts its own ledger entries) and **Consolidate Loan GL Monthly** (one ledger voucher a month for accruals and demands). The walkthrough company posted one entry per accrual and demand.
4. Read the tables for loan classification ranges and for IRAC provisioning. The walkthrough showed the grade bands (STD 0–59, SMA 60–89, SS 90–179, DF 180–364, BL 365–1079, WO 1080 and above) and provision rates by grade and security type.

## What you should see

The values above, shown as plain editable tables and tick boxes. The BRD wants grade, provision and income-recognition rules to have an owner, versions and dates, with approved changes (BR-LMS-197); the walkthrough found that anyone with Company write access edits the tables and only the Version log remains.

## If it looks wrong

The BRD wants two accounting modes, the loan system's own ledger or a posting to the core banking system with its journal reference (BR-LMS-115, partly covered). Only the first exists: the settings hold accounts and the two switches, with no CBS option and no outbound journal reference (D13). The verification's fix for versioned grade and provision rules is D5.

For the provision rates by grade, J4 also found the provision accounts empty in the General Ledger (BR-LMS-193). See `bridge.BR-LMS-115`, `bridge.BR-LMS-197` and `bridge.BR-LMS-193`.
