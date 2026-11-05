---
id: concept.BR-INT-053
type: concept
title: "Passcode messages carry no customer, account or loan identifiers"
summary: "One-time passcode messages do not include customer, account or loan identifiers; this row is a Should, not a Must."
br_ids: [BR-INT-053]
brd_section: 9.7
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-053"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [bridge.BR-INT-053]
version: 1
status: approved
approved_by: Owner
---
**In short:** One-time passcode messages do not include customer, account or loan identifiers; this row is a Should, not a Must.

## What the rule says

BR-INT-053 (Should, BRD 9.7, PDF page 65) says one-time passcode messages do not include customer, account or loan identifiers. It is the only row of 9.7 marked Should; the other four are Must. BR-INT-050 is the row that sends such codes. Both rows are in the notifications part of section 9.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an SMS can be read by anyone who sees the phone's lock screen, so it should reveal only the code.

## Example

The message reads “Your code is 482913”. It does not name the borrower or show an account or loan number.

## Terms to know

- **Identifier:** a name or number that points to a particular person, account or loan.
- **Should:** the BRD's priority for a requirement that is wanted but not mandatory.
