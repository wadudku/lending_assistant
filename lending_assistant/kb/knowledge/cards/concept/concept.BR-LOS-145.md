---
id: concept.BR-LOS-145
type: concept
title: Sampling outcomes feed partner quality figures and can raise a partner's rate
summary: "Sampling outcomes roll up into partner quality metrics: rejection rate overall and by reason, trend over time and comparison across partners; a breach of a configured threshold alerts the Bank and may raise that partner's rate automatically."
br_ids: [BR-LOS-145]
brd_section: 6.5.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-145"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-137"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-106"
related: [bridge.BR-LOS-145, concept.BR-LOS-137, concept.BR-LOS-106, concept.BR-LOS-140, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** Sampling outcomes roll up into partner quality metrics: rejection rate overall and by reason, trend over time and comparison across partners; a breach of a configured threshold alerts the Bank and may raise that partner's rate automatically.

## What the rule says

BR-LOS-145 (Must, BRD 6.5.1, PDF page 37) says sampling outcomes roll up into partner quality metrics: sample rejection rate overall and by reason code, trend over time, and comparison across partners. Where a partner's rejection rate breaches a configurable threshold the platform alerts the Bank and, subject to configuration, escalates that partner's sampling rate automatically. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a partner whose files are often rejected needs closer review, and the Bank should hear about it without having to look. The rejection-rate rule also appears in BR-LOS-137 (PDF page 36).

## Example

Partner A's rejections reach 12% against a threshold of 8%. The Bank gets an alert, and, as configured, the platform raises Partner A's sampling rate from 10% to 20% for later batches.

## Terms to know

- **Rejection rate:** the share of sampled applications that a reviewer rejected.
- **Roll up:** add the individual outcomes into a summary.
- **Escalate:** raise the rate automatically.
- **Alert:** a message sent to the Bank to warn it.
