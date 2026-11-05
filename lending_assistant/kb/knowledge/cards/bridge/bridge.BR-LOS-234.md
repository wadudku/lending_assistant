---
id: bridge.BR-LOS-234
type: bridge
title: Reference data can be changed without a software release
summary: "Not analysed. The team has not compared BR-LOS-234 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-234]
brd_section: 6.11
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-234"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.11"
related: [concept.BR-LOS-234, concept.BR-LOS-172]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-234 with Frappe Lending, so there is no verdict.

## Business need

“Reference data — districts, upazilas, loan purposes, rejection reason codes, supplementary field definitions — shall be maintainable without a software release.” (BR-LOS-234, BRD 6.11, PDF page 45). See `concept.BR-LOS-234` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-234 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-234 sits in section 6.11. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB who may change reference data and whether changes need approval.
2. Read BR-LOS-172, which describes supplementary fields.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
