---
id: bridge.BR-INT-072
type: bridge
title: The daily reconciliation checks every instruction in both directions
summary: "Not analysed. The team has not compared BR-INT-072 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-072]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-072"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [concept.BR-INT-072]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-072 with Frappe Lending, so there is no verdict.

## Business need

“Daily reconciliation under Section 8.4 shall compare every instruction the platform believes it issued against the transactions actually present in the Core Banking System, in both directions, and shall raise every difference as an exception requiring documented closure.” (BR-INT-072, BRD 9.3, PDF page 63). See `concept.BR-INT-072` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-072 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-171r (`bridge.BR-LMS-171r`) is a related servicing requirement the team analysed, about matching every payment end to end. Its result does not apply to BR-INT-072.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-072 sits in section 9.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how the core banking system's daily transaction list can be obtained.
2. List where the platform records the instructions it issued.
3. Compare the two lists on one sample day.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
