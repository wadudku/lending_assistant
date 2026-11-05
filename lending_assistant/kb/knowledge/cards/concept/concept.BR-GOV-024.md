---
id: concept.BR-GOV-024
type: concept
title: Every bank and partner account needs a second login factor
summary: Every bank and partner user account must use multi-factor authentication when signing in.
br_ids: [BR-GOV-024]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-024"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [bridge.BR-GOV-024]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every bank and partner user account must use multi-factor authentication when signing in.

## What the rule says

BR-GOV-024 (Must, BRD 4.3, PDF page 23) says all Bank and partner user accounts require multi-factor authentication.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a password alone can be stolen or guessed, and these accounts can reach loan and customer data. The rule covers two groups of people, the bank's own staff and the partners' staff, so a weak sign-in at a partner would be a way into the bank's data. It is a Must, so it is not left to each team to switch on.

## Example

After typing the right password, an officer is also asked for a second proof of identity besides the password. Without it, the sign-in does not complete. The same applies to a partner's staff: a stolen password alone gives no access to the bank's loan data.

## Terms to know

- **Multi-factor authentication:** proving who you are with two or more things, such as a password and a second proof of identity.
