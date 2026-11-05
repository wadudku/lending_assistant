---
id: bridge.BR-LOS-127
type: bridge
title: Check requests are queued and paced to what the bank's system can take
summary: "Not analysed. The team has not compared BR-LOS-127 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-127]
brd_section: 6.3
doctypes: [RQ Job]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-127"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-126"
related: [concept.BR-LOS-127]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-127 with Frappe Lending, so there is no verdict.

## Business need

“Validation requests shall be queued and rate-limited to the throughput the Core Banking System and the available automation capacity can sustain. Queue depth shall never surface to the partner as an error.” (BR-LOS-127, BRD 6.3, PDF page 32). See `concept.BR-LOS-127` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-127 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **RQ Job** is Frappe's list of background jobs.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-127 sits in section 6.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List what the background-job list above shows about waiting and running jobs.
2. Check whether a limit on jobs per period can be set.
3. Ask NRB for the number of checks per hour the automation can sustain.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
