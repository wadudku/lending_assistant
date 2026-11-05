---
id: bridge.BR-LOS-121
type: bridge
title: Names are tidied before they are compared with the account title
summary: "Not analysed. The team has not compared BR-LOS-121 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-121]
brd_section: 6.3
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-121"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
related: [concept.BR-LOS-121]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-121 with Frappe Lending, so there is no verdict.

## Business need

“Name comparison shall apply normalisation before scoring: case folding, removal of honorifics and titles such as Md., Mohammad, Mst. and Begum, and whitespace collapse. The similarity threshold shall be configurable, defaulting to an exact match after normalisation.” (BR-LOS-121, BRD 6.3, PDF page 32). See `concept.BR-LOS-121` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-121 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-121 sits in section 6.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the name fields on the application document above.
2. Read the code for any comparison of two names.
3. Ask NRB for the full list of titles to remove and the similarity threshold per product.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
