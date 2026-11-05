---
id: bridge.BR-LOS-176
type: bridge
title: "Every capture records who, when, on which device and where"
summary: "Not analysed. The team has not compared BR-LOS-176 with Frappe Lending, so there is no verdict."
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
related: [concept.BR-LOS-176, concept.BR-LOS-173, glossary.meeting-event]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-176 with Frappe Lending, so there is no verdict.

## Business need

“Every capture shall record device identifier, officer identifier, timestamp and geographic coordinates. Where the capture location is materially distant from the registered meeting venue the application shall be flagged for Bank review; it shall not be blocked.” (BR-LOS-176, BRD 6.7.3, PDF page 41). See `concept.BR-LOS-176` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-176 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-176 sits in section 6.7.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB what distance counts as materially distant, since the BRD does not give one.
2. Read BR-LOS-181, which gives the meeting event record its venue and coordinates.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
