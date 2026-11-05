---
id: bridge.BR-LMS-010
type: bridge
title: "Servicing accepts only a complete, confirmed handoff; others go to an exception queue"
summary: "Not analysed. The team has not compared BR-LMS-010 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-010]
brd_section: 5.4
doctypes: [Loan, Loan Disbursement]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-011"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D1"
related: [concept.BR-LMS-010]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-010 with Frappe Lending, so there is no verdict.

## Business need

“The LMS shall accept a loan into servicing only where the handoff package is complete and carries a confirmed disbursement reference. An incomplete or unconfirmed handoff shall be rejected into an exception queue with a stated reason and shall not create a loan.” (BR-LMS-010, BRD 5.4, PDF page 28). See `concept.BR-LMS-010` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-010 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the document for a loan.
- **Loan Disbursement** is the document that records a payout.
- The code for Loan is in `lending/loan_management/doctype/loan/loan.py`.
- The team's analysis document proposes a checked intake interface for the funded-loan handoff (D1); the row itself was not analysed.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-010 sits in section 5.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List what must be present before a loan can be created on the documents above.
2. Read the code for a step that rejects a record and says why.
3. Ask NRB where rejected handoffs should be listed and who clears them.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
