---
id: brd_section.7.12
type: brd_section
title: BRD 7.12 Co-lending and partner economics
summary: "Section 7.12 covers the partner side of co-lending: who the partners are, their shares, their schedules, their credit notes and their reports."
br_ids: []
brd_section: 7.12
doctypes: []
dev_items: [D10, D19]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.12"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.12-co-lending-and-partner-economics"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.12-co-lending-and-partner-economics"
  - "sources/verification/reqs.json#BR-LMS-210"
related: [devitem.D10, devitem.D19, glossary.partner, glossary.fldg]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.12 covers the partner side of co-lending: who the partners are, their shares, their schedules, their credit notes and their reports.

## What this section says

BRD 7.12 (PDF page 55, 5 requirements, BR-LMS-210 to BR-LMS-214) has the platform keep a partner master with the partner, its addresses and the type of first-loss guarantee or risk-sharing in force (210), define the products each partner joins and the share of loan amount and of collection (211), generate the partner's share of each schedule and of ad-hoc charges (212), process partner credit notes and reconcile the partner's position on a cycle (213) and report disbursed, collected and outstanding share, delinquency and guarantee use (214). The last is the only Should in the section; the others are Must.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a co-lent loan has two owners of the cash flows, so each partner's share has to be worked out and reconciled separately from the bank's own. BR-LMS-213 states the reconciliation need (PDF page 55).

## How it meets Frappe Lending

Of the 5 requirements, the verified result on 16.5.1 is 2 covered (210, 211); 2 partly covered (212, 213); 1 a gap (214). Verification moved 1 of these verdicts: 212. Dev items: D10 (reconciliation reports) and D19 (co-lending reports).

## Related cards

Dev items: `devitem.D10`, `devitem.D19`. Terms: `glossary.partner`, `glossary.fldg`.
