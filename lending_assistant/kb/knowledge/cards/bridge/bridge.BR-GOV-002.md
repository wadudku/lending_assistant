---
id: bridge.BR-GOV-002
type: bridge
title: Every outgoing instruction carries a unique key
summary: "Not analysed. The team has not compared BR-GOV-002 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-002]
brd_section: 3.4
doctypes: [Loan Disbursement]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_disbursement/loan_disbursement.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-005"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [concept.BR-GOV-002]
version: 4
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-002 with Frappe Lending, so there is no verdict.

## Business need

“Every outbound financial instruction shall carry a platform-generated idempotency key. A repeat instruction bearing the same key shall never result in a duplicate loan account, a duplicate disbursement or a duplicate posting.” (BR-GOV-002, BRD 3.4, PDF page 19). See `concept.BR-GOV-002` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-002 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Disbursement** is the document that records a payout.
- Its code is in `lending/loan_management/doctype/loan_disbursement/loan_disbursement.py`.
- BR-LMS-162 (`bridge.BR-LMS-162`) is a different, analysed rule about payments coming in. Its result does not apply here.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-002 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List every place where Frappe Lending sends a financial instruction out, starting with the payout document named above.
2. Read its code for a unique reference sent with each payout, and for what happens when the same request is made twice.
3. Ask NRB which durable field in the CBS record will carry the reference (BR-INT-005) and how the state query before and after execution will work (BR-INT-006).

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
