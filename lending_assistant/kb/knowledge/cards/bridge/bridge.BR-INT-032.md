---
id: bridge.BR-INT-032
type: bridge
title: Bureau credentials are kept separate from the rest of the system
summary: "Not analysed. The team has not compared BR-INT-032 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-032]
brd_section: 9.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-032"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [concept.BR-INT-032]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-032 with Frappe Lending, so there is no verdict.

## Business need

“Bureau credentials and session handling shall be isolated from the main application and from the Core Banking System automation, and accessible only to the component that needs them.” (BR-INT-032, BRD 9.5, PDF page 64). See `concept.BR-INT-032` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-032 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-032 sits in section 9.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB where the bureau credentials are held.
2. List the components that would run with bureau access.
3. Check which of them can read the credentials.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
