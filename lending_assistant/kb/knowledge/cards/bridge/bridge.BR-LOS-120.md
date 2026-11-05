---
id: bridge.BR-LOS-120
type: bridge
title: No application is submitted without a successful bank account check
summary: "Not analysed. The team has not compared BR-LOS-120 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-120]
brd_section: 6.3
doctypes: [Loan Application, Bank Account]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
related: [concept.BR-LOS-120]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-120 with Frappe Lending, so there is no verdict.

## Business need

“No application shall reach submitted status without a successful account validation against CBS covering: the account exists; the account status is active, excluding dormant, closed, frozen, blocked and lien-marked; the account type appears in the product's permitted list; the account title matches the applicant name at or above the configured similarity threshold; and the CIF-level KYC status is current.” (BR-LOS-120, BRD 6.3, PDF page 32). See `concept.BR-LOS-120` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-120 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Bank Account** is ERPNext's document for a bank account.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-120 sits in section 6.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the application document above that hold an account number and an account title.
2. Read the code for any call to a system outside the platform before submission.
3. Ask NRB what the CBS enquiry screens return for each of the five checks (see BRD 9.2).

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
