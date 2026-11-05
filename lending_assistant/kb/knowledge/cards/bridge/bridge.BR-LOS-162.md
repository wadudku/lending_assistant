---
id: bridge.BR-LOS-162
type: bridge
title: Data left unsent too long is erased and the check is marked abandoned
summary: "Not analysed. The team has not compared BR-LOS-162 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-162]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-162"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
related: [concept.BR-LOS-162, concept.BR-LOS-161]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-162 with Frappe Lending, so there is no verdict.

## Business need

“Unsynchronised data older than a configurable period shall be purged and the verification marked abandoned. The applicant shall be re-assignable.” (BR-LOS-162, BRD 6.7.2, PDF page 40). See `concept.BR-LOS-162` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-162 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-162 sits in section 6.7.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB what period of unsent data should lead to a purge, since the BRD calls it configurable and gives no number.
2. Read BR-LOS-183, which returns unactioned assignments to the queue, to see how the two rules are meant to work together.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
