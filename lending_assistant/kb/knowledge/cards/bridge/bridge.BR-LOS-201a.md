---
id: bridge.BR-LOS-201a
type: bridge
title: If funding takes too long the officer can end the visit and funding finishes later
summary: "Not analysed. The team has not compared BR-LOS-201a with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-201a]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-201a"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [concept.BR-LOS-201a, concept.BR-LOS-201, concept.BR-LOS-209]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-201a with Frappe Lending, so there is no verdict.

## Business need

“Where the automation cannot complete funding within the configured field waiting period, the officer shall be able to conclude the visit at approved status. Funding shall then complete asynchronously and both the borrower and the officer shall be notified of the outcome. The officer shall never be left waiting on an indefinite progress indicator.” (BR-LOS-201a, BRD 6.9, PDF page 43). See `concept.BR-LOS-201a` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-201a in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-201a sits in section 6.9. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB what the configured field waiting period should be.
2. Read BR-LOS-209, which says how the borrower is notified of the disbursement.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
