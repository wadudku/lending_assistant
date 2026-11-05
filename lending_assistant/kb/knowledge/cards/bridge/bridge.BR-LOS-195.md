---
id: bridge.BR-LOS-195
type: bridge
title: "If the bureau cannot be reached the application waits, and a timeout never counts as a pass"
summary: "Not analysed. The team has not compared BR-LOS-195 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-195]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-195"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [concept.BR-LOS-195, concept.BR-LOS-190, brd_section.6.7.2, glossary.cib]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-195 with Frappe Lending, so there is no verdict.

## Business need

“Where the bureau or the designated host is unavailable, the application shall hold rather than fail, with automatic retry and clear officer messaging. A timeout or transport error shall never be interpreted as a pass.” (BR-LOS-195, BRD 6.8, PDF page 42). See `concept.BR-LOS-195` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-195 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-195 sits in section 6.8. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB how many retries and how long a wait it wants, since the BRD says only "automatic retry".
2. Read BRD 6.7.2, which says credit bureau verification holds at verification in progress when the officer is offline.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
