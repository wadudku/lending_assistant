---
id: bridge.BR-LOS-131
type: bridge
title: The random pick must use a sound random source
summary: "Not analysed. The team has not compared BR-LOS-131 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-131]
brd_section: 6.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-131"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p35"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-130"
related: [concept.BR-LOS-131]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-131 with Frappe Lending, so there is no verdict.

## Business need

“Selection shall use a cryptographically sound random source. A predictable or sequence-based selection is not acceptable.” (BR-LOS-131, BRD 6.5, PDF page 35). See `concept.BR-LOS-131` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-131 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-131 sits in section 6.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which standard for random numbers the Bank requires.
2. Ask which component of the platform is to make the pick.
3. Compare this row with BR-LOS-132, which asks for the pick to be reproducible.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
