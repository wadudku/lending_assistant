---
id: concept.BR-LOS-133
type: concept
title: "The sampling rate comes from product, then partner, then global default"
summary: "The effective sampling rate is the product-level override if there is one, otherwise the partner-level override, otherwise the global default; a rate change never alters a batch that has been sampled."
br_ids: [BR-LOS-133]
brd_section: 6.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-133"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-135"
related: [bridge.BR-LOS-133, concept.BR-LOS-135, concept.BR-LOS-132, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** The effective sampling rate is the product-level override if there is one, otherwise the partner-level override, otherwise the global default; a rate change never alters a batch that has been sampled.

## What the rule says

BR-LOS-133 (Must, BRD 6.5, PDF page 36) says the effective sampling rate is resolved in order of specificity: product-level override, then partner-level override, then global default. A rate change does not alter the selection for a batch already sampled. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the most specific setting should win, and a past pick must not change when the settings change later.

## Example

The global rate is 10%, Partner A has an override of 15%, and Partner A's product P has an override of 25%. A batch for product P from Partner A uses 25%. A later change to 30% leaves the batch already sampled untouched.

## Terms to know

- **Override:** a more specific value that replaces the default.
- **Specificity:** how narrow the setting is: product is narrower than partner.
- **Global default:** the rate used when no override applies.
- **Effective rate:** the rate that is actually used for a batch.
