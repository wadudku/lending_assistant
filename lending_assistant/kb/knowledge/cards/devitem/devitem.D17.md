---
id: devitem.D17
type: devitem
title: D17 Collections escalation
summary: "A planned add-on to Frappe Lending for chasing late payers: contact history, promises to pay, follow-ups and escalation to recovery. Verification showed the base module is develop only, so it is a much bigger item."
br_ids: [BR-LMS-198]
brd_section: 7.10
doctypes: [Loan, Loan Demand]
dev_items: [D17]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D17"
  - "sources/verification/FINAL_REPORT.md#D17"
  - "sources/verification/reqs.json#BR-LMS-198"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-198"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: []
version: 2
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending for chasing late payers: contact history, promises to pay, follow-ups and escalation to recovery. Verification showed the base module is develop only, so it is a much bigger item.

## What we plan to build

The analysis described D17 as extra Collection Case statuses (Escalated to Recovery, Legal), an escalation rule by days past due or a broken promise, and a recovery owner. That plan assumed the collections module exists. Verification found it does not exist in 16.5.1: Collection Case, Collection Case Log, Collection Activity, Promise to Pay, Dunning Rule and Process Collection Dunning are develop only. D17 therefore means building the whole module, or back-porting develop's six doctypes and testing them.

## The gap it closes

BR-LMS-198 asks that delinquent loans enter a collections workflow with contact history, promises to pay and their fulfilment, follow-up scheduling and escalation to recovery. In the test, the Collection Case page was not found, and ERPNext Dunning works on Sales Invoices, not loan demands. BR-LMS-198 moved from partly covered to gap.

## Requirements it closes

BR-LMS-198 (verified as a gap).

## How, size and dependencies

Size: S in the analysis, now L, or M by back-port. Editorial note: counting steps from S to L, this is the largest change of size in the list. The final report drops the framing of extra statuses on the Collection Case. The final report places D17 in step 3, schedule and regulatory.
