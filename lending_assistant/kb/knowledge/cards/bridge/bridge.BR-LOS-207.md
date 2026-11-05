---
id: bridge.BR-LOS-207
type: bridge
title: Payment is blocked when the sanction has lapsed or a sanction condition is not evidenced
summary: "Not analysed. The team has not compared BR-LOS-207 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-207]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-207"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [concept.BR-LOS-207, concept.BR-LOS-202, bridge.BR-LOS-330]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-207 with Frappe Lending, so there is no verdict.

## Business need

“Disbursement shall be blocked where the application's sanction has lapsed under BR-LOS-330, or where a sanction condition remains unevidenced.” (BR-LOS-207, BRD 6.9, PDF page 43). See `concept.BR-LOS-207` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-207 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is a Frappe Lending document with that name.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-207 sits in section 6.9. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BR-LOS-330 in BRD 6.6, which is the row this one refers to.
2. Ask NRB which sanction conditions need evidence before disbursement.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
