---
id: bridge.BR-LOS-116
type: bridge
title: "Duplicates are caught at three levels, each with its own treatment"
summary: "Not analysed. The team has not compared BR-LOS-116 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-116]
brd_section: 6.2
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-116"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-113"
related: [concept.BR-LOS-116]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-116 with Frappe Lending, so there is no verdict.

## Business need

“Duplicate detection shall operate at three scopes, each with its own treatment as set out below.” (BR-LOS-116, BRD 6.2, PDF page 30). See `concept.BR-LOS-116` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-116 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-116 sits in section 6.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the application document above that could identify the same person.
2. Read the application code for a check on a repeated identifier.
3. Ask NRB for the exact fields compared at each of the three scopes and the neutral message wording.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
