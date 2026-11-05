---
id: bridge.BR-LMS-002
type: bridge
title: A status change never erases or overwrites earlier records
summary: "Not analysed. The team has not compared BR-LMS-002 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-002]
brd_section: 5.3
doctypes: [Loan Repayment Schedule]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-003"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
related: [concept.BR-LMS-002, brd_section.5.3, lifecycle.RESTRUCTURED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-002 with Frappe Lending, so there is no verdict.

## Business need

“A status transition shall never delete or overwrite a prior classification, schedule version or posting. Superseded records shall be retained and marked as superseded.” (BR-LMS-002, BRD 5.3, PDF page 28). See `concept.BR-LMS-002` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-002 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Repayment Schedule** is the document that holds the instalment plan of a loan.
- The code for Loan Repayment Schedule is in `lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py`.
- The team's analysis document proposes a servicing status field and a status log (D2); the row itself was not analysed.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-002 sits in section 5.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List what happens to the old schedule document when a loan is changed.
2. Read the code for a field that marks a schedule as replaced.
3. Find where an earlier classification is kept after the next one is posted.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
