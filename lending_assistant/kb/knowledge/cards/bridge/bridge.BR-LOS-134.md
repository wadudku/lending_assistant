---
id: bridge.BR-LOS-134
type: bridge
title: Applications not picked advance as a system decision stating the rate
summary: "Not analysed. The team has not compared BR-LOS-134 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-134]
brd_section: 6.5
doctypes: [Loan Application, Version]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-134"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-130"
related: [concept.BR-LOS-134]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-134 with Frappe Lending, so there is no verdict.

## Business need

“Applications not selected shall advance automatically and shall be recorded in the audit trail as a system decision stating the rate applied, not as a user decision.” (BR-LOS-134, BRD 6.5, PDF page 36). See `concept.BR-LOS-134` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-134 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Version** is Frappe's record of changes made to a document.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-134 sits in section 6.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the audit history of the documents above names who or what made a change.
2. Check whether a change made by the system is shown differently from one made by a person.
3. Ask NRB for the wording of the system decision entry.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
