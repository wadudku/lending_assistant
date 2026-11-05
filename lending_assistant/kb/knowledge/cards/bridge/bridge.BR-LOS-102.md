---
id: bridge.BR-LOS-102
type: bridge
title: A suspended partner can look but not send new batches
summary: "Not analysed. The team has not compared BR-LOS-102 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-102]
brd_section: 6.1
doctypes: [User Permission, Loan Partner]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [concept.BR-LOS-102]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-102 with Frappe Lending, so there is no verdict.

## Business need

“A suspended partner's users shall retain read access to existing applications but shall be prevented from submitting new batches. Applications already in flight shall continue to be processed unless separately halted.” (BR-LOS-102, BRD 6.1, PDF page 29). See `concept.BR-LOS-102` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-102 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **User Permission** is Frappe's document for limiting which records a user can see.
- **Loan Partner** is the Frappe Lending document for a co-lending partner.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-102 sits in section 6.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Check whether the partner document above has a field for a partner's status.
2. Check whether a status change alters what the partner's users can do.
3. Ask NRB which actions a suspended partner may and may not take.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
