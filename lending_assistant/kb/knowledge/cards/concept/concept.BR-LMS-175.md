---
id: concept.BR-LMS-175
type: concept
title: Collateral reports
summary: "The platform reports collateral exposure by borrower and in total, a ledger of every collateral event, and the current status of every pledged item."
br_ids: [BR-LMS-175]
brd_section: 7.8
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-175"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-175"
  - "sources/verification/verification_report.md#BR-LMS-175"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-175"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-175"
related: [bridge.BR-LMS-175, brd_section.7.8]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform reports collateral exposure by borrower and in total, a ledger of every collateral event, and the current status of every pledged item.

## What the rule says

BR-LMS-175 in section 7.8 (Must, BRD PDF page 53) says the platform reports security exposure by applicant and in aggregate, the security event ledger, and the current status of every pledged item.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that credit and risk teams need to see at a glance how much collateral backs the book and what has happened to each item.

## Example

Rahim has loans of 100,000 and eligible collateral of 135,000. The status report shows FDR-001 pledged since 5 June.

## Terms to know

- **Exposure:** how much collateral backs the lending, by borrower or in total.
- **Ledger:** the dated list of pledges and releases.
- **Status:** where each pledged item stands now.
