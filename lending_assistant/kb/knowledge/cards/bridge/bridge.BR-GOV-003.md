---
id: bridge.BR-GOV-003
type: bridge
title: "After a failed call, ask the other system before retrying"
summary: "Not analysed. The team has not compared BR-GOV-003 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-003]
brd_section: 3.4
doctypes: [Loan Disbursement, Error Log]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_disbursement/loan_disbursement.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-GOV-003]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-003 with Frappe Lending, so there is no verdict.

## Business need

“Where a call to an external system fails or times out, the platform shall not infer an outcome. It shall query the external system for the definitive state before any retry or status change. Absence of a response is not a response.” (BR-GOV-003, BRD 3.4, PDF page 19). See `concept.BR-GOV-003` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-003 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Disbursement** is the document that records a payout.
- **Error Log** is Frappe's list of errors raised by the code.
- The code for Loan Disbursement is in `lending/loan_management/doctype/loan_disbursement/loan_disbursement.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-003 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List every place the payout document above sends a request to another system.
2. Read the code around each for what is stored when no reply arrives.
3. Ask NRB how the platform can query the state of an earlier instruction (BR-INT-006).

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
