---
id: concept.BR-LOS-304
type: concept
title: Each score is recorded and cannot be changed afterwards
summary: "Every score is stored with the scorecard version, every attribute value used, each attribute's contribution, the cut-offs in force and the resulting grade and recommendation, and the record cannot be altered."
br_ids: [BR-LOS-304]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-304"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-313"
related: [bridge.BR-LOS-304, concept.BR-LOS-313, glossary.scorecard, glossary.score-cut-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every score is stored with the scorecard version, every attribute value used, each attribute's contribution, the cut-offs in force and the resulting grade and recommendation, and the record cannot be altered.

## What the rule says

BR-LOS-304 (Must, BRD 6.4, PDF page 34) says every score is recorded immutably against the application with the scorecard version applied, the value of every attribute used, the contribution of each attribute to the result, the cut-offs in force and the resulting grade and recommendation. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that audit and the regulator must be able to see exactly how a decision was reached. BR-LOS-313 asks for the same facts to be reproducible later.

## Example

An application is scored on 3 March. The record shows scorecard version 4, income 45,000, instalment-to-income 22%, each attribute’s points, the cut-offs, grade B and “auto-approve”. No one can edit it afterwards.

## Terms to know

- **Immutable:** cannot be changed or deleted once written.
- **Attribute contribution:** how many points one input added or removed.
- **Cut-offs in force:** the cut-offs that applied on the scoring date.
- **Audit:** an independent check of what was done and why.
