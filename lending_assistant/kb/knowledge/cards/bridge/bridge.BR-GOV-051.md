---
id: bridge.BR-GOV-051
type: bridge
title: What the daily comparison must find
summary: "Not analysed. The team has not compared BR-GOV-051 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-051]
brd_section: 8.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-051"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p59"
related: [concept.BR-GOV-051]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-051 with Frappe Lending, so there is no verdict.

## Business need

“Reconciliation shall identify, at minimum: loans booked externally but not on the platform; loans approved on the platform but absent externally; amount mismatches; status divergence; and orphaned idempotency keys.” (BR-GOV-051, BRD 8.4, PDF page 59). See `concept.BR-GOV-051` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-051 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-051 sits in section 8.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how a loan booked outside the platform will be identified.
2. List the amount and status fields a loan holds in Frappe Lending.
3. Find where a unique key sent with an instruction would be stored, if the design uses one.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
