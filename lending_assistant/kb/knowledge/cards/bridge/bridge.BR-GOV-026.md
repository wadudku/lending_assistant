---
id: bridge.BR-GOV-026
type: bridge
title: "Idle accounts switch off, and so do accounts the HR process ends"
summary: "Not analysed. The team has not compared BR-GOV-026 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-026]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-026"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [concept.BR-GOV-026]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-026 with Frappe Lending, so there is no verdict.

## Business need

“User accounts shall be automatically disabled after a configurable period of inactivity, and immediately on instruction from the Bank's HR processes.” (BR-GOV-026, BRD 4.3, PDF page 23). See `concept.BR-GOV-026` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-026 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **User** is Frappe's document for a login account.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-026 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Open the login account document above and find any setting for inactivity.
2. Check what a scheduled job could do about accounts with no recent login.
3. Ask NRB how the HR system will send a leaver's instruction.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
