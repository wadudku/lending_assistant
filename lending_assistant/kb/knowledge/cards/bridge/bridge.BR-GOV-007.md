---
id: bridge.BR-GOV-007
type: bridge
title: "When an outside system is down, the step pauses and retries"
summary: "Not analysed. The team has not compared BR-GOV-007 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-007]
brd_section: 3.4
doctypes: [Error Log]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/hooks.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-007"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-007]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-007 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall degrade gracefully. Unavailability of any external system shall pause the affected step with clear user messaging and automatic retry. It shall never fail an application, corrupt a loan's state, or produce a decision the external system did not give.” (BR-GOV-007, BRD 3.4, PDF page 19). See `concept.BR-GOV-007` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-007 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Error Log** is Frappe's list of errors raised by the code.
- The scheduled jobs that run on their own are listed in `lending/hooks.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-007 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the scheduled jobs in `lending/hooks.py` and what each does when it fails.
2. Test one failing job on a copy of the site and see what is left in the error list.
3. Ask NRB for the outage cases to test and the wording of the user message.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
