---
id: bridge.BR-INT-010
type: bridge
title: "After a failure or odd result, read the real state before trying again"
summary: "Not analysed. The team has not compared BR-INT-010 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-010]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-INT-010]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-010 with Frappe Lending, so there is no verdict.

## Business need

“Where an instruction fails, is interrupted, or produces an unrecognised result, the platform shall re-read the Core Banking System for the definitive state before any retry or status change.” (BR-INT-010, BRD 9.2.1, PDF page 62). See `concept.BR-INT-010` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-010 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-161 (`bridge.BR-LMS-161`) is a related servicing requirement the team analysed, about when a payment counts, once the CBS has confirmed. Its result does not apply to BR-INT-010.
- BR-LMS-162 (`bridge.BR-LMS-162`) is a related servicing requirement the team analysed, about applying each payment only once. Its result does not apply to BR-INT-010.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-010 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which screen shows the final state of an instruction.
2. List the statuses the platform would hold for an instruction in doubt.
3. Compare them with the cases the BRD names: failed, interrupted, unrecognised.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
