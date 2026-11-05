---
id: bridge.BR-LMS-159
type: bridge
title: Tell the borrowers
summary: "Gap. There is no repricing event to send a notice from, although a Frappe Notification could be set up on an approved restructure."
br_ids: [BR-LMS-159]
brd_section: 7.6
doctypes: [Loan Restructure]
verdict: gap
analysis_status: verified
dev_items: [D11]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-159"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-159"
  - "sources/verification/verification_report.md#BR-LMS-159"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-159"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-159"
related: [concept.BR-LMS-159, brd_section.7.6, devitem.D11, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. There is no repricing event to send a notice from, although a Frappe Notification could be set up on an approved restructure.

## Business need

The bank wants borrowers told after a repricing is approved and activated (BR-LMS-159, BRD 7.6, PDF page 50). See `concept.BR-LMS-159`.

## Frappe Lending today

Frappe's generic **Notification** can send a message when a document changes. Frappe Lending ships none for repricing (a search of the app's JSON files for a Notification record finds none).

## Match or gap, and why

This is a **gap**. In the test, there was no repricing event, and no Notification existed on Loan, Loan Restructure or Loan Repayment Schedule (verification_report.md, BR-LMS-159, J5). A Notification on Loan Restructure, on the status change to Approved, could be configured for a single loan. The coverage analysis rated it a gap, and verification confirmed that.

## What to do today

Configure a Notification on Loan Restructure for the status change to Approved, and test the message text with the bank's channel.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch.
