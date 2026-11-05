---
id: concept.BR-LOS-176
type: concept
title: "Every capture records who, when, on which device and where"
summary: "Each capture stores the device, the officer, the time and the coordinates, and a capture far from the meeting venue is flagged for Bank review, not blocked."
br_ids: [BR-LOS-176]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-176"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [bridge.BR-LOS-176, concept.BR-LOS-173, glossary.meeting-event]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each capture stores the device, the officer, the time and the coordinates, and a capture far from the meeting venue is flagged for Bank review, not blocked.

## What the rule says

BR-LOS-176 (Must, BRD 6.7.3, PDF page 41) says every capture "shall record device identifier, officer identifier, timestamp and geographic coordinates". Where the capture location is "materially distant from the registered meeting venue" the application is flagged for Bank review, and "it shall not be blocked". So four items are stored for each capture, and a far-away capture is reviewed but not stopped.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that stored device, officer, time and place let the bank check afterwards that a capture was made where and when it should have been, and not blocking a distant capture avoids stopping an officer who has a genuine reason, such as a changed venue.

## Example

An officer captures a signature at a place a long way from the venue registered for the meeting. The capture is saved with the device, the officer, the time and the coordinates. The application is flagged for Bank review, and the officer can carry on.

## Terms to know

- **Registered meeting venue:** the venue held on the meeting event record (see BR-LOS-181).
- **Flagged for Bank review:** marked so that Bank staff look at it; the BRD says it is not blocked.
