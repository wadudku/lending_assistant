---
id: bridge.BR-LOS-163
type: bridge
title: "Every screen shows connection and sync state, with a queue view"
summary: "Not analysed. The team has not compared BR-LOS-163 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-163]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-163"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
related: [concept.BR-LOS-163, concept.BR-LOS-162, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-163 with Frappe Lending, so there is no verdict.

## Business need

“Connectivity and synchronisation state shall be visible on every screen, and a queue view shall list all pending items with their capture time and sync state.” (BR-LOS-163, BRD 6.7.2, PDF page 40). See `concept.BR-LOS-163` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-163 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None: the BRD puts this step in the field officer's mobile app (BRD 6.7.1), not in the lending system.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-163 sits in section 6.7.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which sync states officers need to see, for example waiting, sent and confirmed.
2. Ask the team that plans the field officer application how the connection state will be shown on every screen without taking up room needed for the work.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
