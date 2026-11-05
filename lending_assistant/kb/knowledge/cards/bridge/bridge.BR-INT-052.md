---
id: bridge.BR-INT-052
type: bridge
title: "A failed notification is retried and reported, and never blocks a loan action"
summary: "Not analysed. The team has not compared BR-INT-052 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-052]
brd_section: 9.7
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-052"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [concept.BR-INT-052]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-052 with Frappe Lending, so there is no verdict.

## Business need

“Notification failure shall be retried and reported. It shall never block or reverse a loan action.” (BR-INT-052, BRD 9.7, PDF page 65). See `concept.BR-INT-052` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-052 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-052 sits in section 9.7. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how many retries and over what period.
2. List where a message is sent in the middle of a loan action.
3. Check what happens to that action if the message fails.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
