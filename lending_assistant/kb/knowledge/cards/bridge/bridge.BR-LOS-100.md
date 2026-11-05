---
id: bridge.BR-LOS-100
type: bridge
title: A partner organisation is recorded with its legal and commercial details
summary: "Not analysed. The team has not compared BR-LOS-100 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-100]
brd_section: 6.1
doctypes: [Loan Partner]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_partner/loan_partner.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
related: [concept.BR-LOS-100]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-100 with Frappe Lending, so there is no verdict.

## Business need

“The Bank shall be able to onboard a partner organisation recording legal name, trade licence number, TIN or BIN, registered address, contact persons, agreement reference and date, permitted loan products, maximum applications per batch, maximum aggregate exposure and status.” (BR-LOS-100, BRD 6.1, PDF page 29). See `concept.BR-LOS-100` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-100 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Partner** is the Frappe Lending document for a co-lending partner.
- The code for Loan Partner is in `lending/loan_management/doctype/loan_partner/loan_partner.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-100 sits in section 6.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the partner document above.
2. Compare them one by one with the ten items the BRD lists.
3. Ask NRB which of the items (such as the batch limit and the exposure ceiling) must be kept per partner and which per product.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
