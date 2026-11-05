---
id: bridge.BR-INT-008
type: bridge
title: Raise a controlled reversal of an earlier transaction
summary: "Not analysed. The team has not compared BR-INT-008 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-008]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-INT-008]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-008 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall be able to raise a controlled reversal of a prior transaction, preserving the original event and recording the new reference returned. Where the Core Banking System requires a human authoriser for a reversal, the platform shall raise the reversal as a task with its full supporting detail and shall record the outcome.” (BR-INT-008, BRD 9.2.1, PDF page 62). See `concept.BR-INT-008` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-008 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-008 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which reversals the core banking system lets an automated user raise.
2. Ask NRB who authorises the others.
3. List how Frappe Lending records a reversal of a posting.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
