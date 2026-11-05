---
id: brd_section.1.2.2
type: brd_section
title: BRD 1.2.2 Explicitly out of scope
summary: Section 1.2.2 says the platform is not the Core Banking System and lists six other things left out of the specification.
br_ids: []
brd_section: 1.2.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.2.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p10"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 1.2.2 says the platform is not the Core Banking System and lists six other things left out of the specification.

## What this section says

BRD 1.2.2 (PDF page 10) opens: “The Platform is not the Core Banking System.” Neither system builds or replaces NRB's customer, account, payment, general ledger or statement engines. Where an account must be inspected, money must move, or an accounting entry must be posted, the platform issues an instruction to the Core Banking System and records the authoritative response; it never moves money on its own authority. Six more things are excluded: lead capture, lead qualification and marketing campaigns; a borrower-facing mobile application or web portal (Phase 2 consideration); partner commission calculation and settlement (Phase 2); anti-money-laundering and sanctions screening, assumed to be done by NRB outside these systems; any modification to NRB's Core Banking System (a dependency on the Bank and its vendors, with its own cost and timeline); and treasury, deposit products, trade finance and card operations.

## Why the bank wants it

The BRD doesn't say why in this section; the usual reason is that naming what is out of scope prevents misunderstanding about cost and responsibility. The principle that the platform never holds money on its own authority is repeated and made a requirement in BR-GOV-001 (PDF page 19).

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it.

## Related cards

Requirement: `concept.BR-GOV-001`. Term: `glossary.cbs`.
