---
id: bridge.BR-LOS-117
type: bridge
title: No application is accepted without recorded borrower consent
summary: "Not analysed. The team has not compared BR-LOS-117 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-117]
brd_section: 6.2.3
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-117"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p31"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
related: [concept.BR-LOS-117]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-117 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall not accept any application without a recorded borrower consent covering, at minimum: the partner's sharing of the individual's personal data with the Bank; the Bank's inquiry to the credit bureau; and identity verification against the national database. The partner shall retain the underlying evidence. The platform shall record the consent reference, the method of capture and the timestamp, and shall make these available to Bank compliance.” (BR-LOS-117, BRD 6.2.3, PDF page 31). See `concept.BR-LOS-117` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-117 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-117 sits in section 6.2.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the application document above that could hold a consent reference, method and time.
2. Check whether an application can be saved with those fields empty.
3. Ask NRB the legal question in the BRD: is a consent reference enough, or must a signed instrument be obtained before the bureau inquiry?

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
