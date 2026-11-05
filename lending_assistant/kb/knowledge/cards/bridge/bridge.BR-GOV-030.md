---
id: bridge.BR-GOV-030
type: bridge
title: A daily check compares payouts in origination with loans in servicing
summary: "Not analysed. The team has not compared BR-GOV-030 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-030]
brd_section: 5.4
doctypes: [Loan Disbursement, Loan]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/hooks.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-030"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-004"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D1"
related: [concept.BR-GOV-030]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-030 with Frappe Lending, so there is no verdict.

## Business need

“A daily control shall compare confirmed disbursements recorded in origination against loans booked in servicing, and shall raise every difference in either direction as an exception requiring documented closure.” (BR-GOV-030, BRD 5.4, PDF page 28). See `concept.BR-GOV-030` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-030 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Disbursement** is the document that records a payout.
- **Loan** is the document for a loan.
- The scheduled jobs that run daily are listed in `lending/hooks.py`.
- The team's analysis document proposes the daily check together with the funded-loan handoff (D1); the row itself was not analysed.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-030 sits in section 5.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the daily scheduled jobs in `lending/hooks.py`.
2. Check whether any of them compares records from two systems.
3. Ask NRB how the platform will read confirmed payouts from origination and who closes the exceptions.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
