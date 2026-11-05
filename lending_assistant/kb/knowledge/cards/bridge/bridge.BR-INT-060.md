---
id: bridge.BR-INT-060
type: bridge
title: The automation runs only inside the bank's network
summary: "Not analysed. The team has not compared BR-INT-060 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-060]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-060"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-INT-060]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-060 with Frappe Lending, so there is no verdict.

## Business need

“The automation shall execute only within the Bank's network on infrastructure the Bank designates, and shall never transmit Core Banking System content outside that perimeter.” (BR-INT-060, BRD 9.3, PDF page 62). See `concept.BR-INT-060` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-060 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-060 sits in section 9.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which machines will host the automation.
2. List every outside service the platform would send data to.
3. Check whether any of them would receive core banking system content.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
