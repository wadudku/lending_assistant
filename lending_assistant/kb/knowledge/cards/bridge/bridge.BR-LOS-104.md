---
id: bridge.BR-LOS-104
type: bridge
title: Partner administrators manage only their own organisation's users
summary: "Not analysed. The team has not compared BR-LOS-104 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-104]
brd_section: 6.1
doctypes: [User, User Permission]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-104"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [concept.BR-LOS-104]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-104 with Frappe Lending, so there is no verdict.

## Business need

“Partner Admins shall be able to create, suspend and remove users within their own organisation only, subject to a maximum user count set by the Bank.” (BR-LOS-104, BRD 6.1, PDF page 29). See `concept.BR-LOS-104` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-104 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **User** is Frappe's document for a login account.
- **User Permission** is Frappe's document for limiting which records a user can see.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-104 sits in section 6.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the two documents above link a user to an organisation.
2. Check who may create or disable a user, and whether that is limited to one organisation.
3. Ask NRB for the maximum user count per partner and who sets it.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
