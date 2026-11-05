---
id: bridge.BR-INT-069
type: bridge
title: "When the automation is down, the step pauses and retries"
summary: "Not analysed. The team has not compared BR-INT-069 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-069]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-069"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [concept.BR-INT-069]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-069 with Frappe Lending, so there is no verdict.

## Business need

“Where the automation is unavailable, the affected step shall pause with clear user messaging and automatic retry. It shall never fail an application, corrupt a loan's state, or produce an outcome the Core Banking System did not give.” (BR-INT-069, BRD 9.3, PDF page 63). See `concept.BR-INT-069` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-069 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-069 sits in section 9.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the steps in origination and servicing that call the core banking system.
2. Check what each one shows the user when the call cannot be made.
3. Ask NRB for the longest outage it plans for.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
