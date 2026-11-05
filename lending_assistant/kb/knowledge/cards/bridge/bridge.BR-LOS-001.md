---
id: bridge.BR-LOS-001
type: bridge
title: Only allowed status changes go through; others are refused and logged
summary: "Not analysed. The team has not compared BR-LOS-001 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-001]
brd_section: 5.2
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-004"
related: [concept.BR-LOS-001]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-001 with Frappe Lending, so there is no verdict.

## Business need

“Status transitions shall be validated against the model above. An attempted transition not permitted by the model shall be rejected, logged as an exception, and shall not alter the application.” (BR-LOS-001, BRD 5.2, PDF page 27). See `concept.BR-LOS-001` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LOS-001 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-001 sits in section 5.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the status values on the application document above.
2. Read the code for a check of which status may follow which.
3. Test an attempt to set a status out of order on a copy of the site and see whether anything is logged.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
