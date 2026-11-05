---
id: bridge.BR-LOS-174
type: bridge
title: "A fingerprint is captured, with a quality score where hardware allows"
summary: "Not analysed. The team has not compared BR-LOS-174 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-174]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-174"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [concept.BR-LOS-174, concept.BR-LOS-173, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-174 with Frappe Lending, so there is no verdict.

## Business need

“A fingerprint shall be captured through integrated hardware where available, with a displayed quality score and retry. Where hardware is unavailable a fingerprint image shall be captured using the device camera; no quality score is produced in that case and the capture serves as evidence of presence rather than as a matchable biometric.” (BR-LOS-174, BRD 6.7.3, PDF page 41). See `concept.BR-LOS-174` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-174 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None: the BRD puts this step in the field officer's mobile app (BRD 6.7.1), not in the lending system.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-174 sits in section 6.7.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB whether the standard issued device has a fingerprint reader (BR-LOS-150 leaves the device to the Bank).
2. Ask NRB what quality score the Bank would accept for a hardware capture, since the BRD only says it is displayed.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
