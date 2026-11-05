---
id: bridge.BR-LOS-305
type: bridge
title: Refer and decline outcomes carry reason codes
summary: "Not analysed. The team has not compared BR-LOS-305 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-305]
brd_section: 6.4
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-305"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-308"
related: [concept.BR-LOS-305]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-305 with Frappe Lending, so there is no verdict.

## Business need

“Every refer and every decline shall record the principal adverse factors that drove the outcome, as reason codes drawn from a configurable list, so that the Bank can explain the decision internally and to the applicant where policy or law requires it.” (BR-LOS-305, BRD 6.4, PDF page 34). See `concept.BR-LOS-305` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-305 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-305 sits in section 6.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the application document above that could hold a reason.
2. Check whether a reason can be picked from a list that the Bank edits.
3. Ask NRB for the reason code list and who owns it.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
