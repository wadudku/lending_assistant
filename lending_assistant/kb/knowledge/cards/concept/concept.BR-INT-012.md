---
id: concept.BR-INT-012
type: concept
title: Reach the core banking system through a single adapter
summary: "The core banking system is reached through one adapter, so the automation can later be replaced by a real interface without changing the origination or servicing engine."
br_ids: [BR-INT-012]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-012"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-INT-012, glossary.cbs, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** The core banking system is reached through one adapter, so the automation can later be replaced by a real interface without changing the origination or servicing engine.

## What the rule says

BR-INT-012 (Must, BRD 9.2.1, PDF page 62) says the core banking system is reached through a single adapter. If the bank later gets an application interface or middleware, the automation can be replaced behind that adapter without change to the origination or servicing engine.

## Why the bank wants it

The BRD gives the reason in the row: “so that if the Bank later acquires an application interface or middleware the automation can be replaced behind that adapter without change to the origination or servicing engine” (PDF page 62).

## Example

Today the adapter drives the bank's screens. In two years the bank adds an interface. Only the adapter is rewritten to call it; the rest of the platform keeps sending the same instructions as before.

## Terms to know

- **Adapter:** the one piece of software that talks to an outside system.
- **Middleware:** software that sits between two systems and passes messages.
- **Engine:** the part of the platform that runs origination or servicing.
