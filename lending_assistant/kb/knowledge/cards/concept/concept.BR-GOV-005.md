---
id: concept.BR-GOV-005
type: concept
title: "Product behaviour is set by configuration, not code"
summary: "Limits, tenors, rates, eligibility rules and similar product behaviour are settings the bank can change, not logic fixed in the program."
br_ids: [BR-GOV-005]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-005"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-GOV-005, glossary.allocation-order, glossary.provisioning, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** Limits, tenors, rates, eligibility rules and similar product behaviour are settings the bank can change, not logic fixed in the program.

## What the rule says

BR-GOV-005 (Must, BRD 3.4, PDF page 19) says product behaviour is configuration, not code. The BRD lists ceilings, tenors, rates, eligibility rules, required fields, sampling rates, decision rules, offset sequences, classification bands and provisioning percentages.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank changes these values often, and a change should not need a new software release.

## Example

The bank lowers the maximum tenor for one product from 36 to 24 months. An authorised user edits the product setting and the new limit applies to new applications. No program change is needed.

## Terms to know

- **Configuration:** a value or rule the bank can change through settings, without changing the program.
- **Ceiling:** the highest amount or number allowed.
- **Tenor:** the length of a loan, in months.
- **Offset sequence:** the order in which a payment is applied to the parts of what is owed.
