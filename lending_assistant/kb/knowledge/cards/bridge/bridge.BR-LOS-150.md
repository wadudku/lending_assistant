---
id: bridge.BR-LOS-150
type: bridge
title: The field officer app runs on Android
summary: "Not analysed. The team has not compared BR-LOS-150 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-150]
brd_section: 6.7.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-150"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.1"
related: [concept.BR-LOS-150, glossary.los, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-150 with Frappe Lending, so there is no verdict.

## Business need

“The field officer application shall run on Android. The minimum supported version is to be confirmed by the Bank based on the standard issued device.” (BR-LOS-150, BRD 6.7.1, PDF page 39). See `concept.BR-LOS-150` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-150 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None: the BRD puts this step in the field officer's mobile app (BRD 6.7.1), not in the lending system.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-150 sits in section 6.7.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which Android version the standard issued device runs, because the BRD leaves the minimum version to the Bank (BR-LOS-150).
2. Ask the team that plans the field officer application whether it is part of the lending system or a separate app, since the BRD calls it "the field officer application".

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
