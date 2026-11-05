---
id: brd_section.5.4
type: brd_section
title: BRD 5.4 The handoff control
summary: "Section 5.4 holds five rules for the handoff: one complete package, servicing accepts only a complete confirmed one, a repeat never creates a second loan, a daily comparison, and a controlled opening-balance load."
br_ids: [BR-LOS-010, BR-LMS-010, BR-LMS-011, BR-GOV-030, BR-GOV-031]
brd_section: 5.4
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.4"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-011"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-030"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-031"
related: [bridge.BR-LOS-010, bridge.BR-LMS-010, bridge.BR-LMS-011, bridge.BR-GOV-030, bridge.BR-GOV-031]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 5.4 holds five rules for the handoff: one complete package, servicing accepts only a complete confirmed one, a repeat never creates a second loan, a daily comparison, and a controlled opening-balance load.

## What this section says

BRD 5.4 (PDF page 28) holds five requirements. BR-LOS-010: on confirmed disbursement the LOS sends the funded loan to the LMS as one complete handoff package. BR-LMS-010: the LMS accepts a loan only if the package is complete and carries a confirmed disbursement reference; an incomplete or unconfirmed one goes to an exception queue with a reason and creates no loan. BR-LMS-011: the handoff is idempotent, so a repeat for the same origination reference returns the original loan and never creates a second. BR-GOV-030: a daily control compares confirmed disbursements in origination with loans booked in servicing, and raises every difference in either direction as an exception needing documented closure. BR-GOV-031: the existing loan book moves into servicing through a controlled opening-balance import with source references, control-total reconciliation and sign-off before cutover.

## Why the bank wants it

The BRD gives the reason in section 3.2: the boundary is a business control that prevents a loan being serviced without being funded, or funded without being serviced (PDF page 17). Section 5.4 states the rules that enforce it.

## How it meets Frappe Lending

The section holds 5 requirements (BR-LOS-010, BR-LMS-010, BR-LMS-011, BR-GOV-030, BR-GOV-031). The team has not analysed them: the analysis covered the 103 servicing requirements of BRD section 7, so this card gives no verdict. Each row has a concept card with the rule and a not-analysed bridge card with pointers only.

## Related cards

Requirement cards: `concept.BR-LOS-010`, `concept.BR-LMS-010`, `concept.BR-LMS-011`, `concept.BR-GOV-030` and `concept.BR-GOV-031` with matching bridge cards. Related: `brd_section.3.2`. Term: `glossary.idempotency`.
