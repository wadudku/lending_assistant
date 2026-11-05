---
id: bridge.BR-LOS-211
type: bridge
title: Bank staff can search every application by seven identifiers
summary: "Not analysed. The team has not compared BR-LOS-211 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-211]
brd_section: 6.10.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-211"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.1"
related: [concept.BR-LOS-211, concept.BR-LOS-220, glossary.nid]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-211 with Frappe Lending, so there is no verdict.

## Business need

“Bank staff shall be able to search across all applications by NID, mobile number, account number, applicant name, partner, batch reference and loan account number.” (BR-LOS-211, BRD 6.10.1, PDF page 44). See `concept.BR-LOS-211` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-211 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-211 sits in section 6.10.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB whether a search should find a name or number from only part of it, since the BRD lists the keys without saying how they are searched.
2. Compare the search keys with the filters in BR-LOS-220.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
