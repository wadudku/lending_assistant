---
id: bridge.BR-INT-012
type: bridge
title: Reach the core banking system through a single adapter
summary: "Not analysed. The team has not compared BR-INT-012 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-012]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-012"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-INT-012]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-012 with Frappe Lending, so there is no verdict.

## Business need

“The Core Banking System shall be reached through a single adapter, so that if the Bank later acquires an application interface or middleware the automation can be replaced behind that adapter without change to the origination or servicing engine.” (BR-INT-012, BRD 9.2.1, PDF page 62). See `concept.BR-INT-012` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-012 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-012 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB whether an interface or middleware is planned.
2. List every place the platform would call the core banking system.
3. Check whether those places could be routed through one component.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
