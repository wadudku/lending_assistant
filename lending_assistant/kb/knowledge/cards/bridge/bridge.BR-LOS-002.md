---
id: bridge.BR-LOS-002
type: bridge
title: "When less is sanctioned than asked, both amounts are kept and shown"
summary: "Not analysed. The team has not compared BR-LOS-002 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-002]
brd_section: 5.2
doctypes: [Loan Application, Sanctioned Loan Amount]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-002a"
related: [concept.BR-LOS-002]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-002 with Frappe Lending, so there is no verdict.

## Business need

“Where the sanctioned amount is below the amount requested, both figures shall be retained, a limit-revised indicator shall be carried, and both figures shall be visible to Bank staff, the partner and the field officer.” (BR-LOS-002, BRD 5.2, PDF page 27). See `concept.BR-LOS-002` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LOS-002 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Sanctioned Loan Amount** is a document in the lending app that holds a sanctioned limit.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-002 sits in section 5.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the amount fields on the application document above.
2. Check whether the requested amount stays on the record after a lower amount is entered.
3. Ask NRB which of the three groups may see which figure, and in which screens.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
