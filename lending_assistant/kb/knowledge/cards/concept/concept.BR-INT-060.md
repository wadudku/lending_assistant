---
id: concept.BR-INT-060
type: concept
title: The automation runs only inside the bank's network
summary: "The automation runs only on infrastructure the bank designates inside its network, and never sends core banking system content outside that perimeter."
br_ids: [BR-INT-060]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-060"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-INT-060, glossary.rpa, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** The automation runs only on infrastructure the bank designates inside its network, and never sends core banking system content outside that perimeter.

## What the rule says

BR-INT-060 (Must, BRD 9.3, PDF page 62) says the automation runs only within the bank's network, on infrastructure the bank designates. It never transmits core banking system content outside that perimeter.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the core banking system holds customer and account data that the bank may not let leave its own controlled network.

## Example

The automation runs on a machine the bank's ICT team has set up inside the bank's network. A request to copy a screen's content to an outside service is refused, because the content would leave the perimeter.

## Terms to know

- **Perimeter:** the boundary of the bank's own controlled network.
- **Designated infrastructure:** the machines the bank has named for the automation.
- **RPA:** software that drives a system's screens like an operator. See `glossary.rpa`.
