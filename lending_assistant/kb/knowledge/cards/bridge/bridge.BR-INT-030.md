---
id: bridge.BR-INT-030
type: bridge
title: "The bureau inquiry runs from a designated host, through automation, under the same controls"
summary: "Not analysed. The team has not compared BR-INT-030 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-030]
brd_section: 9.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-030"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [concept.BR-INT-030]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-030 with Frappe Lending, so there is no verdict.

## Business need

“Bureau inquiry shall execute from a designated host within the Bank's permitted network perimeter, through robotic process automation driving the bureau interface, and shall be subject to the same controls as Section 9.3.” (BR-INT-030, BRD 9.5, PDF page 64). See `concept.BR-INT-030` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-030 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- The team's verification notes list a Credit Bureau Report document type as present in the develop version of Frappe Lending and not in 16.5.1. The team did not compare it with BR-INT-030.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-030 sits in section 9.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which host will run the inquiry.
2. Read section 9.3 for the controls the BRD names.
3. List the steps of a bureau inquiry that the platform would start.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
