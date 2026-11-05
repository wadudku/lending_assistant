---
id: brd_section.6.7.2
type: brd_section
title: BRD 6.7.2 Working without connectivity
summary: "Section 6.7.2 holds five requirements for working offline, followed by a block that says four steps shall never proceed offline."
br_ids: [BR-LOS-160, BR-LOS-161, BR-LOS-162, BR-LOS-163, BR-LOS-164]
brd_section: 6.7.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-160"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-161"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-162"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-163"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-164"
related: [bridge.BR-LOS-160, bridge.BR-LOS-161, bridge.BR-LOS-162, bridge.BR-LOS-163, bridge.BR-LOS-164, brd_section.6, glossary.cib]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.7.2 holds five requirements for working offline, followed by a block that says four steps shall never proceed offline.

## What this section says

BRD 6.7.2 (PDF page 40) holds five requirements, BR-LOS-160 to BR-LOS-164, all Must. They cover pre-downloading assigned applications and capturing data offline (160), encrypting queued data and purging biometrics after synchronisation (161), purging old unsent data and marking the verification abandoned (162), showing connectivity and sync state with a queue view (163) and treating old sanction data as stale (164).

After the table the BRD adds a block of prose with no reference number (BRD line 2133, PDF page 40), headed "Steps that shall never proceed offline": "Credit bureau verification, final approval, loan account opening and disbursement shall not be performed offline under any circumstance. Where the officer is offline at that point, the application shall hold at verification in progress and shall complete automatically upon reconnection, with the outcome notified to both officer and applicant." It names four steps. It has no requirement id, and this card gives it none.

## Why the bank wants it

The BRD gives the context for section 6.7 on PDF page 39: officers often work in rural places with unreliable mobile data. The BRD doesn't say why the four steps may never be done offline; the usual reason is that they depend on a live answer from another system or move money.

## How it meets Frappe Lending

The team has not analysed the LOS (the origination system, BRD section 6), so this section carries no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7. None of the five rows is among the 103 requirements the team verified. The offline block is BRD text, not a row, and has no verdict either.

## Related cards

Rows: `bridge.BR-LOS-160` to `bridge.BR-LOS-164`. Parent section: `brd_section.6.7`. Section 6 as a whole: `brd_section.6`.
