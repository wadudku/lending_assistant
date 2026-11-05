---
id: bridge.BR-LOS-300
type: bridge
title: Every submitted application is scored before it moves on
summary: "Not analysed. The team has not compared BR-LOS-300 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-300]
brd_section: 6.4
doctypes: [Loan Application, Loan Product]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-300"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p33"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
related: [concept.BR-LOS-300]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-300 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall score every submitted application against the scorecard configured for its product, and shall not advance an unscored application to sampling or to sanction.” (BR-LOS-300, BRD 6.4, PDF page 33). See `concept.BR-LOS-300` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-300 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Loan Product** is the document that holds a loan product's settings.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-300 sits in section 6.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the application document above that could hold a score.
2. Read the application code for any step that must finish before the next one starts.
3. Ask NRB for the scorecard owner, the product list and the date the scorecards will be supplied.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
