---
id: concept.BR-LOS-181
type: concept
title: "A meeting event record, with assignment for the whole meeting at once"
summary: "The platform keeps a record for each meeting event with its partner, venue, place, time and attendee numbers, and a whole meeting can be assigned in one action."
br_ids: [BR-LOS-181]
brd_section: 6.7.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-181"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.4"
related: [bridge.BR-LOS-181, concept.BR-LOS-180, glossary.partner, glossary.meeting-event]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform keeps a record for each meeting event with its partner, venue, place, time and attendee numbers, and a whole meeting can be assigned in one action.

## What the rule says

BR-LOS-181 (Must, BRD 6.7.4, PDF page 41) says the platform "shall support a meeting event record" capturing six things: partner, venue, geographic coordinates, scheduled date and time, expected attendee count, and the applications expected to attend. "Assignment shall be possible at meeting level in a single action."

## Why the bank wants it

The BRD doesn't say why; the usual reason is that officers are sent to a meeting, not to one applicant, so the bank needs a record of the meeting and a way to assign everyone expected at it together.

## Example

A partner arranges a meeting at a venue with a date, a time and 40 expected attendees. The meeting event record holds those details and the applications expected to attend. A bank user assigns the whole meeting to one officer in a single action.

## Terms to know

- **Meeting event record:** the platform record of one gathering, with the six items the BRD lists.
- **Expected attendee count:** the number of people expected at the meeting.
