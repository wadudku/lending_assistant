---
id: bridge.BR-INT-021
type: bridge
title: Servicing reports loan status back to origination
summary: "Not analysed. The team has not compared BR-INT-021 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-021]
brd_section: 9.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-021"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [concept.BR-INT-021]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-021 with Frappe Lending, so there is no verdict.

## Business need

“Servicing shall expose loan account status, sanctioned amount, disbursement date, tenor, instalment amount and arrears position back to origination, for partner disbursed-account views, for partner quality monitoring and for scorecard performance monitoring under BR-LOS-312.” (BR-INT-021, BRD 9.4, PDF page 64). See `concept.BR-INT-021` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-021 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-021 sits in section 9.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how origination is to read the six items.
2. List where Frappe Lending holds each of the six items for a loan.
3. Read BR-LOS-312 in the BRD for the scorecard use.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
