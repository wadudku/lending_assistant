---
id: bridge.BR-LOS-309
type: bridge
title: "An authorised person can override a score decision, with a second approver and a reason"
summary: "Not analysed. The team has not compared BR-LOS-309 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-309]
brd_section: 6.4
doctypes: [Authorization Rule, Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-309"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
related: [concept.BR-LOS-309]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-309 with Frappe Lending, so there is no verdict.

## Business need

“An authorised user shall be able to override a score-driven decision under maker-checker, within their delegated authority, with a mandatory reason. Overrides shall be recorded against the application, reported as a distinct population, and monitored for volume and subsequent performance.” (BR-LOS-309, BRD 6.4, PDF page 34). See `concept.BR-LOS-309` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-309 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Authorization Rule** is ERPNext's document for approval limits; its list of documents holds sales and purchase documents only, such as Sales Order and Purchase Invoice.
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-309 sits in section 6.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the first item above sets who may approve what.
2. Check whether the application document records a reason for a changed decision.
3. Ask NRB for the authority limits and the override report fields.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
