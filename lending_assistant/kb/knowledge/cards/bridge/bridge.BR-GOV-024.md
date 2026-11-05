---
id: bridge.BR-GOV-024
type: bridge
title: Every bank and partner account needs a second login factor
summary: "Not analysed. The team has not compared BR-GOV-024 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-024]
brd_section: 4.3
doctypes: [System Settings]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-024"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [concept.BR-GOV-024]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-024 with Frappe Lending, so there is no verdict.

## Business need

“All Bank and partner user accounts shall require multi-factor authentication.” (BR-GOV-024, BRD 4.3, PDF page 23). See `concept.BR-GOV-024` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-024 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **System Settings** is where Frappe keeps site-wide settings, including its two-factor login switch.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-024 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Open the site settings above and find the two-factor switch.
2. Check whether it can be required per role or only for the whole site.
3. Ask NRB which second factors the bank accepts.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
