---
id: bridge.BR-LOS-330
type: bridge
title: A sanction lapses after a set validity period
summary: "Not analysed. The team has not compared BR-LOS-330 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-330]
brd_section: 6.6
doctypes: [Loan Application, Sanctioned Loan Amount]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-330"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-123"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-124"
related: [concept.BR-LOS-330]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-330 with Frappe Lending, so there is no verdict.

## Business need

“A sanction shall lapse after a configurable validity period. A lapsed sanction shall block assignment and disbursement and shall require re-sanction, with the score and account validation refreshed where they have themselves expired.” (BR-LOS-330, BRD 6.6, PDF page 38). See `concept.BR-LOS-330` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-330 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Sanctioned Loan Amount** is a document in the lending app that holds a sanctioned limit.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-330 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the date fields on the documents above.
2. Read the application code for any rule that depends on how old a record is.
3. Ask NRB for the sanction validity period by product.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
