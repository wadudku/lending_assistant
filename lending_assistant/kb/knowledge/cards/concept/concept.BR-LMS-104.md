---
id: concept.BR-LMS-104
type: concept
title: Track the approved limit separately from what was taken
summary: "Where the bank approves a limit larger than the amount paid out, the loan system remembers the approved limit and shows how much of it is used."
br_ids: [BR-LMS-104]
brd_section: 7.1
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-104"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-104"
  - "sources/verification/verification_report.md#BR-LMS-104"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-104"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-104"
related: [bridge.BR-LMS-104, brd_section.7.1, glossary.loc, lifecycle.PARTIALLY_DISBURSED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Where the bank approves a limit larger than the amount paid out, the loan system remembers the approved limit and shows how much of it is used.

## What the rule says

BR-LMS-104 (priority Must, BRD 7.1, PDF page 46) applies where a product carries a sanctioned facility limit that is different from the amount funded. In that case the LMS keeps the sanctioned limit reference and tracks utilisation (how much of the limit is used) against it.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bank can approve a facility of one size and pay it out in parts, so the approved size and the paid-out amount are two different numbers that both matter for risk and for what may still be drawn.

## Example

The approved limit is 500,000 BDT and the customer has drawn 300,000. The LMS shows: limit 500,000, used 300,000, available 200,000.

## Terms to know

- **Sanctioned limit:** the amount the bank approved, whether or not it has all been paid out.
- **Utilisation:** the part of the limit that has been drawn.
- **Line of credit:** a facility that can be drawn and repaid again within a limit. See `glossary.loc`.
- **Tranche:** one part of a loan paid out in stages. See `lifecycle.PARTIALLY_DISBURSED`.
