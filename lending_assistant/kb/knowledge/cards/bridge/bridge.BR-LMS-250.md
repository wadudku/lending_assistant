---
id: bridge.BR-LMS-250
type: bridge
title: A monthly extract for the Credit Information Bureau
summary: "Not analysed. The team has not compared BR-LMS-250 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-250]
brd_section: 8.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-250"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [concept.BR-LMS-250]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-250 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall support the monthly CIB contribution extract, carrying every field Bangladesh Bank requires for each reportable loan. The required format is to be supplied by the Bank.” (BR-LMS-250, BRD 8.3, PDF page 58). See `concept.BR-LMS-250` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-250 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-250 carries the LMS prefix but sits in BRD section 8.3, outside the 103 requirements of section 7, so it was not analysed.
- The team's verification notes list a Credit Bureau Report document type as present in the develop version of Frappe Lending and not in 16.5.1. The team did not compare it with BR-LMS-250.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-250 sits in section 8.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the CIB contribution layout and the date each month the file is due.
2. List the fields that layout needs for each loan.
3. Compare that list with the fields Frappe Lending holds for a loan and its borrower.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
