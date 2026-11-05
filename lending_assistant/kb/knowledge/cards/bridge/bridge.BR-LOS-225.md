---
id: bridge.BR-LOS-225
type: bridge
title: "The partner portal shows a dashboard of pipeline, conversion and items awaiting the partner"
summary: "Not analysed. The team has not compared BR-LOS-225 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-225]
brd_section: 6.10.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-225"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.2"
related: [concept.BR-LOS-225, concept.BR-LOS-224]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-225 with Frappe Lending, so there is no verdict.

## Business need

“The portal shall present a dashboard showing pipeline volumes and values by status, conversion and drop-off by stage, and items awaiting partner action.” (BR-LOS-225, BRD 6.10.2, PDF page 45). See `concept.BR-LOS-225` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-225 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Dashboard** is Frappe's document for dashboards.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-225 sits in section 6.10.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which stages the dashboard should count.
2. Read BR-LOS-224, which describes partner reports.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
