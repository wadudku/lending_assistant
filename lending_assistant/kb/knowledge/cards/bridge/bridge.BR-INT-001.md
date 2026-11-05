---
id: bridge.BR-INT-001
type: bridge
title: Look up an account in the core banking system
summary: "Not analysed. The team has not compared BR-INT-001 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-001]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [concept.BR-INT-001]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-001 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall obtain, for a given account number, its existence, status, product type, account title, CIF reference and KYC currency, sufficient to satisfy the validation rules in Section 6.3.” (BR-INT-001, BRD 9.2.1, PDF page 61). See `concept.BR-INT-001` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-001 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-001 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which of the six items the core banking system shows on screen.
2. List the fields Frappe Lending holds for a payout account.
3. Compare that list with the six items in the BRD sentence.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
