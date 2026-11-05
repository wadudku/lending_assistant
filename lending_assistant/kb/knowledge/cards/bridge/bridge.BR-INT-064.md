---
id: bridge.BR-INT-064
type: bridge
title: Each automation run keeps evidence of what it did
summary: "Not analysed. The team has not compared BR-INT-064 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-064]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-064"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [concept.BR-INT-064]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-064 with Frappe Lending, so there is no verdict.

## Business need

“Each automation run shall retain evidence of what it did — the screens traversed, the values entered and the values read back — sufficient to reconstruct the transaction for audit or dispute, with sensitive content protected under the access rules of Section 4.3.” (BR-INT-064, BRD 9.3, PDF page 63). See `concept.BR-INT-064` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-064 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-064 sits in section 9.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how long the evidence must be kept and who may open it.
2. List what a run would need to store.
3. Check where Frappe Lending keeps files or logs of that kind.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
