---
id: bridge.BR-GOV-020
type: bridge
title: "Access follows roles, and a person can hold several"
summary: "Not analysed. The team has not compared BR-GOV-020 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-020]
brd_section: 4.3
doctypes: [Role, Custom DocPerm]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.json]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-020"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p22"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p22"
related: [concept.BR-GOV-020]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-020 with Frappe Lending, so there is no verdict.

## Business need

“Access shall be role-based. A user may hold more than one role. Permissions shall be assignable at function level, not only at role level.” (BR-GOV-020, BRD 4.3, PDF page 22). See `concept.BR-GOV-020` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-020 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Role** is Frappe's list of roles that permissions are given to.
- **Custom DocPerm** is Frappe's document for custom permission rules.
- The permission rules set for Loan are in `lending/loan_management/doctype/loan/loan.json`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-020 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the roles the lending app creates and what each may do on the loan document.
2. Open the permission rules for one document and see whether a single action can be set apart from the role.
3. Ask NRB for its list of functions that need their own permission.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
