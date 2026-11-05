---
id: bridge.BR-LMS-241
type: bridge
title: Every report states when and how it was produced
summary: "Not analysed. The team has not compared BR-LMS-241 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-241]
brd_section: 8.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-241"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [concept.BR-LMS-241]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-241 with Frappe Lending, so there is no verdict.

## Business need

“Every report shall state the date and time it was generated, the parameters used and the data cut-off applied.” (BR-LMS-241, BRD 8.2, PDF page 58). See `concept.BR-LMS-241` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-241 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-241 carries the LMS prefix but sits in BRD section 8.2, outside the 103 requirements of section 7, so it was not analysed.
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-241 sits in section 8.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Open each report the BRD names in section 8.2 and note what its header and filters show.
2. Compare that with the three items the BRD sentence asks every report to state.
3. Ask NRB whether the data cut-off is a date or a time.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
