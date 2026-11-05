---
id: bridge.BR-LMS-011
type: bridge
title: Sending the same handoff twice never creates a second loan
summary: "Not analysed. The team has not compared BR-LMS-011 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-011]
brd_section: 5.4
doctypes: [Loan]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-011"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D1"
related: [concept.BR-LMS-011]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-011 with Frappe Lending, so there is no verdict.

## Business need

“The handoff shall be idempotent. A repeated handoff of the same origination reference shall return the original booked loan and shall never create a second loan record.” (BR-LMS-011, BRD 5.4, PDF page 28). See `concept.BR-LMS-011` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-011 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the document for a loan.
- The code for Loan is in `lending/loan_management/doctype/loan/loan.py`.
- The team's analysis document proposes a unique origination-reference field for the handoff (D1); the row itself was not analysed.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-011 sits in section 5.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the loan document above that could hold an origination reference.
2. Read the code for any check that stops two loans sharing one reference.
3. Test creating two loans with the same reference on a copy of the site and look at the result.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
