---
id: bridge.BR-LOS-194
type: bridge
title: "Pass or fail rules are owned by Credit Risk, versioned and checked by a second person"
summary: "Not analysed. The team has not compared BR-LOS-194 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-194]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-194"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [concept.BR-LOS-194, glossary.maker-checker, concept.BR-LOS-190]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-194 with Frappe Lending, so there is no verdict.

## Business need

“Decision rules determining pass or fail shall be configuration owned by Credit Risk, versioned, and subject to maker-checker. The rule version applied shall be recorded against every decision, so that two applications decided under different rule versions each show the version in force at their own decision time.” (BR-LOS-194, BRD 6.8, PDF page 42). See `concept.BR-LOS-194` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-194 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's document for the history of changes to other documents.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-194 sits in section 6.8. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB whether Credit Risk or another team will enter the decision rules and approve them.
2. Read BR-LOS-232 and BR-LOS-233, which ask for versioned configuration in general.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
