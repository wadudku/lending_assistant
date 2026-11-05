---
id: concept.BR-LOS-141
type: concept
title: "Each review decision is saved with who, what, why and when"
summary: "The reviewer's identity, decision, reason and timestamp are recorded immutably against the application."
br_ids: [BR-LOS-141]
brd_section: 6.5.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-141"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-144"
related: [bridge.BR-LOS-141, concept.BR-LOS-144, concept.BR-LOS-304, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** The reviewer's identity, decision, reason and timestamp are recorded immutably against the application.

## What the rule says

BR-LOS-141 (Must, BRD 6.5.1, PDF page 37) says reviewer identity, decision, reason and timestamp are recorded immutably against the application. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that sampling decisions are what the 6.5 introduction calls attributable and reproducible, and audit must be able to rely on them (PDF page 35).

## Example

A reviewer accepts an application. The record shows the reviewer's name, “accepted”, the reason entered and the time. Nobody can edit it later; a reversal is a new entry (see BR-LOS-144).

## Terms to know

- **Immutable:** cannot be changed or deleted once written.
- **Reviewer:** the staff member who examines a sampled application.
- **Timestamp:** the date and time of the decision.
- **Attributable:** tied to a named person.
