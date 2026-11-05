---
id: bridge.BR-LMS-252
type: bridge
title: Every regulatory extract is kept so a return can be reproduced
summary: "Not analysed. The team has not compared BR-LMS-252 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-252]
brd_section: 8.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-252"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [concept.BR-LMS-252]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-252 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall retain every generated regulatory extract, together with the parameters used and the generating user, for the full retention period, so that a submitted return can be reproduced exactly.” (BR-LMS-252, BRD 8.3, PDF page 58). See `concept.BR-LMS-252` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-252 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-252 carries the LMS prefix but sits in BRD section 8.3, outside the 103 requirements of section 7, so it was not analysed.
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-252 sits in section 8.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the retention period of each return.
2. List where Frappe Lending stores a file or a generated report once it is made.
3. Check what is recorded with it about who made it and with which settings.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
