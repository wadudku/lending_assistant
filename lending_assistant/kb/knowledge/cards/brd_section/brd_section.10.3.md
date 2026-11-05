---
id: brd_section.10.3
type: brd_section
title: BRD 10.3 Shared entities
summary: "Section 10.3 is a table of five entities shared by both systems: Configuration, AuditEvent, Exception, User and Role, and Notification."
br_ids: []
brd_section: 10.3
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#10.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p66"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p67"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p68"
related: [brd_section.10, brd_section.10.2, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 10.3 is a table of five entities shared by both systems: Configuration, AuditEvent, Exception, User and Role, and Notification.

## What this section says

BRD 10.3 (PDF pages 67 and 68) is a table of five shared entities. Configuration is versioned settings, with key, value, effective dates, maker, checker and justification. AuditEvent is the immutable log, with actor, action, entity, before and after, and timestamp. Exception is an item requiring intervention, with type, owner, raised date, ageing and closure record. User and Role is access control, with organisation scope, roles, function permissions and authority limits. Notification is an outbound message, with template, channel, recipient, delivery state and retry history. The last row, Notification, is on PDF page 68.

## Why the bank wants it

The BRD gives the reason for all of Section 10 in its opening (PDF page 66): the table “establishes the shared vocabulary in which the two systems and the business describe the same things”.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it.

## Related cards

Parent: `brd_section.10`. Term: `glossary.maker-checker`.
