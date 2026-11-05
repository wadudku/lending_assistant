---
id: bridge.BR-LOS-324
type: bridge
title: "The approver has five ways to decide, and declines and revisions need reason codes"
summary: "Not analysed. The team has not compared BR-LOS-324 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-324]
brd_section: 6.6
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-324"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-305"
related: [concept.BR-LOS-324]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-324 with Frappe Lending, so there is no verdict.

## Business need

“The credit approver shall be able to sanction as proposed, sanction at revised terms, sanction subject to conditions, defer to a higher authority with a note, or decline. A decline and a revision shall each require a reason code from a configurable list; free text is additional, never a substitute.” (BR-LOS-324, BRD 6.6, PDF page 38). See `concept.BR-LOS-324` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-324 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-324 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the status values of the application document above and mark which of the five decisions each could stand for.
2. Check whether a reason can be required for one decision and not another.
3. Ask NRB for the reason code lists for decline and for revision.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
