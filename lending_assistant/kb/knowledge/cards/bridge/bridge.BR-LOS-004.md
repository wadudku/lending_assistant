---
id: bridge.BR-LOS-004
type: bridge
title: Every status change leaves a permanent audit record
summary: "Not analysed. The team has not compared BR-LOS-004 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-004]
brd_section: 5.2
doctypes: [Version, Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-001"
related: [concept.BR-LOS-004]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-004 with Frappe Lending, so there is no verdict.

## Business need

“Every status change shall write an immutable audit record capturing application reference, previous status, new status, actor identity or system process, timestamp, reason code where applicable and free-text reason where captured.” (BR-LOS-004, BRD 5.2, PDF page 27). See `concept.BR-LOS-004` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LOS-004 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's record of changes made to a document.
- **Loan Application** is the document Frappe Lending uses for applications.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-004 sits in section 5.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Open the version record of an application and list what it holds.
2. Compare that list with the fields named in the rule.
3. Check whether a version record can be edited or deleted by any role.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
