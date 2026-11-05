---
id: concept.BR-INT-061
type: concept
title: The automation signs in with its own dedicated accounts
summary: "The automation signs in with dedicated service accounts the bank sets up, holding only the privilege its transactions need, and never shared with or used by a person."
br_ids: [BR-INT-061]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-061"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-INT-061, glossary.rpa, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** The automation signs in with dedicated service accounts the bank sets up, holding only the privilege its transactions need, and never shared with or used by a person.

## What the rule says

BR-INT-061 (Must, BRD 9.3, PDF page 62) says the automation signs in with dedicated service accounts provisioned by the bank. They hold the least privilege necessary for the transactions in scope. They are not shared with or used by any human user.

## Why the bank wants it

The BRD gives the reason in section 9.2: “The automation signs in with real Core Banking System credentials holding real transaction rights. It must be treated as a privileged account” (PDF page 61).

## Example

The bank creates a service account used only by the automation, able to open loan accounts and post payouts but not to change limits. No staff member knows its password or uses it to sign in.

## Terms to know

- **Service account:** a sign-in used by software, not by a person.
- **Least privilege:** only the rights needed for the task.
- **Provisioned:** created and handed over by the bank.
