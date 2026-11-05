---
id: bridge.BR-LOS-182
type: bridge
title: "Assignment can be done in bulk, with workload shown and a capacity warning"
summary: "Not analysed. The team has not compared BR-LOS-182 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-182]
brd_section: 6.7.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-182"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.4"
related: [concept.BR-LOS-182, concept.BR-LOS-181]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-182 with Frappe Lending, so there is no verdict.

## Business need

“Assignment shall be bulk-capable, shall display each officer's current open workload and coverage area, and shall warn where an assignment would exceed a configurable per-officer daily capacity.” (BR-LOS-182, BRD 6.7.4, PDF page 41). See `concept.BR-LOS-182` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-182 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-182 sits in section 6.7.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the daily capacity per officer, since the BRD calls it configurable and gives no number.
2. Ask NRB whether the person assigning may go over the capacity after a warning, because the BRD only says warn.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
