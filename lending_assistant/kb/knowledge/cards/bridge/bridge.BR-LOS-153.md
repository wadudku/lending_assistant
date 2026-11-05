---
id: bridge.BR-LOS-153
type: bridge
title: The app comes in Bangla and English
summary: "Not analysed. The team has not compared BR-LOS-153 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-153]
brd_section: 6.7.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-153"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.1"
related: [concept.BR-LOS-153, concept.BR-LOS-152, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-153 with Frappe Lending, so there is no verdict.

## Business need

“The interface shall support Bangla and English, switchable by the user without losing in-progress work.” (BR-LOS-153, BRD 6.7.1, PDF page 40). See `concept.BR-LOS-153` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-153 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None: the BRD puts this step in the field officer's mobile app (BRD 6.7.1), not in the lending system.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-153 sits in section 6.7.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB whether the Bangla wording of screens and messages will be written by the Bank or by the supplier.
2. Ask the team that plans the field officer application how a language switch is meant to keep entered data, since the BRD requires that.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
