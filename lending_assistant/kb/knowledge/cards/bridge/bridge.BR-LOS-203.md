---
id: bridge.BR-LOS-203
type: bridge
title: "If the account opens but payment fails, the application holds and an exception is raised"
summary: "Not analysed. The team has not compared BR-LOS-203 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-203]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-203"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [concept.BR-LOS-203, concept.BR-LOS-202, concept.BR-LOS-204]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-203 with Frappe Lending, so there is no verdict.

## Business need

“Where account opening succeeds and disbursement fails, the application shall hold at account opened and an exception shall be raised. It shall not be silently retried in a loop.” (BR-LOS-203, BRD 6.9, PDF page 43). See `concept.BR-LOS-203` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-203 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-203 sits in section 6.9. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BR-LOS-213, which describes the exceptions workspace.
2. Ask NRB who should receive an exception raised at account opened.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
