---
id: bridge.BR-LOS-320
type: bridge
title: "The proposed sanction is set from product, grade, headroom and borrower exposure"
summary: "Not analysed. The team has not compared BR-LOS-320 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-320]
brd_section: 6.6
doctypes: [Loan Application, Loan Product, Sanctioned Loan Amount]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-320"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-306"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-331"
related: [concept.BR-LOS-320]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-320 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall determine the proposed sanction — amount, tenor, applicable rate and fees — from the product configuration, the treatment attaching to the application's risk grade under BR-LOS-306, the partner's remaining exposure headroom, and the borrower's aggregate exposure under BR-LOS-331.” (BR-LOS-320, BRD 6.6, PDF page 37). See `concept.BR-LOS-320` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-320 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Loan Product** is the document that holds a loan product's settings.
- **Sanctioned Loan Amount** is a document in the lending app that holds a sanctioned limit.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-320 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the amount, tenor, rate and fee fields on the documents above.
2. Read the application code for any step that sets the amount offered.
3. Ask NRB which of the four inputs are held in which system.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
