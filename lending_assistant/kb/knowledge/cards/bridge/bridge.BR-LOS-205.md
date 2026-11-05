---
id: bridge.BR-LOS-205
type: bridge
title: The account is checked again just before payment and a bad account stops it
summary: "Not analysed. The team has not compared BR-LOS-205 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-205]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [concept.BR-LOS-205, concept.BR-LOS-203]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-205 with Frappe Lending, so there is no verdict.

## Business need

“Account validation shall be re-executed immediately before disbursement. A dormant, closed or otherwise ineligible account shall halt disbursement and raise an exception.” (BR-LOS-205, BRD 6.9, PDF page 43). See `concept.BR-LOS-205` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-205 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-205 sits in section 6.9. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which account states count as ineligible, since the BRD names dormant and closed and adds "otherwise ineligible".
2. Read BR-LOS-213, which lists stale validations among the items for the exceptions workspace.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
