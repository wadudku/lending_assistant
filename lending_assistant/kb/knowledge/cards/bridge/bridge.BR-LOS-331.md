---
id: bridge.BR-LOS-331
type: bridge
title: The borrower's total exposure is added up before sanction and held to a limit
summary: "Not analysed. The team has not compared BR-LOS-331 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-331]
brd_section: 6.6
doctypes: [Loan, Loan Application, Customer]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-331"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-320"
related: [concept.BR-LOS-331]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-331 with Frappe Lending, so there is no verdict.

## Business need

“Before sanction the platform shall aggregate the borrower's exposure across every application and loan held on the platform, and across the Bank where that position can be retrieved, and shall apply the configured single-borrower exposure limit.” (BR-LOS-331, BRD 6.6, PDF page 38). See `concept.BR-LOS-331` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-331 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the document for a loan.
- **Loan Application** is the document Frappe Lending uses for applications.
- **Customer** is ERPNext's document for a customer.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-331 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the documents above are linked to one borrower.
2. Read the application code for any total of loans per borrower.
3. Ask NRB where the position across the Bank can be retrieved and the limit amount.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
