---
id: brd_section.7.2
type: brd_section
title: BRD 7.2 Product and servicing configuration
summary: "Section 7.2 says loan behaviour must come from product configuration that business users can change under maker-checker, without a software release."
br_ids: []
brd_section: 7.2
doctypes: []
dev_items: [D4, D5, D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.2-product-and-servicing-configuration"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.2-product-and-servicing-configuration"
  - "sources/verification/reqs.json#BR-LMS-110"
related: [devitem.D4, devitem.D5, devitem.D13, glossary.moratorium, glossary.allocation-order, glossary.emi, glossary.maker-checker, glossary.partner, glossary.effective-date]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.2 says loan behaviour must come from product configuration that business users can change under maker-checker, without a software release.

## What this section says

BRD 7.2 (PDF pages 46 and 47, 8 requirements, BR-LMS-110 to BR-LMS-117) lists what a product must be able to set. It covers the schedule methods (110: monthly equated instalment, pro-rated, cycle-date, flat interest and revolving line of credit), the rate and its repricing rule (111), moratorium rules (112), charges and their accounts (113), the payment allocation order (114) and the two accounting modes (115). Co-lending partners are linked to a product (116). All configuration is versioned and effective-dated under maker-checker, and each loan records the version it was booked under (117).

## Why the bank wants it

The BRD gives its reason under the section heading (PDF page 46): servicing behaviour is driven entirely by product configuration, so a new lending product can be introduced, or an existing one amended, by authorised business users under maker-checker without a software release.

## How it meets Frappe Lending

Of the 8 requirements, the verified result on 16.5.1 is 2 covered (110, 116); 5 partly covered (111, 112, 113, 114, 115); 1 a gap (117). Verification moved 3 of these verdicts: 112, 113, 114. Dev items: D4 (floating-rate setup), D5 (versioned, approved configuration) and D13 (the CBS and RPA posting bridge, which BR-LMS-115 depends on).

## Related cards

Dev items: `devitem.D4`, `devitem.D5` and `devitem.D13`. Terms: `glossary.moratorium`, `glossary.allocation-order`, `glossary.emi`, `glossary.maker-checker`, `glossary.partner`, `glossary.effective-date`.
