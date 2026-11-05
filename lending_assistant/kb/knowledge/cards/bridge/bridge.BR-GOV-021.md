---
id: bridge.BR-GOV-021
type: bridge
title: A partner's users see only their own partner's data
summary: "Not analysed. The team has not compared BR-GOV-021 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-021]
brd_section: 4.3
doctypes: [Loan Partner, User Permission]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_partner/loan_partner.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-021"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [concept.BR-GOV-021]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-021 with Frappe Lending, so there is no verdict.

## Business need

“Partner users shall be scoped to their own partner organisation. No partner user shall be able to view, infer or export data belonging to another partner under any circumstance, including through search, reporting, export or error messages.” (BR-GOV-021, BRD 4.3, PDF page 23). See `concept.BR-GOV-021` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-021 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Partner** is the document that holds a co-lending partner.
- **User Permission** is Frappe's way to limit a user to certain records.
- The code for Loan Partner is in `lending/loan_management/doctype/loan_partner/loan_partner.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-021 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the places partner data can appear: lists, search, reports, exports and error messages.
2. Test one limited user on a copy of the site in each of those places.
3. Ask NRB to confirm whether partners that send applications and partners that co-lend are the same kind of partner for this rule.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
