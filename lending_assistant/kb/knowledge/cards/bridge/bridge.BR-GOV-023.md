---
id: bridge.BR-GOV-023
type: bridge
title: A sampling reviewer cannot review their own organisation's or their own earlier cases
summary: "Not analysed. The team has not compared BR-GOV-023 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-023]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-023"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [concept.BR-GOV-023]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-023 with Frappe Lending, so there is no verdict.

## Business need

“A sampling reviewer shall not be able to review an application submitted by an organisation to which their user account is linked, nor one they have previously decided.” (BR-GOV-023, BRD 4.3, PDF page 23). See `concept.BR-GOV-023` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-023 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-023 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Find out whether the lending app has any sampling or review step for applications.
2. Read the application code for a check on who may review an application.
3. Ask NRB how a user account is linked to an organisation.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
