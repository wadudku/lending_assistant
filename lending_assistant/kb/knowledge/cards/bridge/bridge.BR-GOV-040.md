---
id: bridge.BR-GOV-040
type: bridge
title: A changed regulatory rule takes effect from a date and leaves past returns alone
summary: "Not analysed. The team has not compared BR-GOV-040 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-040]
brd_section: 8.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-040"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [concept.BR-GOV-040]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-040 with Frappe Lending, so there is no verdict.

## Business need

“Where a regulatory rule changes, the change shall be implemented as a versioned, effective-dated configuration change. Returns for prior periods shall continue to reflect the rules in force in those periods.” (BR-GOV-040, BRD 8.3, PDF page 58). See `concept.BR-GOV-040` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-040 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-040 sits in section 8.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB who approves a rule change and how soon before its date it is known.
2. List the regulatory settings Frappe Lending holds and note which carry a start date.
3. Test what a re-run of an earlier period uses after one setting has changed.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
