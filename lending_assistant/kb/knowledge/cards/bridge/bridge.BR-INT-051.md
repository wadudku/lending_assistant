---
id: bridge.BR-INT-051
type: bridge
title: "Borrower notices for five events, in Bangla and English"
summary: "Not analysed. The team has not compared BR-INT-051 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-051]
brd_section: 9.7
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-051"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [concept.BR-INT-051]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-051 with Frappe Lending, so there is no verdict.

## Business need

“Borrower notifications shall be issued on disbursement, on instalment due and overdue, on approved term change, on settlement and on closure, through configurable templates in Bangla and English.” (BR-INT-051, BRD 9.7, PDF page 65). See `concept.BR-INT-051` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-051 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-159 (`bridge.BR-LMS-159`) is a related servicing requirement the team analysed, about telling the borrowers. Its result does not apply to BR-INT-051.
- BR-LMS-235 (`bridge.BR-LMS-235`) is a related servicing requirement the team analysed, about a closure letter, a final statement and a message. Its result does not apply to BR-INT-051.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-051 sits in section 9.7. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the wording of each template in both languages.
2. List the notice events in the BRD sentence.
3. Find where Frappe Lending lets a message be written once for many borrowers.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
