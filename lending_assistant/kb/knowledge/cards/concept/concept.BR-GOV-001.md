---
id: concept.BR-GOV-001
type: concept
title: The platform never holds money or books entries itself
summary: "The platform never keeps a money balance, posts to the bank's books or moves money on its own; it sends instructions to the bank's core system and records the replies."
br_ids: [BR-GOV-001]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-GOV-001, glossary.cbs, concept.BR-GOV-002, concept.BR-GOV-004]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform never keeps a money balance, posts to the bank's books or moves money on its own; it sends instructions to the bank's core system and records the replies.

## What the rule says

BR-GOV-001 (Must, BRD 3.4, PDF page 19) says the platform never holds a financial balance, never posts an accounting entry to the Bank's books, and never moves money on its own authority. Every financial action is an instruction issued to the Core Banking System (CBS) and a record of the response received. BRD 3.4 lists it among the guiding principles that are binding on the design: a design that conflicts with one needs written approval from NRB Bank.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bank keeps one official set of books, and a second system that also held balances could disagree with it. The surrounding rules point the same way: the CBS is authoritative for all facts after a loan is booked (BR-GOV-004, PDF page 19), and every instruction carries a unique key so a repeat cannot pay twice (BR-GOV-002, PDF page 19).

## Example

A customer's instalment arrives. The platform does not change any bank balance itself. It sends the CBS an instruction to post the amount, then stores the CBS reply (accepted, with a reference) as its own record of what happened.

## Terms to know

- **CBS:** the bank's main system, which holds the official accounts. See `glossary.cbs`.
- **Instruction:** a request the platform sends to another system to do something.
- **Authoritative:** the system whose figure is taken as correct when two systems differ.
- **Posting:** recording a money movement in the books.
