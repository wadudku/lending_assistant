---
id: bridge.BR-LOS-103
type: bridge
title: A submission that would break the partner's exposure ceiling is stopped
summary: "Not analysed. The team has not compared BR-LOS-103 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-103]
brd_section: 6.1
doctypes: [Loan Partner, Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-103"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-115"
related: [concept.BR-LOS-103]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-103 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall track partner aggregate exposure against the agreed ceiling and shall prevent a submission that would breach it, with a clear message stating the remaining headroom.” (BR-LOS-103, BRD 6.1, PDF page 29). See `concept.BR-LOS-103` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-103 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Partner** is the Frappe Lending document for a co-lending partner.
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-103 sits in section 6.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the partner document above that hold an amount.
2. Read the application code for a check made at submission against a total.
3. Ask NRB how exposure is counted: sanctioned, disbursed, or still outstanding.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
