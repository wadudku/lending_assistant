---
id: devitem.D14
type: devitem
title: D14 Provisioning engine
summary: "A planned add-on to Frappe Lending that works out, stores and optionally posts the money set aside against expected loan losses, by class and by security cover."
br_ids: [BR-LMS-193]
brd_section: 7.10
doctypes: [Loan, Loan Classification]
dev_items: [D14]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D14"
  - "sources/verification/FINAL_REPORT.md#D14"
  - "sources/verification/reqs.json#BR-LMS-193"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-193"
  - "sources/NRB_LMS_Team_Discussion_Summary.md#4.-proposed-development-custom-app-no-core-changes"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that works out, stores and optionally posts the money set aside against expected loan losses, by class and by security cover.

## What we plan to build

D14 adds a Loan Provisioning Run with an as-on date. For each loan it records the class, the security type (secured, semi-secured or unsecured, from the collateral cover), the base amount, the rate taken from the existing IRAC rate table, the provision and the rule version. A journal entry is optional. The base and the rates follow the Bangladesh Bank circular. It is built in a custom app.

## The gap it closes

BR-LMS-193 asks to calculate provisions by classification and by secured, semi-secured and unsecured status, with configurable percentages, and to keep the calculation basis of each run. Verification confirmed a gap in the live site: only the rate table exists, and nothing calculates or stores provisions.

## Requirements it closes

BR-LMS-193 (gap).

## How, size and dependencies

Size: M, unchanged by verification. The team summary lists the circular list from Bangladesh Bank as an open item for D14, because the provisioning base and rates depend on it. The analysis names D11, D14 and D5 as the big bank-grade pieces; the final report places D14 in step 3.
