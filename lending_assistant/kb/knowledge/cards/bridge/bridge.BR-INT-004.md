---
id: bridge.BR-INT-004
type: bridge
title: Pay out against the opened account and keep the reference and date
summary: "Not analysed. The team has not compared BR-INT-004 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-004]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [concept.BR-INT-004]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-004 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall execute disbursement against an opened loan account to the validated target account, and shall read back and retain the transaction reference and value date as recorded by the Core Banking System.” (BR-INT-004, BRD 9.2.1, PDF page 61). See `concept.BR-INT-004` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-004 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Disbursement** is the Frappe Lending document for a payout.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-004 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which screen records the payout and what it shows afterwards.
2. List the fields a Loan Disbursement holds.
3. Compare them with the transaction reference and value date the BRD names.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
