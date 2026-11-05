---
id: bridge.BR-LOS-206
type: bridge
title: "On a screen the automation does not recognise, the platform stops and does not guess"
summary: "Not analysed. The team has not compared BR-LOS-206 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-206]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-206"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-064"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [concept.BR-LOS-206, glossary.rpa, concept.BR-LOS-204]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-206 with Frappe Lending, so there is no verdict.

## Business need

“Where the automation encounters an unrecognised screen, an unexpected message or an ambiguous outcome, the platform shall halt, hold the application, capture the session evidence and raise an exception for manual resolution. It shall not guess and shall not proceed to the next step.” (BR-LOS-206, BRD 6.9, PDF page 43). See `concept.BR-LOS-206` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-206 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-206 sits in section 6.9. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BR-INT-064 in BRD 9.3, which lists the evidence each automation run keeps, and ask NRB whether that is the session evidence this row means.
2. Read BRD 9.2, which the BRD cites for the automation driving the core banking system.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
