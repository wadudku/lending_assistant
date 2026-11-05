---
id: bridge.BR-GOV-053
type: bridge
title: The platform checks its own records against each other
summary: "Not analysed. The team has not compared BR-GOV-053 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-053]
brd_section: 8.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-053"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p59"
related: [concept.BR-GOV-053]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-053 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall reconcile internally across schedule, demand, accrual, repayment allocation and accounting posting, and shall report any internal inconsistency as an exception.” (BR-GOV-053, BRD 8.4, PDF page 59). See `concept.BR-GOV-053` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-053 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-145 (`bridge.BR-LMS-145`) is a related servicing requirement the team analysed, about checking that interest numbers agree. Its result does not apply to BR-GOV-053.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-053 sits in section 8.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the five records the BRD names and where Frappe Lending stores each.
2. Ask NRB which differences should be treated as inconsistencies and which as rounding.
3. Compare that list with the checks that run today.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
