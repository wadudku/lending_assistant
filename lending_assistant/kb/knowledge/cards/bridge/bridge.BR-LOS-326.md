---
id: bridge.BR-LOS-326
type: bridge
title: "Approvers cannot approve their own sampled cases or their own organisation's, and dual sanction needs two people"
summary: "Not analysed. The team has not compared BR-LOS-326 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-326]
brd_section: 6.6
doctypes: [Authorization Rule, User Permission]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-326"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-141"
related: [concept.BR-LOS-326]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-326 with Frappe Lending, so there is no verdict.

## Business need

“An approver shall not be able to sanction an application they reviewed at sampling, nor one submitted by an organisation to which their user account is linked. Where the Bank requires dual sanction above a configurable amount, the second approver shall be a different user from the first.” (BR-LOS-326, BRD 6.6, PDF page 38). See `concept.BR-LOS-326` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-326 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Authorization Rule** is ERPNext's document for approval limits; its list of documents holds sales and purchase documents only, such as Sales Order and Purchase Invoice.
- **User Permission** is Frappe's document for limiting which records a user can see.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-326 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List what the two items above can base a rule on.
2. Check whether a rule can refer to a person's earlier action on the same record.
3. Ask NRB for the amount above which dual sanction applies.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
