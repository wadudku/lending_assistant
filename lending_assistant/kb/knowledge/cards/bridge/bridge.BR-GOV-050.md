---
id: bridge.BR-GOV-050
type: bridge
title: A daily comparison of the platform and the core banking system
summary: "Not analysed. The team has not compared BR-GOV-050 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-050]
brd_section: 8.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-050"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p59"
related: [concept.BR-GOV-050]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-050 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall run a daily reconciliation comparing its own application and loan status against the Core Banking System and servicing position for every record in a post-approval status, and shall produce an exception report of all differences.” (BR-GOV-050, BRD 8.4, PDF page 59). See `concept.BR-GOV-050` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-050 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the Frappe Lending document for a loan, and it holds the loan's status.
- BR-LMS-170r (`bridge.BR-LMS-170r`) is a related servicing requirement the team analysed, about payments made directly in the CBS. Its result does not apply to BR-GOV-050.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-050 sits in section 8.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which fields of the core banking system the platform can read each day.
2. List the status values a loan can hold in Frappe Lending.
3. Compare them with the statuses the core banking system uses.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
