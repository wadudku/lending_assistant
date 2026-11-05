---
id: bridge.BR-LOS-210
type: bridge
title: "Bank staff can open the full application detail, including the data a partner cannot see"
summary: "Not analysed. The team has not compared BR-LOS-210 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-210]
brd_section: 6.10.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-210"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.1"
related: [concept.BR-LOS-210, concept.BR-LOS-193, concept.BR-LOS-222, glossary.cib, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-210 with Frappe Lending, so there is no verdict.

## Business need

“Bank staff shall have access to full application detail: everything visible to the partner, plus credit bureau data in full, the identity verification payload including portrait match confidence and liveness result, field officer captured data, signature image, fingerprint capture metadata and quality score, request and response payloads exchanged with external systems, and the complete audit trail.” (BR-LOS-210, BRD 6.10.1, PDF page 44). See `concept.BR-LOS-210` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-210 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's document for the history of changes to other documents.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-210 sits in section 6.10.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which Bank roles should see each of the seven kinds of detail, since BR-LOS-193 limits the bureau response to separately permissioned Bank users.
2. Compare BR-LOS-210 with BR-LOS-221, which lists what the partner sees.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
