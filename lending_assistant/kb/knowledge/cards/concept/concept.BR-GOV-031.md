---
id: concept.BR-GOV-031
type: concept
title: The existing loan book moves in through a controlled opening-balance load
summary: "The bank's existing loans are moved into servicing through a controlled opening-balance load with principal, interest, penalty and charge balances, source references, control-total reconciliation and formal sign-off before go-live."
br_ids: [BR-GOV-031]
brd_section: 5.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-031"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
related: [bridge.BR-GOV-031, glossary.pos, concept.BR-GOV-009]
version: 1
status: approved
approved_by: Owner
---
**In short:** The bank's existing loans are moved into servicing through a controlled opening-balance load with principal, interest, penalty and charge balances, source references, control-total reconciliation and formal sign-off before go-live.

## What the rule says

BR-GOV-031 (Must, BRD 5.4, PDF page 28) says the platform supports migrating the Bank's existing loan book into servicing through a controlled opening-balance import. The import carries principal, interest, penalty and charge balances, with source references, control-total reconciliation and formal sign-off before cutover.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that old loans must arrive with the right balances, and a total that agrees with the old system, signed off before go-live, shows nothing was lost or doubled.

## Example

The bank loads 5,000 old loans with their balances. The loaded totals for principal, interest, penalty and charges are compared with the old system's totals. They agree, a manager signs the migration off, and only then does the platform go live.

## Terms to know

- **Opening balance:** the amount owed on the day a loan enters the new system.
- **Control total:** a sum from the old system that the loaded data must match.
- **Cutover:** the day the new system takes over.
- **Sign-off:** formal approval by named people.
