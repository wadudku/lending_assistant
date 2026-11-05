---
id: concept.BR-LOS-332
type: concept
title: "No sanction if identity failed, a validation is outstanding or the ceiling would break"
summary: "No sanction is issued where identity verification has failed, a mandatory validation is outstanding, or the partner's exposure ceiling would be breached."
br_ids: [BR-LOS-332]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-332"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-103"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
related: [bridge.BR-LOS-332, concept.BR-LOS-103, concept.BR-LOS-120, glossary.nid]
version: 1
status: approved
approved_by: Owner
---
**In short:** No sanction is issued where identity verification has failed, a mandatory validation is outstanding, or the partner's exposure ceiling would be breached.

## What the rule says

BR-LOS-332 (Must, BRD 6.6, PDF page 39) says no sanction is issued where identity verification has failed, a mandatory validation is outstanding, or the partner's exposure ceiling would be breached. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that these are hard stops that no approver should be able to override by accident. The 6.6.1 table shows the route: blocked before sanction and referred to the Bank (PDF page 39).

## Example

An application's NID check failed. The approver opens it and tries to sanction. The platform refuses until the failure is dealt with.

## Terms to know

- **Identity verification:** the check of the applicant against the national database.
- **Mandatory validation:** a check that must be finished before sanction.
- **Outstanding:** not yet finished.
- **Ceiling:** the highest total exposure agreed with the partner. See BR-LOS-103.
