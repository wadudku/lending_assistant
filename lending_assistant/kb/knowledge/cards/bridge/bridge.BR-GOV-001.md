---
id: bridge.BR-GOV-001
type: bridge
title: The platform never holds money or books entries itself
summary: "Not analysed. The team has not compared BR-GOV-001 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-001]
brd_section: 3.4
doctypes: [Loan Disbursement, Loan Repayment]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_disbursement/loan_disbursement.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-001]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-001 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall never hold a financial balance, post an accounting entry to the Bank's books, or move money on its own authority. Every financial action shall be an instruction issued to CBS and a record of the response received.” (BR-GOV-001, BRD 3.4, PDF page 19). See `concept.BR-GOV-001` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-001 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Disbursement** is the document that records a payout.
- **Loan Repayment** is the document for payments and other postings on a loan, such as waivers; its Repayment Type field lists the kinds.
- The code for Loan Disbursement is in `lending/loan_management/doctype/loan_disbursement/loan_disbursement.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-001 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the documents above that create accounting entries when they are submitted.
2. Read the code for each to see whether it posts entries itself or sends an instruction outward.
3. Ask NRB for the list of CBS instruction types and the record of each reply the bank wants kept (BR-GOV-001, BR-INT-006).

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
