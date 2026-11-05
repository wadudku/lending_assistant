---
id: bridge.BR-LOS-308
type: bridge
title: A score-declined application gets its own final status and is not shown the score
summary: "Not analysed. The team has not compared BR-LOS-308 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-308]
brd_section: 6.4
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-308"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-305"
related: [concept.BR-LOS-308]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-308 with Frappe Lending, so there is no verdict.

## Business need

“An application declined by score shall take a distinct terminal status with its reason codes, shall not be assigned to a field officer, and shall be reported to the partner as declined without disclosure of the score, the grade or the scorecard logic.” (BR-LOS-308, BRD 6.4, PDF page 34). See `concept.BR-LOS-308` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-308 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-308 sits in section 6.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the status values of the application document above.
2. Check which user roles can see which fields.
3. Ask NRB for the status name and the exact message shown to the partner.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
