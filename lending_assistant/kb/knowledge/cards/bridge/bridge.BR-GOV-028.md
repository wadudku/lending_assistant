---
id: bridge.BR-GOV-028
type: bridge
title: "Approval limits by role and amount, and a case over the limit escalates"
summary: "Not analysed. The team has not compared BR-GOV-028 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-028]
brd_section: 4.3
doctypes: [Authorization Rule, Workflow]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [concept.BR-GOV-028]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-028 with Frappe Lending, so there is no verdict.

## Business need

“Delegated authority limits — for score override, sampling override, sanction and sanction variation, waiver, settlement, write-off and rate change — shall be configurable by role and by amount band, and shall be enforced by the platform at the point of action. A case above the acting user's limit shall escalate, and shall not be actionable by that user.” (BR-GOV-028, BRD 4.3, PDF page 23). See `concept.BR-GOV-028` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-028 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Authorization Rule** is ERPNext's document for approval limits; its list of documents holds sales and purchase documents only, such as Sales Order and Purchase Invoice.
- **Workflow** is Frappe's tool for approval steps on a document.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-028 sits in section 4.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the actions named in the rule that are documents in the lending app.
2. Open the rule document above and see which amount fields and roles it can use.
3. Ask NRB for the roles and amount bands for each action.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
