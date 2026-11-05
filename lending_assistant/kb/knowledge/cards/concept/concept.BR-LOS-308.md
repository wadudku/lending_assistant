---
id: concept.BR-LOS-308
type: concept
title: A score-declined application gets its own final status and is not shown the score
summary: "An application declined by score takes a distinct final status with reason codes, is not given to a field officer, and is reported to the partner as declined without the score, grade or scorecard logic."
br_ids: [BR-LOS-308]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-308"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-305"
related: [bridge.BR-LOS-308, concept.BR-LOS-305, concept.BR-LOS-314, glossary.scorecard, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** An application declined by score takes a distinct final status with reason codes, is not given to a field officer, and is reported to the partner as declined without the score, grade or scorecard logic.

## What the rule says

BR-LOS-308 (Must, BRD 6.4, PDF page 34) says an application declined by score takes a distinct terminal status with its reason codes, is not assigned to a field officer, and is reported to the partner as declined without disclosure of the score, the grade or the scorecard logic. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that showing a partner how the score works would let it shape applications to pass, and a declined case needs no field visit.

## Example

A score-declined application is marked “Declined by score” with two reason codes. No field officer receives it. The partner’s screen says “declined” and nothing more about the score or grade.

## Terms to know

- **Terminal status:** a final status: nothing further happens.
- **Field officer:** the bank's staff member who meets the applicant.
- **Disclosure:** showing information to someone.
- **Scorecard logic:** the attributes and weights behind the score.
