---
id: bridge.BR-LOS-196
type: bridge
title: Every bureau inquiry is logged in full and kept for the whole retention period
summary: "Not analysed. The team has not compared BR-LOS-196 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-196]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-196"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [concept.BR-LOS-196, concept.BR-LOS-193, concept.BR-LOS-194, glossary.cib]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-196 with Frappe Lending, so there is no verdict.

## Business need

“Every inquiry shall be logged with application reference, initiating officer, timestamp, borrower identifier, inquiry reference, raw response, evaluated outcome and rule version, and retained for the full retention period.” (BR-LOS-196, BRD 6.8, PDF page 42). See `concept.BR-LOS-196` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-196 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- The team's own reports list a Credit Bureau Report doctype that is only in the develop checkout (commit db34994), not in 16.5.1, and say the origination side was out of their scope (FINAL_REPORT.md:266). Nothing about it was tested.
- **Log Settings** is a Frappe document with that name.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-196 sits in section 6.8. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the retention period that applies to bureau logs.
2. Compare the eight items in BR-LOS-196 with the seven items shown in the panel of BR-LOS-193.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
