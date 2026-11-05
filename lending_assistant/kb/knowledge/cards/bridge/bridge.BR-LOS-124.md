---
id: bridge.BR-LOS-124
type: bridge
title: The account is checked again just before the payout
summary: "Not analysed. The team has not compared BR-LOS-124 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-124]
brd_section: 6.3
doctypes: [Loan Disbursement]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_disbursement/loan_disbursement.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-124"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
related: [concept.BR-LOS-124]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-124 with Frappe Lending, so there is no verdict.

## Business need

“Validation shall be performed again immediately before the disbursement instruction is issued. An account that has become dormant, closed or otherwise ineligible in the interim shall halt disbursement and raise an exception.” (BR-LOS-124, BRD 6.3, PDF page 32). See `concept.BR-LOS-124` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-124 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Disbursement** is the document that records a payout.
- The code for Loan Disbursement is in `lending/loan_management/doctype/loan_disbursement/loan_disbursement.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-124 sits in section 6.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the checks that the payout document above makes when it is saved or submitted.
2. Read the code for any call to check the receiving account.
3. Ask NRB how an exception from a failed last check is to be raised and who clears it.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
