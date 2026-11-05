---
id: concept.BR-LOS-230
type: concept
title: "Administrators manage users, roles and permissions for the Bank and partners"
summary: "Platform administrators manage users, roles and function-level permissions for Bank and partner organisations, with onboarding by invitation and a forced password reset on first use."
br_ids: [BR-LOS-230]
brd_section: 6.11
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-230"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.11"
related: [bridge.BR-LOS-230, concept.BR-LOS-222]
version: 1
status: approved
approved_by: Owner
---
**In short:** Platform administrators manage users, roles and function-level permissions for Bank and partner organisations, with onboarding by invitation and a forced password reset on first use.

## What the rule says

BR-LOS-230 (Must, BRD 6.11, PDF page 45) says platform administrators "shall manage users, roles and function-level permissions for both Bank and partner organisations, with invitation-based onboarding and forced password reset on first use".

## Why the bank wants it

The BRD doesn't say why; the usual reason is that every user, at the bank and at a partner, gets only the access their role needs, and starts with a password only they know.

## Example

An administrator invites a new partner user. The user must set a new password the first time they sign in, and sees only the functions their role allows.

## Terms to know

- **Function-level permission:** permission to use a particular function, as the BRD uses the term.
- **Invitation-based onboarding:** a user is added by being invited, as the BRD says.
