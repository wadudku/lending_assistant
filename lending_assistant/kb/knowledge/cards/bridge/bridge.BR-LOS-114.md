---
id: bridge.BR-LOS-114
type: bridge
title: Wrong rows can be fixed in the browser or exported for offline correction
summary: "Not analysed. The team has not compared BR-LOS-114 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-114]
brd_section: 6.2
doctypes: [Data Import]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-114"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-113"
related: [concept.BR-LOS-114]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-114 with Frappe Lending, so there is no verdict.

## Business need

“Invalid rows shall be editable in the browser, individually re-validatable without re-uploading the batch, and exportable as a corrections file for offline handling.” (BR-LOS-114, BRD 6.2, PDF page 30). See `concept.BR-LOS-114` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-114 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Data Import** is Frappe's general tool for loading files.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-114 sits in section 6.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Load a test file with errors through the import tool above and see whether rows can be edited before saving.
2. Check whether the failing rows can be downloaded.
3. Ask NRB how a corrected row should be tied back to its batch.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
