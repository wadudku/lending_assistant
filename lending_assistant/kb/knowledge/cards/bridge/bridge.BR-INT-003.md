---
id: bridge.BR-INT-003
type: bridge
title: Open the loan account in the core banking system and keep its number
summary: "Not analysed. The team has not compared BR-INT-003 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-003]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [concept.BR-INT-003]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-003 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall open a loan account in the Core Banking System, supplying the borrower reference, product code and sanctioned terms, and shall read back and retain the loan account number as displayed by that system.” (BR-INT-003, BRD 9.2.1, PDF page 61). See `concept.BR-INT-003` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-003 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the Frappe Lending document for a loan.
- BR-LMS-100 (`bridge.BR-LMS-100`) is a related servicing requirement the team analysed, about accepting only loans that are really paid out. Its result does not apply to BR-INT-003.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-003 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which fields the loan account opening screen needs.
2. List where Frappe Lending holds the borrower reference, product and terms.
3. Find where an external loan account number could be stored against the loan.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
