---
id: bridge.BR-GOV-022
type: bridge
title: "Nobody approves their own work, and the system enforces it"
summary: "Not analysed. The team has not compared BR-GOV-022 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-022]
brd_section: 4.3
doctypes: [Workflow, Loan Write Off]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_write_off/loan_write_off.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-022"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-022]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-022 with Frappe Lending, so there is no verdict.

## Business need

“A user shall not be able to approve their own maker action. The platform shall enforce this at the point of approval, not only in the user interface.” (BR-GOV-022, BRD 4.3, PDF page 23). See `concept.BR-GOV-022` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-022 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Workflow** is Frappe's tool for approval steps on a document.
- **Loan Write Off** is the document used to write a loan off.
- The code for Loan Write Off is in `lending/loan_management/doctype/loan_write_off/loan_write_off.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-022 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the documents that need a second person's approval (see BR-GOV-008).
2. Test as one limited user on a copy of the site: prepare a document, then submit it as the same user, through the screen and through a direct call.
3. Read the server code for a check on who saved and who submitted.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
