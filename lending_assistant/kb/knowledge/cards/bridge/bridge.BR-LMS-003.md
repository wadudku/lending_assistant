---
id: bridge.BR-LMS-003
type: bridge
title: Status names follow the bank's own words and Bangladesh Bank's
summary: "Not analysed. The team has not compared BR-LMS-003 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-003]
brd_section: 5.3
doctypes: [Loan]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.json]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-002"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
related: [concept.BR-LMS-003, brd_section.5.3, lifecycle.OVERDUE]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-003 with Frappe Lending, so there is no verdict.

## Business need

“Terminology for servicing statuses shall be aligned with the Bank's existing vocabulary and with Bangladesh Bank classification nomenclature before the configuration is baselined.” (BR-LMS-003, BRD 5.3, PDF page 28). See `concept.BR-LMS-003` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-003 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the document for a loan, and it holds the loan's status.
- The status options of Loan are in `lending/loan_management/doctype/loan/loan.json`.
- The team's analysis document proposes showing NRB terms through the servicing status field (D2); the row itself was not analysed.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-003 sits in section 5.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the status words shown on the loan document.
2. Compare them with the twelve names in BRD 5.3.
3. Ask NRB for its own list of status terms and the Bangladesh Bank terms.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
