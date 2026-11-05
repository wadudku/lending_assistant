---
id: bridge.BR-INT-044
type: bridge
title: "If identity verification is down, the application waits and retries"
summary: "Not analysed. The team has not compared BR-INT-044 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-044]
brd_section: 9.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-044"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [concept.BR-INT-044]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-044 with Frappe Lending, so there is no verdict.

## Business need

“Where verification is unavailable, the application shall hold rather than fail, with automatic retry.” (BR-INT-044, BRD 9.6, PDF page 65). See `concept.BR-INT-044` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-044 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-044 sits in section 9.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the usual length of an outage.
2. List the statuses an application can wait in.
3. Check what the platform shows the officer while it waits.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
