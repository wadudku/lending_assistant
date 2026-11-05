---
id: bridge.BR-LOS-140
type: bridge
title: A rejection needs a reason code from a list; free text is extra
summary: "Not analysed. The team has not compared BR-LOS-140 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-140]
brd_section: 6.5.1
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-140"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-145"
related: [concept.BR-LOS-140]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-140 with Frappe Lending, so there is no verdict.

## Business need

“Rejection shall require a reason code selected from a configurable list. Free text is additional, never a substitute.” (BR-LOS-140, BRD 6.5.1, PDF page 37). See `concept.BR-LOS-140` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-140 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-140 sits in section 6.5.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the application document above that could hold a reason.
2. Check whether a field can be required for one decision and not another.
3. Ask NRB for the rejection reason code list.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
