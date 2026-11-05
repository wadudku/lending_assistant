---
id: brd_section.6.2.1
type: brd_section
title: BRD 6.2.1 Duplicate detection
summary: "Section 6.2.1 is the table behind BR-LOS-116: three duplicate-detection scopes, what each matches on and how each is treated."
br_ids: []
brd_section: 6.2.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.2.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.2.1 is the table behind BR-LOS-116: three duplicate-detection scopes, what each matches on and how each is treated.

## What this section says

BRD 6.2.1 (PDF page 30) has a table with three scopes. Within the uploaded batch, rows are matched on NID, account number and mobile number; all matching rows are flagged and the partner resolves them before submission. Against the partner's earlier batches, matched on NID and account number; flagged, and blocked where an earlier application is still in a non-terminal status. Across all partners, platform-wide, matched on NID and account number; blocked and referred to the Bank, and the other partner's identity is not disclosed. A note on cross-partner handling explains that two partners may legitimately hold a relationship with the same individual, and that telling Partner A that Partner B has submitted the same person would leak commercially sensitive information, so the platform blocks the second application with a neutral message and refers it to the Bank, which can see both sides.

## Why the bank wants it

The BRD gives the reason for the cross-partner treatment in the note: disclosing to one partner that another has submitted the same person would leak commercially sensitive information (PDF page 30).

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. It describes the origination system (LOS), which the team has not analysed.

## Related cards

Requirement: `concept.BR-LOS-116`. Related: `concept.BR-LOS-122`, `brd_section.6.2`.
