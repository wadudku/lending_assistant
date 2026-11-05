---
id: bridge.BR-INT-070
type: bridge
title: A manual fallback for every automated transaction
summary: "Not analysed. The team has not compared BR-INT-070 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-070]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-070"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [concept.BR-INT-070]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-070 with Frappe Lending, so there is no verdict.

## Business need

“A manual fallback shall exist for every automated transaction: authorised Bank staff shall be able to perform the transaction directly in the Core Banking System and record its reference against the application or loan, so that a prolonged automation outage does not halt lending.” (BR-INT-070, BRD 9.3, PDF page 63). See `concept.BR-INT-070` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-070 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-170r (`bridge.BR-LMS-170r`) is a related servicing requirement the team analysed, about catching payments made directly in the CBS. Its result does not apply to BR-INT-070.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-070 sits in section 9.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which staff may do each transaction by hand.
2. List the transactions the automation does, from BR-INT-003 and BR-INT-004 onwards.
3. Check where Frappe Lending could record a reference made outside it.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
