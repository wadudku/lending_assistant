---
id: bridge.BR-LOS-235
type: bridge
title: Configuration can be exported and imported between environments
summary: "Not analysed. The team has not compared BR-LOS-235 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-235]
brd_section: 6.11
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-235"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.11"
related: [concept.BR-LOS-235, concept.BR-LOS-232]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-235 with Frappe Lending, so there is no verdict.

## Business need

“Configuration shall be exportable and importable between environments to support controlled promotion from test to production.” (BR-LOS-235, BRD 6.11, PDF page 45). See `concept.BR-LOS-235` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-235 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Data Import** is Frappe's document for importing data from a file.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-235 sits in section 6.11. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which environments are in use and who approves promotion to production, since the BRD speaks of "controlled" promotion.
2. Read BR-LOS-232, which asks for a change history on all configuration.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
