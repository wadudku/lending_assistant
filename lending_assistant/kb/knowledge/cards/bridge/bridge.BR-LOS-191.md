---
id: bridge.BR-LOS-191
type: bridge
title: "The device never receives, shows, keeps or logs any bureau detail"
summary: "Not analysed. The team has not compared BR-LOS-191 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-191]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [concept.BR-LOS-191, concept.BR-LOS-190, concept.BR-LOS-192]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-191 with Frappe Lending, so there is no verdict.

## Business need

“The device shall never receive, display, cache or log any bureau detail: no score, no exposure figures, no institution names, no classification, no account counts.” (BR-LOS-191, BRD 6.8, PDF page 42). See `concept.BR-LOS-191` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-191 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-191 sits in section 6.8. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB whether any field in the officer application will hold a copy of the bureau result, since the BRD says the device receives only pass or fail (BR-LOS-190).
2. Read BR-LOS-190 and BR-LOS-192, which describe what the device is told instead.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
