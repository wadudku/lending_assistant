---
id: brd_section.3.3
type: brd_section
title: BRD 3.3 System landscape
summary: "Section 3.3 describes six layers of the platform and states what it never does: hold a balance, post to the Bank's books or move money on its own authority."
br_ids: []
brd_section: 3.3
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#3.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p18"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 3.3 describes six layers of the platform and states what it never does: hold a balance, post to the Bank's books or move money on its own authority.

## What this section says

BRD 3.3 (PDF pages 18 and 19) says the platform sits between the origination channel and the Bank's existing systems, and shows a business view (the technical architecture is a design deliverable). A table lists six layers: the channel (Partner Portal, Bank Admin Console, Field Officer App, LMS servicing workspace); the origination engine (workflow, status model, scoring engine, sampling, decision rules, evidence store, immutable audit); the servicing engine (schedule generation and versioning, demand, accrual, allocation, classification, provisioning, restructuring, closure); reporting and reconciliation (dashboards, statements, regulatory extracts, daily reconciliation); the integration layer (one adapter per counterparty, with idempotency keys, retry, circuit breaking and payload logging; for the Core Banking System the adapter drives a robotic process automation runtime, because no programmatic interface exists); and the external systems (Core Banking System, Credit Information Bureau, Election Commission Database, SMS gateway, collection and payment channels). A closing note says the platform never holds a financial balance, posts an accounting entry on its own authority or moves money; where the Bank elects to have the platform keep servicing ledgers, they stay subordinate to the CBS, which is authoritative for every post-booking financial fact.

## Why the bank wants it

The BRD doesn't say why the landscape is laid out this way; the table does say the integration layer isolates the business logic from any one counterparty system and from the manner in which that system is reached (PDF page 18).

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. Its closing note is made a requirement in BR-GOV-001 (section 3.4); the team has not analysed that row. It also describes the origination system (LOS), which the team has not analysed.

## Related cards

Related: `concept.BR-GOV-001`, `concept.BR-GOV-006`. Terms: `glossary.cbs`, `glossary.rpa`, `glossary.idempotency`.
