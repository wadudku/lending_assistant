---
id: bridge.BR-LOS-332
type: bridge
title: "No sanction if identity failed, a validation is outstanding or the ceiling would break"
summary: "Not analysed. The team has not compared BR-LOS-332 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-332]
brd_section: 6.6
doctypes: [Loan Application, Loan Partner]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-332"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-103"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
related: [concept.BR-LOS-332]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-332 with Frappe Lending, so there is no verdict.

## Business need

“No sanction shall be issued where identity verification has failed, a mandatory validation is outstanding, or the partner's exposure ceiling would be breached.” (BR-LOS-332, BRD 6.6, PDF page 39). See `concept.BR-LOS-332` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-332 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Loan Partner** is the Frappe Lending document for a co-lending partner.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-332 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the checks the application document above makes before it is saved with a new status.
2. Read the code for a check on the partner's total.
3. Ask NRB which validations are mandatory before sanction.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
