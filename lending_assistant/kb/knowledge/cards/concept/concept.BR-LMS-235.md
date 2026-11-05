---
id: concept.BR-LMS-235
type: concept
title: "Closure letter, final statement and a message"
summary: "At closure the borrower gets a payoff or closure letter, a final statement of account and a message through the agreed channel."
br_ids: [BR-LMS-235]
brd_section: 7.14
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-235"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-235"
  - "sources/verification/verification_report.md#BR-LMS-235"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-235"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-235"
related: [bridge.BR-LMS-235, brd_section.7.14, concept.BR-LMS-230]
version: 1
status: approved
approved_by: Owner
---
**In short:** At closure the borrower gets a payoff or closure letter, a final statement of account and a message through the agreed channel.

## What the rule says

BR-LMS-235 in section 7.14 (Must, BRD PDF page 56) says that on closure the platform shall produce a payoff or closure confirmation and a final statement of account, and shall notify the borrower through the configured channel.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the borrower needs proof that the debt is paid, and the bank needs proof that the borrower was told.

## Example

Rahim receives an SMS "Your loan is fully paid and closed", a closure letter and a final statement PDF.

## Terms to know

- **Payoff or closure letter:** a printed confirmation that nothing more is owed.
- **Final statement of account:** every posting on the loan, ending at 0.
- **Configured channel:** SMS, email or the bank's chosen way of contacting the borrower.
