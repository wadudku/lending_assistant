---
id: bridge.BR-LOS-142
type: bridge
title: A reviewer may pass a case up to a supervisor with a note
summary: "Not analysed. The team has not compared BR-LOS-142 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-142]
brd_section: 6.5.1
doctypes: [Comment, Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-142"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-144"
related: [concept.BR-LOS-142]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-142 with Frappe Lending, so there is no verdict.

## Business need

“A reviewer shall be able to defer an application to a supervisor with a note, rather than being forced to accept or reject.” (BR-LOS-142, BRD 6.5.1, PDF page 37). See `concept.BR-LOS-142` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-142 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Comment** is Frappe's document for a note on a record.
- **Loan Application** is the document Frappe Lending uses for applications.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-142 sits in section 6.5.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the first item above attaches a note to a record.
2. Check whether a record can be assigned to another user.
3. Ask NRB who the supervisors are and how a deferred case reaches them.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
