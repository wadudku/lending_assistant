---
id: bridge.BR-LOS-183
type: bridge
title: Assignments can be reassigned and unactioned ones go back to the queue
summary: "Not analysed. The team has not compared BR-LOS-183 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-183]
brd_section: 6.7.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-183"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.4"
related: [concept.BR-LOS-183, concept.BR-LOS-182, concept.BR-LOS-162]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-183 with Frappe Lending, so there is no verdict.

## Business need

“Assignments shall be reassignable with a recorded reason. Assignments not actioned within a configurable period shall return automatically to the queue and shall be reported.” (BR-LOS-183, BRD 6.7.4, PDF page 41). See `concept.BR-LOS-183` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-183 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-183 sits in section 6.7.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the period after which an unactioned assignment returns to the queue.
2. Read BR-LOS-162, which makes an applicant assignable again after abandoned data is purged, to see how the two rules relate.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
