---
id: bridge.BR-LOS-111
type: bridge
title: A bad upload file is rejected whole
summary: "Not analysed. The team has not compared BR-LOS-111 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-111]
brd_section: 6.2
doctypes: [Data Import, Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-111"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-110"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
related: [concept.BR-LOS-111]
version: 4
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-111 with Frappe Lending, so there is no verdict.

## Business need

“A structurally invalid file — wrong format, wrong or reordered columns, or row count above the configured or partner-specific ceiling — shall be rejected in its entirety with a clear reason. There shall be no partial ingestion.” (BR-LOS-111, BRD 6.2, PDF page 30). See `concept.BR-LOS-111` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-111 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Data Import** is Frappe's general tool for loading files.
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-111 sits in section 6.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Load a test file with reordered columns, and one with more rows than allowed, through the general import tool named above, and see whether any record is created.
2. Read the import code for a check of column order and a row ceiling that runs before any row is saved.
3. Ask NRB for the partner file template and the row ceilings (BR-LOS-110, BR-LOS-111).

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
