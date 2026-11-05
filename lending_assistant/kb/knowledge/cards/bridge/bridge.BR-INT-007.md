---
id: bridge.BR-INT-007
type: bridge
title: Post the accounting effects to the core banking system and keep the reference
summary: "Not analysed. The team has not compared BR-INT-007 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-007]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-007"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-INT-007]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-007 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall record approved demand, accrual, charge, restructure, settlement and write-off accounting effects into the Core Banking System, individually or as an agreed batch, and shall retain the resulting voucher or journal reference against the loan.” (BR-INT-007, BRD 9.2.1, PDF page 62). See `concept.BR-INT-007` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-007 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-134 (`bridge.BR-LMS-134`) is a related servicing requirement the team analysed, about sending bills to the CBS and keeping its journal number. Its result does not apply to BR-INT-007.
- BR-LMS-204 (`bridge.BR-LMS-204`) is a related servicing requirement the team analysed, about sending settlements and write-offs to the CBS. Its result does not apply to BR-INT-007.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-007 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which events go one by one and which in a batch.
2. List the event types in the BRD sentence and where Frappe Lending records each.
3. Find where a journal number from outside could be kept against a loan.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
