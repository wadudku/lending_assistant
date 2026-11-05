---
id: concept.BR-LMS-170c
type: concept
title: A master list of collateral
summary: "The platform keeps a master list of the security behind loans: type, description, valuation, price history, the haircut that applies and the resulting eligible value."
br_ids: [BR-LMS-170]
brd_section: 7.8
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-170c"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-170c"
  - "sources/verification/verification_report.md#BR-LMS-170c"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-170"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-170"
related: [bridge.BR-LMS-170c, glossary.ltv, brd_section.7.8, concept.BR-LMS-170r]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform keeps a master list of the security behind loans: type, description, valuation, price history, the haircut that applies and the resulting eligible value.

## What the rule says

BR-LMS-170 in section 7.8 (Must, BRD PDF page 52) says the platform keeps a security master. For each security it records the type, description, valuation, price history, applicable haircut and the resulting eligible value. The BRD uses the number 170 twice. This is the collateral one (card suffix c). The other, in section 7.7, is about payments made directly in the CBS and has its own cards, `concept.BR-LMS-170r` and `bridge.BR-LMS-170r`.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank needs one trusted list of what it holds as security and what each item is worth today, so that every loan can be checked against it.

## Example

Fixed deposit receipt FDR-001 is worth 150,000 and carries a 10% haircut, so its eligible value is 135,000.

## Terms to know

- **Security (collateral):** something the borrower pledges, such as a fixed deposit or shares.
- **Haircut:** a safety cut taken off the market value. See `glossary.ltv` for the related loan-to-value limit.
- **Eligible value:** the value left after the haircut, which is what the bank counts.
- **Price history:** the dated list of prices a security has had.
