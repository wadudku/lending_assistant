---
id: bridge.BR-LOS-323
type: bridge
title: The credit approver sees the whole case on one screen
summary: "Not analysed. The team has not compared BR-LOS-323 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-323]
brd_section: 6.6
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-323"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-305"
related: [concept.BR-LOS-323]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-323 with Frappe Lending, so there is no verdict.

## Business need

“The credit approver shall see, on one screen: the submitted KYC; the account validation result; the risk grade, recommended decision and principal adverse reason codes; bureau data in full where the inquiry has been performed at this stage; duplicate and mandatory-sampling flags; the sampling outcome and reviewer's note where the application was sampled; partner context and track record; the borrower's aggregate exposure; and the proposed terms.” (BR-LOS-323, BRD 6.6, PDF page 38). See `concept.BR-LOS-323` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-323 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-323 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the sections and linked records shown on the application document above.
2. Check each item in the BRD list for a field or a link.
3. Ask NRB which screen the credit approver is to work in.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
