---
id: bridge.BR-LOS-132
type: bridge
title: The seed and rate are saved so a pick can be reproduced for audit
summary: "Not analysed. The team has not compared BR-LOS-132 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-132]
brd_section: 6.5
doctypes: [Version]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-132"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-131"
related: [concept.BR-LOS-132]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-132 with Frappe Lending, so there is no verdict.

## Business need

“The selection seed and the rate applied shall be recorded against the batch, such that the selection can be independently reproduced and demonstrated to audit at any future date.” (BR-LOS-132, BRD 6.5, PDF page 36). See `concept.BR-LOS-132` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-132 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's record of changes made to a document.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-132 sits in section 6.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the item above shows the state of a record at an earlier time.
2. Check where a seed and a rate could be stored with a batch.
3. Ask NRB how long selection records must be kept.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
