---
id: bridge.BR-INT-002
type: bridge
title: "Account lookups are queued, with an agreed rate or an offline file"
summary: "Not analysed. The team has not compared BR-INT-002 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-002]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [concept.BR-INT-002]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-002 with Frappe Lending, so there is no verdict.

## Business need

“Account enquiry shall be queued and shall sustain the throughput the Bank agrees at design stage. Where a same-day batch cannot be validated at the required rate, the Bank and the supplier shall agree either additional automation capacity or a file-based extract from the Core Banking System against which validation is performed offline.” (BR-INT-002, BRD 9.2.1, PDF page 61). See `concept.BR-INT-002` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-002 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-002 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the batch size and the time allowed to check it.
2. Ask NRB whether the core banking system can produce a daily account file.
3. List how Frappe Lending would hold such a file once loaded.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
