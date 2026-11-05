---
id: bridge.BR-LOS-222
type: bridge
title: "Partners never see bureau data, identity images, scores, sampling, officer notes or another partner's data"
summary: "Not analysed. The team has not compared BR-LOS-222 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-222]
brd_section: 6.10.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-222"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.2"
related: [concept.BR-LOS-222, concept.BR-LOS-221, concept.BR-LOS-191, glossary.sampling, glossary.cib, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-222 with Frappe Lending, so there is no verdict.

## Business need

“Partners shall not have access to credit bureau data of any kind, identity images or match scores, sampling selection or outcome detail, field officer notes, internal reference data, or any data belonging to another partner.” (BR-LOS-222, BRD 6.10.2, PDF page 44). See `concept.BR-LOS-222` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-222 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **User Permission** is Frappe's document for limiting which records a user may open.
- **Role** is Frappe's list of roles that permissions are given to.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-222 sits in section 6.10.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the list of internal reference data, since the BRD does not give one.
2. Compare BR-LOS-222 with BR-LOS-191, which keeps bureau detail off the officer's device.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
