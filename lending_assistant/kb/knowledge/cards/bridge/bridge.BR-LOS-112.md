---
id: bridge.BR-LOS-112
type: bridge
title: File size and row limits are shown before upload
summary: "Not analysed. The team has not compared BR-LOS-112 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-112]
brd_section: 6.2
doctypes: [Data Import]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-112"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-111"
related: [concept.BR-LOS-112]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-112 with Frappe Lending, so there is no verdict.

## Business need

“File size and row count limits shall be stated on screen before upload, not only in the resulting error.” (BR-LOS-112, BRD 6.2, PDF page 30). See `concept.BR-LOS-112` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-112 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Data Import** is Frappe's general tool for loading files.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-112 sits in section 6.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Open the import tool above and note whether size or row limits are shown before a file is chosen.
2. Ask NRB for the file size and row limits, and whether a partner can have its own.
3. Compare the wording of any limit message with what BR-LOS-111 asks for.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
