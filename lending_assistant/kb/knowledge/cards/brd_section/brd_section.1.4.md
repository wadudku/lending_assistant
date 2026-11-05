---
id: brd_section.1.4
type: brd_section
title: BRD 1.4 How to read this document
summary: "Section 1.4 explains that the BRD states business needs, not technical design, and how requirement numbers, priorities and boxed notes work."
br_ids: []
brd_section: 1.4
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.4"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p10"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p11"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 1.4 explains that the BRD states business needs, not technical design, and how requirement numbers, priorities and boxed notes work.

## What this section says

BRD 1.4 (PDF pages 10 and 11) says this is a business requirements document, not a technical specification: screen design, data model, API contracts and technology selection follow later. Requirements are numbered for review, change control and acceptance testing, with four prefixes: BR-LOS-nnn (origination), BR-LMS-nnn (servicing), BR-INT-nnn (integration with an external system) and BR-GOV-nnn (governance, access control or audit, for both systems). Each requirement carries one of four priorities: Must (required for go-live), Should (the Bank can go live without it and absorb a manual workaround for a defined period), Could (valuable, scheduled to a later phase unless capacity allows) and Deferred (cannot be stated until the Bank has taken a decision it depends on; not baselined and not estimated; “Section 7.7 is the one such area in this issue”). Boxed notes flag matters that affect scope, cost or regulatory position and need a decision or action from NRB.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that readers need the numbering and priority words defined before they read the rows.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it.

## Related cards

Deferred area: `brd_section.7.7`.
