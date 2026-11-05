---
id: concept.BR-GOV-022
type: concept
title: "Nobody approves their own work, and the system enforces it"
summary: "A person cannot approve their own maker action, and the platform enforces this at the point of approval, not only by hiding a button."
br_ids: [BR-GOV-022]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-022"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-GOV-022, glossary.maker-checker, concept.BR-GOV-008]
version: 1
status: approved
approved_by: Owner
---
**In short:** A person cannot approve their own maker action, and the platform enforces this at the point of approval, not only by hiding a button.

## What the rule says

BR-GOV-022 (Must, BRD 4.3, PDF page 23) says a user cannot approve their own maker action. The platform enforces this at the point of approval, not only in the user interface.

## Why the bank wants it

The BRD doesn't say why in this row. It is the control behind maker-checker approval (BR-GOV-008, PDF page 19): two different users are required for every controlled financial change.

## Example

An officer prepares a write-off and then tries to approve it. Even if the screen still shows an approve button, or the request is sent directly, the system refuses because the same person made it.

## Terms to know

- **Maker action:** the step where a person prepares or enters a change.
- **Point of approval:** the moment the approval is saved, as opposed to what the screen shows.
- **Screen:** what people click on; a rule enforced only there can be bypassed.
