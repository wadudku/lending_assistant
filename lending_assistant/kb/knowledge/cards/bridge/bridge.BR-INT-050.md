---
id: bridge.BR-INT-050
type: bridge
title: Send one-time passcodes by SMS for multi-factor sign-in
summary: "Not analysed. The team has not compared BR-INT-050 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-050]
brd_section: 9.7
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-050"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [concept.BR-INT-050]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-050 with Frappe Lending, so there is no verdict.

## Business need

“SMS shall be issued to deliver one-time passcodes for multi-factor authentication.” (BR-INT-050, BRD 9.7, PDF page 65). See `concept.BR-INT-050` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-050 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-050 sits in section 9.7. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which SMS gateway will be used.
2. List how users sign in to Frappe Lending today.
3. Find where a phone number is held for a user.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
