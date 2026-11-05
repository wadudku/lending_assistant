---
id: bridge.BR-GOV-031
type: bridge
title: The existing loan book moves in through a controlled opening-balance load
summary: "Not analysed. The team has not compared BR-GOV-031 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-031]
brd_section: 5.4
doctypes: [Data Import, Loan]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-031"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D3"
related: [concept.BR-GOV-031]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-031 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall support the migration of the Bank's existing loan book into servicing through a controlled opening-balance import carrying principal, interest, penalty and charge balances, with source references and control-total reconciliation and formal sign-off before cutover.” (BR-GOV-031, BRD 5.4, PDF page 28). See `concept.BR-GOV-031` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-031 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Data Import** is Frappe's general tool for loading files.
- **Loan** is the document for a loan.
- The team's analysis document proposes a migration batch with control totals and a hold flag (D3); the row itself was not analysed.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-031 sits in section 5.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Load a small test file of loans through the general import tool above on a copy of the site.
2. List what the import cannot set, such as balances of interest, penalty and charges.
3. Ask NRB for the layout of the existing loan book and the control totals it will give.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
