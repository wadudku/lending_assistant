---
id: bridge.BR-LOS-220
type: bridge
title: "Partners can list, filter, sort and export their own applications"
summary: "Not analysed. The team has not compared BR-LOS-220 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-220]
brd_section: 6.10.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-220"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.2"
related: [concept.BR-LOS-220, concept.BR-LOS-221, concept.BR-LOS-224, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-220 with Frappe Lending, so there is no verdict.

## Business need

“Partner users shall be able to list, filter, sort and export their own applications. Filters shall include batch, status, submission date range, amount band, district and assigned field officer.” (BR-LOS-220, BRD 6.10.2, PDF page 44). See `concept.BR-LOS-220` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-220 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **User Permission** is Frappe's document for limiting which records a user may open.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-220 sits in section 6.10.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which export formats a partner list should offer, since the BRD says "export" without a format here.
2. Compare the filters with the search keys in BR-LOS-211.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
