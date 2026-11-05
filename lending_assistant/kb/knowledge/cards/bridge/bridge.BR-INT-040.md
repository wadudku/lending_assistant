---
id: bridge.BR-INT-040
type: bridge
title: Verify each applicant's identity against the Election Commission Database
summary: "Not analysed. The team has not compared BR-INT-040 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-040]
brd_section: 9.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-040"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [concept.BR-INT-040]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-040 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall verify applicant identity against the Election Commission Database for every submitted application, returning demographic match, portrait and a verification reference. The returned portrait shall be retained for face matching at field verification.” (BR-INT-040, BRD 9.6, PDF page 64). See `concept.BR-INT-040` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-040 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-040 sits in section 9.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how the Election Commission Database is reached.
2. List the items that come back from a check.
3. Find where Frappe Lending would keep a photo and a reference against an application.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
