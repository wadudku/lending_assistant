---
id: bridge.BR-LOS-135
type: bridge
title: "Sampling rates are set globally, per partner and per product, with a second approver"
summary: "Not analysed. The team has not compared BR-LOS-135 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-135]
brd_section: 6.5
doctypes: [Version, Authorization Rule]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-135"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-133"
related: [concept.BR-LOS-135]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-135 with Frappe Lending, so there is no verdict.

## Business need

“Sampling rates shall be configurable globally, per partner and per product. Changes shall require maker-checker approval, shall be effective-dated, and shall be retained in a change history recording before value, after value, maker, checker, timestamp and stated justification.” (BR-LOS-135, BRD 6.5, PDF page 36). See `concept.BR-LOS-135` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-135 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's record of changes made to a document.
- **Authorization Rule** is ERPNext's document for approval limits; its list of documents holds sales and purchase documents only, such as Sales Order and Purchase Invoice.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-135 sits in section 6.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the two items above record a change, who made it and when.
2. Check whether a change can start on a later date and be held for a second person's approval.
3. Ask NRB who in Credit Risk may propose and who may approve a rate change.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
