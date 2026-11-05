---
id: bridge.BR-LOS-133
type: bridge
title: "The sampling rate comes from product, then partner, then global default"
summary: "Not analysed. The team has not compared BR-LOS-133 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-133]
brd_section: 6.5
doctypes: [Loan Product, Loan Partner]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_product/loan_product.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-133"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-135"
related: [concept.BR-LOS-133]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-133 with Frappe Lending, so there is no verdict.

## Business need

“The effective sampling rate shall be resolved in order of specificity: product-level override, then partner-level override, then global default. A rate change shall not alter the selection for a batch already sampled.” (BR-LOS-133, BRD 6.5, PDF page 36). See `concept.BR-LOS-133` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-133 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Product** is the document that holds a loan product's settings.
- **Loan Partner** is the Frappe Lending document for a co-lending partner.
- The code for Loan Product is in `lending/loan_management/doctype/loan_product/loan_product.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-133 sits in section 6.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List where the two documents above could hold a rate for a product and for a partner.
2. Check where a global default could be held.
3. Ask NRB for the current rates at all three levels.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
