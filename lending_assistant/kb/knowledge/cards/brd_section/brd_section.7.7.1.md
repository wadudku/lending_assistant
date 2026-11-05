---
id: brd_section.7.7.1
type: brd_section
title: BRD 7.7.1 Requirements that hold whatever the channel
summary: "Section 7.7.1 lists what must be true for every known payment, whatever channel it came through."
br_ids: []
brd_section: 7.7.1
doctypes: []
dev_items: [D9, D10, D12, D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.7.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.7-repayment-collection-and-allocation"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.7-repayment-collection-and-allocation"
  - "sources/verification/reqs.json#BR-LMS-160"
related: [brd_section.7.7, devitem.D9, devitem.D10, devitem.D12, devitem.D13, decision.waiver, glossary.value-date, glossary.posting-date, glossary.allocation-order, glossary.cbs, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.7.1 lists what must be true for every known payment, whatever channel it came through.

## What this section says

BRD 7.7.1 (PDF pages 50 and 51, 12 requirements, BR-LMS-160 to BR-LMS-171) is the part of 7.7 that does not wait for NRB's channel decision. A confirmed payment is recorded with its channel, CBS reference, amount, value date and posting date (160). It counts only after the CBS confirms it (161) and is applied once (162), as at its value date (163), in the set offset order, visible line by line (164). The section covers all repayment types (165), bulk upload (166), an unidentified-receipts queue (167), a payoff figure with approved settlement (168), a controlled repost for corrections (169) and reconciliation with the CBS (170 and 171). BR-LMS-170 and 171 appear twice in the BRD: here for repayments, and in 7.8 for collateral, so this card calls the repayment ones 170r and 171r.

## Why the bank wants it

The BRD gives its reason in the 7.7 introduction (PDF page 50): the deferral on collection and detection does not touch anything downstream of a known payment, so the section states only what holds whatever the channel is.

## How it meets Frappe Lending

Of the 12 requirements, the verified result on 16.5.1 is 4 covered (160, 163, 165, 169); 5 partly covered (161, 164, 166, 167, 168); 1 a gap (162); 2 a gap that needs the CBS link (170r, 171r). Verification moved 2 of these verdicts: 164, 168. Dev items: D12 (payment confirmation and receipts), D13 (the CBS and RPA posting bridge), D9 (batch run and exception framework) and D10 (reconciliation reports). The parent card is `brd_section.7.7`; this card gives the verified counts for the 12 requirements only.

## Related cards

Parent: `brd_section.7.7`. Dev items: `devitem.D9`, `devitem.D10`, `devitem.D12`, `devitem.D13`. Decision: `decision.waiver`. Terms: `glossary.value-date`, `glossary.posting-date`, `glossary.allocation-order`, `glossary.cbs`, `glossary.idempotency`.
