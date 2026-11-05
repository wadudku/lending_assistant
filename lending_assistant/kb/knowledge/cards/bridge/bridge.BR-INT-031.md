---
id: bridge.BR-INT-031
type: bridge
title: The bureau automation is monitored and alerts on repeated failure
summary: "Not analysed. The team has not compared BR-INT-031 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-031]
brd_section: 9.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-031"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [concept.BR-INT-031]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-031 with Frappe Lending, so there is no verdict.

## Business need

“The automation component shall be monitored for failure and for interface change, and shall alert on consecutive failures rather than degrading silently.” (BR-INT-031, BRD 9.5, PDF page 64). See `concept.BR-INT-031` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-031 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-031 sits in section 9.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB who receives the alert.
2. List the signs of failure the monitor would watch.
3. Compare them with the five things listed for the core banking system automation in BR-INT-066.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
