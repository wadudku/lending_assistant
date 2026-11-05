---
id: bridge.BR-LOS-233
type: bridge
title: Every decision records the configuration version in force so it can be explained later
summary: "Not analysed. The team has not compared BR-LOS-233 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-233]
brd_section: 6.11
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-233"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.11"
related: [concept.BR-LOS-233, concept.BR-LOS-232, concept.BR-LOS-194]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-233 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall record, against every decision it takes, the configuration version in force at that moment, so that a past decision can be explained by reference to the rules then applying.” (BR-LOS-233, BRD 6.11, PDF page 45). See `concept.BR-LOS-233` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-233 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- The team analysed a related servicing requirement, BR-LMS-117 (product rules have versions, start dates and approval). That is not a comparison with BR-LOS-233.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-233 sits in section 6.11. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which decisions the platform takes, since the BRD says "every decision it takes".
2. Compare BR-LOS-233 with BR-LOS-194, which records the rule version against every bureau decision.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
