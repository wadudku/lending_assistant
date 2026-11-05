---
id: bridge.BR-GOV-025
type: bridge
title: Sensitive personal data is permissioned apart and every look is logged
summary: "Not analysed. The team has not compared BR-GOV-025 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-025]
brd_section: 4.3
doctypes: [Access Log, Custom DocPerm]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-025"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [concept.BR-GOV-025]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-025 with Frappe Lending, so there is no verdict.

## Business need

“Access to credit bureau data, identity images, biometric captures and full borrower financial position shall be separately permissioned from ordinary operational access, and every access shall be logged with user, record and timestamp.” (BR-GOV-025, BRD 4.3, PDF page 23). See `concept.BR-GOV-025` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-025 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Access Log** is Frappe's document for logged exports, downloads and print views.
- **Custom DocPerm** is Frappe's document for custom permission rules.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-025 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List where the lending app stores each of the four kinds of data in the rule.
2. Open the permission rules for each and see whether a field can be restricted apart from the rest of the document.
3. Check what the access log records when a document is opened.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
