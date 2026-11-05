---
id: brd_section.9.7
type: brd_section
title: BRD 9.7 Notifications
summary: "Section 9.7 sets five rules for notifications: SMS passcodes, borrower notices in Bangla and English, failure handling, what a passcode message may hold, and the bank's confirmation of channels and templates."
br_ids: []
brd_section: 9.7
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.7"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-050"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-051"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-052"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-053"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-054"
related: [brd_section.9, brd_section.9.1, brd_section.7]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 9.7 sets five rules for notifications: SMS passcodes, borrower notices in Bangla and English, failure handling, what a passcode message may hold, and the bank's confirmation of channels and templates.

## What this section says

BRD 9.7 (PDF page 65) has 5 requirements: four Must and one Should (BR-INT-053). BR-INT-050: SMS delivers one-time passcodes for multi-factor authentication. BR-INT-051: borrower notifications on disbursement, instalment due and overdue, approved term change, settlement and closure, through configurable templates in Bangla and English. BR-INT-052: a notification failure is retried and reported, and never blocks or reverses a loan action. BR-INT-053 (Should): passcode messages carry no customer, account or loan identifiers. BR-INT-054: notification channels and the full set of borrower notice templates are to be confirmed by the bank.

## Why the bank wants it

The BRD gives one reason, in BR-INT-050: the passcodes are for multi-factor authentication (PDF page 65). It doesn't say why the other rows are needed.

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section holds 5 requirement rows and none was analysed, so the team makes no statement about them. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.9`. The inventory that lists the SMS gateway: `brd_section.9.1`.
