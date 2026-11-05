---
id: bridge.BR-LOS-136
type: bridge
title: The rate screen shows how much review work the rate creates
summary: "Not analysed. The team has not compared BR-LOS-136 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-136]
brd_section: 6.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-136"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-135"
related: [concept.BR-LOS-136]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-136 with Frappe Lending, so there is no verdict.

## Business need

“The configuration screen shall express the rate in operational terms as well as a percentage — for example, how many applications the rate would have selected from the partner's most recent batch — so that the person setting it understands the review workload being created.” (BR-LOS-136, BRD 6.5, PDF page 36). See `concept.BR-LOS-136` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-136 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-136 sits in section 6.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB where the size of a partner's most recent batch is kept today.
2. Ask NRB which workload figures the person setting the rate needs.
3. Compare this row with BR-LOS-135 on who may change the rate.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
