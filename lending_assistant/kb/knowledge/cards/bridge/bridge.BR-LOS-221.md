---
id: bridge.BR-LOS-221
type: bridge
title: Partners see a set of eight details for each of their applications
summary: "Not analysed. The team has not compared BR-LOS-221 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-221]
brd_section: 6.10.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-221"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.2"
related: [concept.BR-LOS-221, concept.BR-LOS-222, concept.BR-LOS-210, glossary.field-officer, glossary.sanctioned-amount]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-221 with Frappe Lending, so there is no verdict.

## Business need

“Application detail shall show to the partner: submitted KYC summary; account number masked except the last four digits; current status; the full status timeline with timestamps; requested amount; sanctioned amount and the difference where revised; rejection reason where rejected; and assigned field officer name and contact where assigned.” (BR-LOS-221, BRD 6.10.2, PDF page 44). See `concept.BR-LOS-221` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-221 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-221 sits in section 6.10.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB what the KYC summary contains, since the BRD only calls it a summary.
2. Compare BR-LOS-221 with BR-LOS-210, which says Bank staff see everything the partner sees and more.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
