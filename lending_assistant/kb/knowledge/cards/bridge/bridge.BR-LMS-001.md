---
id: bridge.BR-LMS-001
type: bridge
title: "A loan has exactly one current status, with its full history"
summary: "Not analysed. The team has not compared BR-LMS-001 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-001]
brd_section: 5.3
doctypes: [Loan]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.json]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
related: [concept.BR-LMS-001, brd_section.5.3, lifecycle.ACTIVE, lifecycle.OVERDUE, lifecycle.NPA]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-001 with Frappe Lending, so there is no verdict.

## Business need

“The LMS shall maintain exactly one current servicing status for every loan, and shall retain the full history of prior statuses with the date and reason for each transition.” (BR-LMS-001, BRD 5.3, PDF page 27). See `concept.BR-LMS-001` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-001 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the document for a loan, and it holds the loan's status.
- The status options of Loan are in `lending/loan_management/doctype/loan/loan.json`.
- The team's analysis document proposes a servicing status field and a status log (D2); the row itself was not analysed.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-001 sits in section 5.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the loan document above that carry a status or a flag.
2. Compare them with the twelve states in BRD 5.3.
3. Find out whether the history of earlier statuses with date and reason is kept anywhere.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
