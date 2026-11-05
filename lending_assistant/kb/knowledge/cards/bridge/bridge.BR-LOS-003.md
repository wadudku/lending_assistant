---
id: bridge.BR-LOS-003
type: bridge
title: Idle applications expire automatically
summary: "Not analysed. The team has not compared BR-LOS-003 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-003]
brd_section: 5.2
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/hooks.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-001"
related: [concept.BR-LOS-003]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-003 with Frappe Lending, so there is no verdict.

## Business need

“Applications shall automatically move to EXPIRED after a configurable period in any non-terminal status. Default periods are to be confirmed by the Bank.” (BR-LOS-003, BRD 5.2, PDF page 27). See `concept.BR-LOS-003` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LOS-003 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The scheduled jobs that run on their own are listed in `lending/hooks.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-003 sits in section 5.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the scheduled jobs in `lending/hooks.py` that touch applications.
2. Read the application document above for a field that holds an expiry period.
3. Ask NRB for the default expiry period of each status.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
