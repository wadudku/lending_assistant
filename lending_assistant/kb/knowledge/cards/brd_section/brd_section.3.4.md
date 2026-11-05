---
id: brd_section.3.4
type: brd_section
title: BRD 3.4 Guiding business principles
summary: "Section 3.4 sets twelve guiding principles that bind the design, such as never holding money, unique keys on every instruction and configuration instead of code."
br_ids: [BR-GOV-001, BR-GOV-002, BR-GOV-003, BR-GOV-004, BR-GOV-005, BR-GOV-006, BR-GOV-007, BR-GOV-008, BR-GOV-009, BR-GOV-010, BR-GOV-011, BR-GOV-012]
brd_section: 3.4
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#3.4"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p20"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-005"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-007"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-008"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-009"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-011"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-012"
related: [bridge.BR-GOV-001, bridge.BR-GOV-002, bridge.BR-GOV-003, bridge.BR-GOV-004, bridge.BR-GOV-005, bridge.BR-GOV-006, bridge.BR-GOV-007, bridge.BR-GOV-008, bridge.BR-GOV-009, bridge.BR-GOV-010, bridge.BR-GOV-011, bridge.BR-GOV-012]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 3.4 sets twelve guiding principles that bind the design, such as never holding money, unique keys on every instruction and configuration instead of code.

## What this section says

BRD 3.4 (PDF pages 19 and 20) says the principles are binding on the design: a design that conflicts with any of them needs written NRB Bank Limited approval before implementation. It holds twelve requirements, BR-GOV-001 to BR-GOV-012. In short: the platform never holds money or books entries (001); every outgoing instruction carries a unique key (002); after a failed call it asks the other system before retrying (003); its status is checked against the core system daily (004); product behaviour is configuration, not code (005); every outside system sits behind a replaceable adapter (006); when an outside system is down the step pauses and retries (007); controlled money changes need two different people (008); financial histories are never overwritten (009); four kinds of date are kept apart (010); any past date can be reproduced (011); and one vocabulary is used across every screen, report and extract (012).

## Why the bank wants it

The BRD doesn't say why; it says the principles are binding, and a design that conflicts with any of them needs written NRB Bank Limited approval before implementation (PDF page 19).

## How it meets Frappe Lending

The section holds 12 requirements (BR-GOV-001 to BR-GOV-012, of which BR-GOV-002 is an approved pilot). The team has not analysed them: the analysis covered the 103 servicing requirements of BRD section 7, so this card gives no verdict. Each row has a concept card with the rule and a not-analysed bridge card with pointers only.

## Related cards

Requirement cards: `concept.BR-GOV-001` to `concept.BR-GOV-012` with matching bridge cards. Terms: `glossary.cbs`, `glossary.idempotency`, `glossary.maker-checker`, `glossary.value-date`, `glossary.posting-date`.
