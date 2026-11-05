---
id: concept.BR-LMS-102
type: concept
title: The stages of a loan's life
summary: "A loan moves from booked to active, sometimes through partially disbursed, then to closure requested and finally to closed, settled or written off. Servicing starts only after the money is paid out."
br_ids: [BR-LMS-102]
brd_section: 7.1
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-102"
  - "sources/verification/verification_report.md#BR-LMS-102"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-102"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-102"
related: [bridge.BR-LMS-102, brd_section.7.1, devitem.D2, lifecycle.BOOKED, lifecycle.ACTIVE, lifecycle.PARTIALLY_DISBURSED, lifecycle.CLOSED, lifecycle.SETTLED, lifecycle.WRITTEN_OFF, lifecycle.CLOSURE_REQUESTED, glossary.write-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** A loan moves from booked to active, sometimes through partially disbursed, then to closure requested and finally to closed, settled or written off. Servicing starts only after the money is paid out.

## What the rule says

BR-LMS-102 (priority Must, BRD 7.1, PDF page 46) sets the loan lifecycle. It runs from booked through active, including partially disbursed where a tranche product applies, to closure requested, and then to one of three endings: closed, settled or written off. Servicing ownership begins only after confirmed funding.

## Why the bank wants it

The BRD gives the reason for the last sentence in the rule: servicing ownership begins only after confirmed funding (BR-LMS-102, PDF page 46). For the stage list, the BRD gives no reason in this row. BRD 5.3 defines the twelve servicing states in full (PDF page 27).

## Example

Rahim's loan is booked on 5 June 2026. It is active while he pays his EMIs. When he asks to pay everything off, it moves to closure requested, and when he has paid, to closed. If he had stopped paying for years, the loan might have ended as written off instead.

## Terms to know

- **Partially disbursed:** a tranche loan where part of the approved money is still to be paid out. See `lifecycle.PARTIALLY_DISBURSED`.
- **Closed, settled, written off:** the three endings. Closed means paid in full; settled means the bank accepted less; written off means the bank gave up collecting. See `glossary.write-off`.
- **Booked:** the first stage. See `lifecycle.BOOKED`.
