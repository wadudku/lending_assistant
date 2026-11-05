---
id: bridge.BR-LOS-301
type: bridge
title: The scorecard can use seven kinds of input
summary: "Not analysed. The team has not compared BR-LOS-301 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-301]
brd_section: 6.4
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-301"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p33"
related: [concept.BR-LOS-301]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-301 with Frappe Lending, so there is no verdict.

## Business need

“The scorecard shall be able to draw on, at minimum: application data including demographics, declared income, loan purpose, requested amount and tenor; derived measures such as instalment-to-income and loan-to-income; geography at district and upazila level; account behaviour where available from the Core Banking System; the partner's own track record; credit bureau data where the inquiry has been performed at this stage; and duplicate, negative-list and mandatory-sampling flags.” (BR-LOS-301, BRD 6.4, PDF page 33). See `concept.BR-LOS-301` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-301 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-301 sits in section 6.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the application document above and mark which of the seven kinds each belongs to.
2. Check which of the kinds have no field.
3. Ask NRB which inputs are known at scoring time and which arrive later.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
