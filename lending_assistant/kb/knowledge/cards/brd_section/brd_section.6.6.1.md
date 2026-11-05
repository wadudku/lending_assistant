---
id: brd_section.6.6.1
type: brd_section
title: BRD 6.6.1 Sanction routing
summary: "Section 6.6.1 is the routing table for sanction: four cases, where each goes and how it is recorded."
br_ids: []
brd_section: 6.6.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.6.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.6.1 is the routing table for sanction: four cases, where each goes and how it is recorded.

## What this section says

BRD 6.6.1 (PDF page 39) has a table with four cases. An application within every auto-sanction threshold, with no sampling rejection and no condition triggered, is sanctioned by the system on the proposed terms and recorded as a system decision naming the threshold rule and version. An application outside any one threshold (amount, grade, tenor, product or partner) goes to the credit approval queue, is decided within delegated authority and recorded as a user decision naming the approver and the limit relied on. An application above the acting approver's delegated limit is escalated to the next authority level and the escalation is recorded with both approvers. Where aggregate borrower exposure or the partner ceiling would be breached, the case is blocked before sanction and referred to the Bank, with a system decision recording the limit that was breached.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a sanction must later be traceable to the rule or the person who made it.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. It describes the origination system (LOS), which the team has not analysed.

## Related cards

Requirements: `concept.BR-LOS-321`, `concept.BR-LOS-322`, `concept.BR-LOS-325`, `concept.BR-LOS-328`, `concept.BR-LOS-332`. Related: `brd_section.6.6`.
