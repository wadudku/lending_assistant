---
id: concept.BR-LOS-221
type: concept
title: Partners see a set of eight details for each of their applications
summary: "The application detail a partner sees has eight items, including a masked account number, the full status timeline, the sanctioned amount and any rejection reason."
br_ids: [BR-LOS-221]
brd_section: 6.10.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-221"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.2"
related: [bridge.BR-LOS-221, concept.BR-LOS-222, concept.BR-LOS-210, glossary.field-officer, glossary.sanctioned-amount]
version: 1
status: approved
approved_by: Owner
---
**In short:** The application detail a partner sees has eight items, including a masked account number, the full status timeline, the sanctioned amount and any rejection reason.

## What the rule says

BR-LOS-221 (Must, BRD 6.10.2, PDF page 44) lists what the application detail "shall show to the partner": the submitted KYC summary; the account number masked except the last four digits; the current status; the full status timeline with timestamps; the requested amount; the sanctioned amount and the difference where revised; the rejection reason where rejected; and the assigned field officer name and contact where assigned. That is eight items.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the partner can tell its applicants where they stand, while the masked account number and the limits in BR-LOS-222 keep the rest of the record away from the partner.

## Example

A partner opens one application. They see the KYC summary, the account number with only its last four digits, the status and timeline, the requested and sanctioned amounts, and the name of the assigned field officer.

## Terms to know

- **Masked:** shown with part hidden; here all but the last four digits.
- **Status timeline:** the history of statuses with timestamps, as the BRD uses the term.
