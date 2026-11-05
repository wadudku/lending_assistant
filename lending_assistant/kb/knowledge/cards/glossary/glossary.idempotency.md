---
id: glossary.idempotency
type: glossary
title: Idempotency
summary: "A rule that doing the same thing twice has the effect of doing it once, so a repeated instruction cannot create a duplicate payment or posting."
br_ids: [BR-LMS-162]
brd_section: 7.7
doctypes: [Loan Repayment]
dev_items: []
terms: [idempotency, idempotent, apply once]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-162"
related: [bridge.BR-LMS-162, devitem.D12]
version: 1
status: approved
approved_by: Owner
---
**In short:** A rule that doing the same thing twice has the effect of doing it once, so a repeated instruction cannot create a duplicate payment or posting.

## Plain meaning

The BRD defines idempotency as the property that repeating the same instruction cannot create a duplicate financial effect (BRD 1.5).

## Example

Rahim's 9,000 payment arrives from the bank twice with the same reference. An idempotent system applies it once and recognises the second as a repeat.

## Why it matters here

BR-LMS-162 says a payment is applied once and only once, keyed on the core banking reference. In the test, Frappe Lending accepted the same reference twice, so this is a gap. The BRD also asks for idempotent handoff and repricing batches.

## See also

`bridge.BR-LMS-162`, `devitem.D12`.
