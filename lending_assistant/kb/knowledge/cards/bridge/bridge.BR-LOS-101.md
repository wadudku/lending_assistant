---
id: bridge.BR-LOS-101
type: bridge
title: "Each partner and product pair has its own limits, rates and fields"
summary: "Not analysed. The team has not compared BR-LOS-101 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-101]
brd_section: 6.1
doctypes: [Loan Product, Loan Partner]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_product/loan_product.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-101"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [concept.BR-LOS-101]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-101 with Frappe Lending, so there is no verdict.

## Business need

“Each partner and product pairing shall carry its own configuration: minimum and maximum ticket size, permitted tenors, applicable rate and fees, required application fields, and any sampling rate override.” (BR-LOS-101, BRD 6.1, PDF page 29). See `concept.BR-LOS-101` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-101 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Product** is the document that holds a loan product's settings.
- **Loan Partner** is the Frappe Lending document for a co-lending partner.
- The code for Loan Product is in `lending/loan_management/doctype/loan_product/loan_product.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-101 sits in section 6.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List where the two documents above hold settings for a product and for a partner.
2. Check whether any setting is held for a partner and product together.
3. Ask NRB for the list of fields that differ between partner and product pairs.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
