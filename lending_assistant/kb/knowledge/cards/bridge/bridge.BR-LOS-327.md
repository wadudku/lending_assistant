---
id: bridge.BR-LOS-327
type: bridge
title: "Conditions on a sanction are recorded, checked in the field and must be evidenced"
summary: "Not analysed. The team has not compared BR-LOS-327 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-327]
brd_section: 6.6
doctypes: [Loan Application, Loan Application Document]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-327"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-324"
related: [concept.BR-LOS-327]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-327 with Frappe Lending, so there is no verdict.

## Business need

“Where the approver sanctions subject to conditions, those conditions shall be recorded as structured items, presented to the field officer at verification, and evidenced before the application can reach approved status. An unmet condition shall halt the application and refer it back to the approver.” (BR-LOS-327, BRD 6.6, PDF page 38). See `concept.BR-LOS-327` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-327 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Loan Application Document** is a document in the lending app that links a file to an application.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-327 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields and linked records on the documents above that could hold a condition and its proof.
2. Check whether a status can be blocked until a record is attached.
3. Ask NRB for the usual conditions and the evidence each needs.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
