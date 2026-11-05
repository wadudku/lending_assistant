---
id: bridge.BR-INT-067
type: bridge
title: "An operations view of automation work, with controlled retry, cancel and escalate"
summary: "Not analysed. The team has not compared BR-INT-067 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-067]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-067"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [concept.BR-INT-067]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-067 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall present an automation operations view showing pending, in progress, completed and failed transactions, with the ability to retry, cancel or escalate an individual item under maker-checker.” (BR-INT-067, BRD 9.3, PDF page 63). See `concept.BR-INT-067` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-067 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-067 sits in section 9.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which roles may propose and approve a retry.
2. List the statuses a queued job can hold in Frappe Lending.
3. Compare them with pending, in progress, completed and failed.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
