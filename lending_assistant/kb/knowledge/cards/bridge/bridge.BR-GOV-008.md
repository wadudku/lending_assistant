---
id: bridge.BR-GOV-008
type: bridge
title: Controlled money changes need two different people
summary: "Not analysed. The team has not compared BR-GOV-008 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-008]
brd_section: 3.4
doctypes: [Loan Restructure, Loan Write Off]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_write_off/loan_write_off.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-008]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-008 with Frappe Lending, so there is no verdict.

## Business need

“Every controlled financial change — repricing, restructuring, settlement, waiver, write-off, bulk operation and corrective posting — shall require maker-checker approval by two different users.” (BR-GOV-008, BRD 3.4, PDF page 19). See `concept.BR-GOV-008` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-008 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Restructure** is the document used to change a loan's terms.
- **Loan Write Off** is the document used to write a loan off.
- The code for Loan Write Off is in `lending/loan_management/doctype/loan_write_off/loan_write_off.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-008 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the documents above and the other documents that change a loan's money figures.
2. Read each for a check that the person who saves a document is not the person who submits it.
3. Find out whether Frappe's approval workflow can be switched on for each of them.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
