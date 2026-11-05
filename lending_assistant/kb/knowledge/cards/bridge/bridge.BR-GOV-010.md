---
id: bridge.BR-GOV-010
type: bridge
title: Four kinds of date are kept apart and never mixed
summary: "Not analysed. The team has not compared BR-GOV-010 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-010]
brd_section: 3.4
doctypes: [Loan Repayment, Loan Interest Accrual]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment/loan_repayment.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-010]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-010 with Frappe Lending, so there is no verdict.

## Business need

“Effective date, posting date, value date and system timestamp shall be recorded and used as distinct concepts. They shall never be conflated.” (BR-GOV-010, BRD 3.4, PDF page 19). See `concept.BR-GOV-010` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-010 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Repayment** is the document for payments and other postings on a loan, such as waivers; its Repayment Type field lists the kinds.
- **Loan Interest Accrual** is the document that records interest earned for a period.
- The code for Loan Repayment is in `lending/loan_management/doctype/loan_repayment/loan_repayment.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-010 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the date fields on the documents above.
2. Compare them with the four dates in the rule and note any that is not recorded.
3. Find where interest uses a date, and check which of the four it is.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
