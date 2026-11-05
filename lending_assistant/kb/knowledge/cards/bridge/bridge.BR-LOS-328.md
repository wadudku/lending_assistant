---
id: bridge.BR-LOS-328
type: bridge
title: Every sanction is recorded as a system or user decision with the rules relied on
summary: "Not analysed. The team has not compared BR-LOS-328 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-328]
brd_section: 6.6
doctypes: [Loan Application, Version]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-328"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-321"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-304"
related: [concept.BR-LOS-328]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-328 with Frappe Lending, so there is no verdict.

## Business need

“Every sanction shall record: whether it was a system decision or a user decision; the threshold rule and version relied on, or the approver identity and the delegated limit relied on; the scorecard version and grade; the configuration version in force; the proposed and final terms; the reason codes; and the timestamp. A system sanction shall be recorded as a system decision naming the threshold applied, never against a user.” (BR-LOS-328, BRD 6.6, PDF page 38). See `concept.BR-LOS-328` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-328 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Version** is Frappe's record of changes made to a document.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-328 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the document above that record who made a decision.
2. Compare them with the seven things the BRD says each sanction records.
3. Ask NRB for the wording of a system decision entry.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
