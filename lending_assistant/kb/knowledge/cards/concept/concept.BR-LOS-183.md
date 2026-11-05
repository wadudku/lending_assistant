---
id: concept.BR-LOS-183
type: concept
title: Assignments can be reassigned and unactioned ones go back to the queue
summary: "An assignment can be given to someone else with a recorded reason, and one not acted on within a set time returns to the queue and is reported."
br_ids: [BR-LOS-183]
brd_section: 6.7.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-183"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.4"
related: [bridge.BR-LOS-183, concept.BR-LOS-182, concept.BR-LOS-162]
version: 1
status: approved
approved_by: Owner
---
**In short:** An assignment can be given to someone else with a recorded reason, and one not acted on within a set time returns to the queue and is reported.

## What the rule says

BR-LOS-183 (Must, BRD 6.7.4, PDF page 41) says assignments "shall be reassignable with a recorded reason". Assignments not actioned within a configurable period "shall return automatically to the queue and shall be reported". Two things follow: a reassignment always carries a reason, and an idle assignment comes back without anyone moving it.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an assignment that sits unactioned holds an applicant back, so the bank wants it released and reported, and a recorded reason lets someone explain a change later.

## Example

An officer falls ill and an assignment is reassigned, with the reason "officer unavailable" recorded. Another assignment is not acted on within the configured period, so it returns to the queue by itself and appears in a report.

## Terms to know

- **Reassign:** give an assignment to a different officer.
- **Return to the queue:** put the application back among those waiting to be assigned.
