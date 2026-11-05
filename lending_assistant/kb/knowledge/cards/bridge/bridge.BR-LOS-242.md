---
id: bridge.BR-LOS-242
type: bridge
title: "Origination reports can be exported, scheduled and emailed"
summary: "Not analysed. The team has not compared BR-LOS-242 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-242]
brd_section: 8.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-242"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p57"
related: [concept.BR-LOS-242]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-242 with Frappe Lending, so there is no verdict.

## Business need

“Reports shall be exportable to XLSX and CSV, schedulable, and deliverable to configured recipients by email.” (BR-LOS-242, BRD 8.1, PDF page 57). See `concept.BR-LOS-242` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LOS-242 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-242 sits in section 8.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB who the recipients are and how often each report is wanted.
2. Open the reports named in BR-LOS-241 in Frappe Lending and note which export formats they offer.
3. Find out how a report is set to run on a schedule and be sent by email.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
