---
id: concept.BR-LMS-192
type: concept
title: Keep the history of grade changes
summary: "Every move into or out of the early-warning and bad-loan grades is kept as history, and a past grade is never deleted."
br_ids: [BR-LMS-192]
brd_section: 7.10
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-192"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-192"
  - "sources/verification/verification_report.md#BR-LMS-192"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-192"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-192"
related: [bridge.BR-LMS-192, brd_section.7.10, glossary.sma, glossary.npa, concept.BR-LMS-191]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every move into or out of the early-warning and bad-loan grades is kept as history, and a past grade is never deleted.

## What the rule says

BR-LMS-192 in section 7.10 (Must, BRD PDF page 53) says movement into and out of early-warning and non-performing categories shall be tracked as a history. A prior classification shall never be deleted.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a regulator or auditor may ask what grade a loan had on any past date, and the answer must not depend on someone's memory or on the present figure.

## Example

Rahim's loan is Standard, then SMA on 2 September, then SS on 2 October, then Standard again on 15 November after he pays everything. All the moves stay on record.

## Terms to know

- **Early-warning categories:** grades such as SMA that come before non-performing. See `glossary.sma`.
- **Non-performing (NPA):** the bad-loan state. See `glossary.npa`.
- **History:** a dated list of every change, kept for good.
