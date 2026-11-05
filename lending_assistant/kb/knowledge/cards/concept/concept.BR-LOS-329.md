---
id: concept.BR-LOS-329
type: concept
title: Cases awaiting approval age visibly and escalate on their own
summary: "Applications awaiting credit approval show how long they have waited, escalate automatically after a configured period and are reported with their ageing so that a queue does not delay a scheduled meeting event."
br_ids: [BR-LOS-329]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-329"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-322"
related: [bridge.BR-LOS-329, concept.BR-LOS-322, concept.BR-LOS-325, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Applications awaiting credit approval show how long they have waited, escalate automatically after a configured period and are reported with their ageing so that a queue does not delay a scheduled meeting event.

## What the rule says

BR-LOS-329 (Must, BRD 6.6, PDF page 38) says applications awaiting credit approval age visibly, escalate automatically after a configurable period, and are reported with their ageing so that a queue does not silently delay a scheduled meeting event. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the row itself: so that a queue does not silently delay a scheduled meeting event (PDF page 38).

## Example

A case has waited three days in the queue and shows “3 days”. After the configured two days it moved to a higher level, and the weekly report lists it with its age.

## Terms to know

- **Ageing:** how long a case has been waiting.
- **Meeting event:** a gathering where the field officer meets applicants.
- **Escalate:** pass a case to the next level automatically.
- **Queue:** the list of cases waiting for a decision.
