---
id: bridge.BR-LOS-130
type: bridge
title: "After scoring, a share of applications is picked for manual review"
summary: "Not analysed. The team has not compared BR-LOS-130 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-130]
brd_section: 6.5
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-130"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p35"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-307"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-137"
related: [concept.BR-LOS-130]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-130 with Frappe Lending, so there is no verdict.

## Business need

“Once applications have been scored, the platform shall select a subset for manual review at a rate determined by configuration, together with every application the scorecard referred and every application caught by a mandatory sampling rule, and shall pass the remainder automatically.” (BR-LOS-130, BRD 6.5, PDF page 35). See `concept.BR-LOS-130` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-130 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-130 sits in section 6.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the statuses on the application document above that come after scoring.
2. Read the application code for any step that picks some records and passes the others.
3. Ask NRB for the global sampling rate and who may change it.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
