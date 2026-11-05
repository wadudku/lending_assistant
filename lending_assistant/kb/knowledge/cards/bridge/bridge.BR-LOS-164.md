---
id: bridge.BR-LOS-164
type: bridge
title: Old downloaded sanction data is refreshed before approval
summary: "Not analysed. The team has not compared BR-LOS-164 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-164]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-164"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
related: [concept.BR-LOS-164, concept.BR-LOS-163]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-164 with Frappe Lending, so there is no verdict.

## Business need

“Where the application has been offline beyond a configurable period, pre-downloaded sanction data shall be treated as stale and refreshed before approval proceeds.” (BR-LOS-164, BRD 6.7.2, PDF page 40). See `concept.BR-LOS-164` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-164 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-164 sits in section 6.7.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB what offline period makes sanction data stale, since the BRD calls it configurable and gives no number.
2. Read the block "Steps that shall never proceed offline" in BRD 6.7.2 (PDF page 40), which says approval cannot be done offline, to see how it relates to BR-LOS-164.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
