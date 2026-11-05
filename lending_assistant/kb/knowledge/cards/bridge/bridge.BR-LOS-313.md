---
id: bridge.BR-LOS-313
type: bridge
title: Any past decision can be reproduced as it was at the time
summary: "Not analysed. The team has not compared BR-LOS-313 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-313]
brd_section: 6.4
doctypes: [Version, Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-313"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p35"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-304"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-302"
related: [concept.BR-LOS-313]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-313 with Frappe Lending, so there is no verdict.

## Business need

“The Bank shall be able to reproduce, for any past application, the score, the attribute values, the grade, the cut-offs and the scorecard version in force at its own decision time, irrespective of later scorecard changes.” (BR-LOS-313, BRD 6.4, PDF page 35). See `concept.BR-LOS-313` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-313 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's record of changes made to a document.
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-313 sits in section 6.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the first item above lets a past state of a document be viewed.
2. Check whether scorecard settings are kept as dated versions.
3. Ask NRB how long past scores must be kept.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
