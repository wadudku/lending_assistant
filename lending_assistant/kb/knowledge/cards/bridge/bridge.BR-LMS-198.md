---
id: bridge.BR-LMS-198
type: bridge
title: Chasing late payers (collections)
summary: "Gap. Frappe Lending 16.5.1 has no collections documents at all; the Collection Case, Collection Activity, Promise to Pay and Dunning Rule documents exist only in the develop branch (develop only). The original analysis said partly covered."
br_ids: [BR-LMS-198]
brd_section: 7.10
doctypes: [Loan]
verdict: gap
analysis_status: verified
dev_items: [D17]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-198"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-198"
  - "sources/verification/verification_report.md#BR-LMS-198"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-198"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-198"
  - "sources/verification/FINAL_REPORT.md#D17"
related: [concept.BR-LMS-198, concept.BR-LMS-198, devitem.D17]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. Frappe Lending 16.5.1 has no collections documents at all; the Collection Case, Collection Activity, Promise to Pay and Dunning Rule documents exist only in the develop branch (develop only). The original analysis said partly covered.

## Business need

Late loans must go through a collections workflow with contact history, promises to pay, follow-up dates and escalation (BR-LMS-198 in section 7.10, BRD PDF page 54). See `concept.BR-LMS-198`.

## Frappe Lending today

Nothing in the installed 16.5.1. The lending app has no document for a collection case, a collection activity or a promise to pay, and no dunning rule. ERPNext has a Dunning document, but it belongs to overdue Sales Invoices and has no loan or demand field. The earlier analysis listed Collection Case, Collection Activity, Promise to Pay and Dunning Rule as present; the verification found those six documents (the three above, Collection Case Log, Dunning Rule and Process Collection Dunning) only in the develop code, commit db34994, which is not what is installed.

## Match or gap, and why

This is a **gap**. The original analysis said partly covered, and the verification moved it because a feature that exists only in develop counts as missing on 16.5.1 (J4).

- In the test, none of the six documents existed on the site, the page for a collection case was not found, and the Loan had no collection, promise or escalation field.
- So there is no contact log, no promise to pay and whether it was kept, no follow-up date and no escalation.
- The test for the collections journey (C7) could not be run.

## What to do today

Run collections outside the system, with a register of calls, promises and visits per loan, and enter the outcome in the Loan remarks. Treat the days past due as the escalation trigger.

## Planned fix

Dev item D17 (collections escalation) covers this row. The final report says the base module exists only in develop, so the choice is to build all of it or to back-port develop's six documents and test them. It sizes the item large, or medium by back-port.
