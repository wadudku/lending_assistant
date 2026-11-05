---
id: bridge.BR-INT-006
type: bridge
title: A compensating control stands in for idempotency
summary: "Not analysed. The team has not compared BR-INT-006 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-006]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-INT-006]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-006 with Frappe Lending, so there is no verdict.

## Business need

“Because the Core Banking System does not support idempotency natively, the platform shall implement the compensating control agreed with the Bank: a pre-execution state query, execution carrying the unique reference, a post-execution verification, and a blocking exception on any ambiguity. This control shall be documented and tested as a risk mitigation, and shall not be represented as equivalent to transactional idempotency.” (BR-INT-006, BRD 9.2.1, PDF page 62). See `concept.BR-INT-006` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-006 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-162 (`bridge.BR-LMS-162`) is a related servicing requirement the team analysed, about applying each payment only once. Its result does not apply to BR-INT-006.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-006 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which screen shows an instruction's state before and after it runs.
2. List the instructions the platform would send to the core banking system.
3. Compare that list with the four steps of the control.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
