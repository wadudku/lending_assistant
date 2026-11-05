---
id: bridge.BR-LOS-152
type: bridge
title: Officers log in with two factors and the session locks when idle
summary: "Not analysed. The team has not compared BR-LOS-152 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-152]
brd_section: 6.7.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-152"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-024"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-050"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [concept.BR-LOS-152, concept.BR-LOS-151, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-152 with Frappe Lending, so there is no verdict.

## Business need

“Login shall require credentials and a second factor. The session shall lock after a configurable idle period and shall require re-authentication.” (BR-LOS-152, BRD 6.7.1, PDF page 39). See `concept.BR-LOS-152` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-152 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-152 sits in section 6.7.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BR-GOV-024 and BR-INT-050, which ask for multi-factor authentication and SMS one-time passcodes, and ask NRB whether the same applies to officers on the device and what idle period it has in mind.
2. Check whether the field officer application signs in through the same login as the Bank's other systems or has its own, using the Bank's security requirements.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
