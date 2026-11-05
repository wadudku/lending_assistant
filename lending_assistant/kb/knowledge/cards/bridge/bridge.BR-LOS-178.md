---
id: bridge.BR-LOS-178
type: bridge
title: Evidence cannot be changed once sent; a correction is a new capture
summary: "Not analysed. The team has not compared BR-LOS-178 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-178]
brd_section: 6.7.3
doctypes: [Version]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-178"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [concept.BR-LOS-178, concept.BR-LOS-176]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-178 with Frappe Lending, so there is no verdict.

## Business need

“Evidence shall be immutable once synchronised. A correction shall require a new capture, with both retained and the sequence visible in the audit trail.” (BR-LOS-178, BRD 6.7.3, PDF page 41). See `concept.BR-LOS-178` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-178 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's document for the history of changes to other documents.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-178 sits in section 6.7.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how long evidence is kept, since the BRD says both captures are retained.
2. Read BR-LOS-196 in BRD 6.8, which names a retention period for bureau inquiry records, to see whether the Bank has a general retention period.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
