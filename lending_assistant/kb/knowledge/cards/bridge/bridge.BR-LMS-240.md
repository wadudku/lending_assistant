---
id: bridge.BR-LMS-240
type: bridge
title: A servicing dashboard shows the state of the loan book
summary: "Not analysed. The team has not compared BR-LMS-240 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-240]
brd_section: 8.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/loan_management_dashboard/loan_dashboard/loan_dashboard.json]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-240"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [concept.BR-LMS-240]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-240 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall present a servicing dashboard showing book size and composition, collection performance against demand, DPD distribution, classification movement, provision position and exception queue volumes.” (BR-LMS-240, BRD 8.2, PDF page 58). See `concept.BR-LMS-240` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-240 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-240 carries the LMS prefix but sits in BRD section 8.2, outside the 103 requirements of section 7, so it was not analysed.
- The definition of the loan dashboard in the lending app is in `lending/loan_management/loan_management_dashboard/loan_dashboard/loan_dashboard.json`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-240 sits in section 8.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Open the loan dashboard in Frappe Lending and list what it shows.
2. Compare that list with the six items in the BRD sentence.
3. Ask NRB what period and what level of detail each of the six items should show.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
