---
id: bridge.BR-LOS-160
type: bridge
title: Officers can capture data offline and send it later
summary: "Not analysed. The team has not compared BR-LOS-160 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-160]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-160"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
related: [concept.BR-LOS-160, concept.BR-LOS-155, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-160 with Frappe Lending, so there is no verdict.

## Business need

“The application shall pre-download the officer's assigned applications, including retrieved KYC and the retained identity portrait, whenever connectivity is available. The officer shall be able to complete data capture — additional fields, signature, fingerprint and liveness — while offline, with captures queued locally for synchronisation.” (BR-LOS-160, BRD 6.7.2, PDF page 40). See `concept.BR-LOS-160` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-160 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None: the BRD puts this step in the field officer's mobile app (BRD 6.7.1), not in the lending system.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-160 sits in section 6.7.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how many assigned applications an officer should be able to hold on the device at one time.
2. Ask the team that plans the field officer application how the pre-download and the later upload of captures will be built and tested without a connection.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
