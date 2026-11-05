---
id: concept.BR-LOS-102
type: concept
title: A suspended partner can look but not send new batches
summary: "When a partner is suspended, its users can still read existing applications but cannot submit new batches; applications in progress carry on unless someone halts them."
br_ids: [BR-LOS-102]
brd_section: 6.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [bridge.BR-LOS-102, glossary.partner, glossary.batch]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a partner is suspended, its users can still read existing applications but cannot submit new batches; applications in progress carry on unless someone halts them.

## What the rule says

BR-LOS-102 (Must, BRD 6.1, PDF page 29) says a suspended partner's users retain read access to existing applications but are prevented from submitting new batches. Applications already in flight continue to be processed unless separately halted. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that suspending a partner should stop new risk without cutting off borrowers whose applications are already in progress.

## Example

The Bank suspends a partner after an audit finding. The partner's staff can still open their old applications, but the upload screen refuses a new file. A borrower whose application is half through still gets a decision.

## Terms to know

- **Suspended:** a partner status that stops new business but keeps old records visible.
- **In flight:** already submitted and not yet finished.
- **Batch:** a group of applications sent together. See `glossary.batch`.
- **Read access:** the right to view, but not change.
