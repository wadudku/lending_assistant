---
id: bridge.BR-GOV-011
type: bridge
title: "Any past date can be reproduced: status, configuration and rules then in force"
summary: "Not analysed. The team has not compared BR-GOV-011 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-011]
brd_section: 3.4
doctypes: [Loan, Loan Repayment Schedule]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-011"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p20"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p20"
related: [concept.BR-GOV-011]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-011 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall be able to reproduce, for any application or loan at any past date, the status it held on that date and the configuration and rule versions then in force.” (BR-GOV-011, BRD 3.4, PDF page 20). See `concept.BR-GOV-011` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-011 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the document for a loan, and it holds the loan's status.
- **Loan Repayment Schedule** is the document that holds the instalment plan of a loan.
- The code for Loan Repayment Schedule is in `lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-011 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List which of status, product settings and classification rules keep a dated history.
2. Read how the schedule document is versioned when a loan changes.
3. Ask NRB which past dates must be reproducible and for how long.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
