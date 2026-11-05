---
id: bridge.BR-INT-061
type: bridge
title: The automation signs in with its own dedicated accounts
summary: "Not analysed. The team has not compared BR-INT-061 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-061]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-061"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-INT-061]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-061 with Frappe Lending, so there is no verdict.

## Business need

“The automation shall sign in using dedicated service accounts, provisioned by the Bank, holding the least privilege necessary for the transactions in scope. Those accounts shall not be shared with or used by any human user.” (BR-INT-061, BRD 9.3, PDF page 62). See `concept.BR-INT-061` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-061 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-061 sits in section 9.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which transactions the service account must be allowed to do.
2. Ask NRB who creates and reviews the account.
3. List the rights each transaction in the BRD needs.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
