---
id: bridge.BR-LOS-204
type: bridge
title: Before any retry the platform checks what really happened and never pays twice
summary: "Not analysed. The team has not compared BR-LOS-204 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-204]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-204"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-LOS-204, glossary.idempotency, glossary.rpa, concept.BR-LOS-203]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-204 with Frappe Lending, so there is no verdict.

## Business need

“Before any retry the platform shall re-read the Core Banking System to establish the definitive state of the instruction. It shall never retry on the basis of an incomplete or interrupted automation session. Where an interrupted instruction is found to have executed, success shall be recorded without issuing a second instruction.” (BR-LOS-204, BRD 6.9, PDF page 43). See `concept.BR-LOS-204` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-204 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- The team analysed a related servicing requirement, BR-LMS-100 (accepting only loans that are really paid out). That is not a comparison with BR-LOS-204.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-204 sits in section 6.9. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BR-INT-006 and BR-INT-010 in BRD 9.2.1, which describe the state query before execution and the re-read before any retry.
2. Read BRD 9.2, which the BRD cites for the way the automation drives the core banking system.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
