---
id: brd_section.6.4.1
type: brd_section
title: BRD 6.4.1 Recommended decision bands
summary: "Section 6.4.1 shows four illustrative risk bands, each with its recommended decision and what happens next."
br_ids: []
brd_section: 6.4.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.4.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p35"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.4.1 shows four illustrative risk bands, each with its recommended decision and what happens next.

## What this section says

BRD 6.4.1 (PDF page 35) says the bands are illustrative of the structure the platform must support; the actual grades, score ranges, cut-offs and treatments are configuration to be supplied by Credit Risk before go-live. The table has four bands. Low risk: auto-approve; advances automatically, sampled at the reduced rate for the band, never at zero, with the full requested amount and tenor. Moderate risk: auto-approve with treatment; advances automatically, subject to any cap on amount or tenor and to the pricing tier. Elevated risk: refer; sampled mandatorily, and a reviewer reaches an explicit accept, reject or defer decision with a reason code. High risk: decline; terminal with reason codes, not assigned to a field officer, and reversible only by an authorised override under maker-checker.

## Why the bank wants it

The BRD doesn't say why; it says the bands only show the structure, and Credit Risk supplies the real values before go-live (PDF page 35).

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. It describes the origination system (LOS), which the team has not analysed.

## Related cards

Requirements: `concept.BR-LOS-303`, `concept.BR-LOS-307`, `concept.BR-LOS-308`. Related: `brd_section.6.4`.
