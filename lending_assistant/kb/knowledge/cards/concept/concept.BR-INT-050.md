---
id: concept.BR-INT-050
type: concept
title: Send one-time passcodes by SMS for multi-factor sign-in
summary: The platform sends one-time passcodes by SMS for multi-factor authentication.
br_ids: [BR-INT-050]
brd_section: 9.7
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-050"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [bridge.BR-INT-050]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform sends one-time passcodes by SMS for multi-factor authentication.

## What the rule says

BR-INT-050 (Must, BRD 9.7, PDF page 65) says SMS is issued to deliver one-time passcodes for multi-factor authentication. The inventory in 9.1 lists the SMS gateway for one-time passcode delivery and borrower notification, and marks it “Blocking for login; non-blocking for notices” (PDF page 60). So a passcode that cannot be sent stops a user from signing in.

## Why the bank wants it

The BRD gives the reason in the row: the passcodes are “for multi-factor authentication” (PDF page 65).

## Example

A user signs in with a password. The platform sends a six-digit code by SMS to their registered phone. They type the code to finish signing in.

## Terms to know

- **One-time passcode:** a code that works once.
- **Multi-factor authentication:** proving who you are with two or more things, such as a password and a phone.
