---
id: devitem.D4
type: devitem
title: D4 Floating-rate setup
summary: "A planned add-on to Frappe Lending that records whether a loan's rate is fixed or floating, which benchmark it follows, the spread and when it reprices."
br_ids: [BR-LMS-111]
brd_section: 7.2
doctypes: [Loan, Loan Product]
dev_items: [D4]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D4"
  - "sources/verification/FINAL_REPORT.md#D4"
  - "sources/verification/reqs.json#BR-LMS-111"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-111"
  - "sources/verification/verification_report.md#BR-LMS-111"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that records whether a loan's rate is fixed or floating, which benchmark it follows, the spread and when it reprices.

## What we plan to build

D4 adds custom fields on the Loan Product and the Loan: a rate type (fixed or floating), a benchmark linked to a new Reference Rate record that holds dated values, a spread, a repricing frequency and the next repricing date. It is built in a custom app, without changing Frappe Lending.

## The gap it closes

BR-LMS-111 asks the system to store the interest rate, how it is calculated and whether it is fixed or floating. In the test there was no fixed or floating flag, no benchmark and no repricing frequency, and the verdict stayed partly covered. Verification also found that rates are copied at booking.

## Requirements it closes

BR-LMS-111 (verified partly covered). D4 is the data foundation for the repricing run in `devitem.D11`.

## How, size and dependencies

Size: S (under a week), unchanged by verification. Because rates are copied at booking, repricing has to update each Loan, which is the job of D11. The team summary places D4 in its fourth phase, completion.
