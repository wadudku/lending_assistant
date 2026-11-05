---
id: concept.BR-GOV-006
type: concept
title: Every outside system sits behind a replaceable adapter
summary: "Each link to an outside system goes through an adapter, so replacing that system needs a new adapter and leaves the origination and servicing engine untouched."
br_ids: [BR-GOV-006]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-GOV-006, glossary.cbs, glossary.los]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each link to an outside system goes through an adapter, so replacing that system needs a new adapter and leaves the origination and servicing engine untouched.

## What the rule says

BR-GOV-006 (Must, BRD 3.4, PDF page 19) says every integration is implemented behind an adapter, so that replacing a counterparty system needs a new adapter and no change to the origination or servicing engine.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank may change its core system or a credit bureau, and the cost of that change should stay in one small piece of code.

## Example

The bank moves to a new credit bureau. Only the bureau adapter is replaced. The code that decides a loan application is not touched.

## Terms to know

- **Adapter:** a small piece of code that translates between the platform and one outside system.
- **Integration:** a link between the platform and another system.
- **Counterparty system:** the outside system on the other end of a link.
- **Engine:** the part of the platform that runs the origination or servicing work.
