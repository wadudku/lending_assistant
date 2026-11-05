---
id: concept.BR-LOS-115
type: concept
title: "The partner can submit the valid rows and keep the rest, with a confirmation summary"
summary: "A partner can submit only the valid part of a batch and keep the rest for correction, and gets a confirmation with the row count, total requested value and exposure against the ceiling."
br_ids: [BR-LOS-115]
brd_section: 6.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-115"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-103"
related: [bridge.BR-LOS-115, concept.BR-LOS-103, concept.BR-LOS-113]
version: 1
status: approved
approved_by: Owner
---
**In short:** A partner can submit only the valid part of a batch and keep the rest for correction, and gets a confirmation with the row count, total requested value and exposure against the ceiling.

## What the rule says

BR-LOS-115 (Must, BRD 6.2, PDF page 30) says the partner can submit the valid subset of a batch and retain the remainder for correction. Submission is confirmed with an explicit summary stating row count, total requested value and the resulting partner exposure against the ceiling. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that good applications should not wait for bad ones, and the partner should see the effect on its ceiling before it commits.

## Example

A batch has 480 valid and 20 invalid rows. The partner submits the 480. The summary reads: 480 rows, total requested 38,400,000, exposure 41,000,000 of a 50,000,000 ceiling. The 20 stay open for correction.

## Terms to know

- **Valid subset:** the rows that passed every check.
- **Remainder:** the rows that did not pass and stay with the partner.
- **Requested value:** the sum of the amounts asked for.
- **Ceiling:** the highest total exposure agreed. See BR-LOS-103.
