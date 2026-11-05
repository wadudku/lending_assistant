---
id: bridge.BR-LMS-231
type: bridge
title: Check the core bank before confirming closure
summary: "Gap (needs the CBS link). Nothing in the closure path calls an outside banking service, and the app has no field to hold a CBS balance."
br_ids: [BR-LMS-231]
brd_section: 7.14
doctypes: [Loan, Loan Repayment, Loan Security Release]
verdict: gap_cbs
analysis_status: verified
dev_items: [D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-231"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-231"
  - "sources/verification/verification_report.md#BR-LMS-231"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-231"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-231"
  - "sources/verification/FINAL_REPORT.md#D13"
related: [concept.BR-LMS-231, bridge.BR-LMS-204, bridge.BR-LMS-230, devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap (needs the CBS link). Nothing in the closure path calls an outside banking service, and the app has no field to hold a CBS balance.

## Business need

Where the CBS owns the books, the platform must check the external account and ledger before closure is confirmed (BR-LMS-231 in section 7.14, BRD PDF page 56). See `concept.BR-LMS-231`.

## Frappe Lending today

A loan is closed from the Loan (the Request Loan Closure call, the Close Loan button, the daily credit-line job), from a **Loan Repayment** (a Loan Closure, or any repayment within the Auto Write Off Amount), or from a **Loan Security Release**, a **Loan Refund** or a **Loan Write Off**; `lifecycle.CLOSED` lists each path. None of them calls an outside service: a search of their code for web requests, CBS or core-banking names finds none. The app has no field for a CBS account or CBS balance on the Loan.

## Match or gap, and why

This is a **gap (needs the CBS link)**, and the verification confirmed it. It was not tested live, because there is no CBS to call; the check is by code reading only (J9). It is the same missing link as BR-LMS-204: the postings are made in this app, and the CBS has to be told, or asked, through a bridge that has to be built.

- The BRD says "where the CBS owns the books", so the rule applies only on that setting. Whether the NRB deployment keeps loan ledgers in the CBS is a question for the bank.

## What to do today

Until the bridge exists, have the Finance team compare the CBS balance with the loan system for each loan before the closure is submitted, and record that it was done.

## Planned fix

Dev item D13 (CBS and RPA posting bridge, sized large) covers this row.
