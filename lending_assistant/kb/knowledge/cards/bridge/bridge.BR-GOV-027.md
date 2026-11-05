---
id: bridge.BR-GOV-027
type: bridge
title: "Sign-ins, permission changes and sensitive views are logged with source and outcome"
summary: "Not analysed. The team has not compared BR-GOV-027 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-027]
brd_section: 4.3
doctypes: [Activity Log, Version]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-027"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [concept.BR-GOV-027]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-027 with Frappe Lending, so there is no verdict.

## Business need

“Every authentication attempt, permission change and privileged data access shall be logged with user, timestamp, source address and outcome.” (BR-GOV-027, BRD 4.3, PDF page 23). See `concept.BR-GOV-027` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-027 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Activity Log** is Frappe's record of logins and similar events.
- **Version** is Frappe's record of changes made to a document.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-027 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List what the activity log records for a failed and for a successful sign-in.
2. Open the version record of a permission change and see what it shows.
3. Check whether a source address is stored for each.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
