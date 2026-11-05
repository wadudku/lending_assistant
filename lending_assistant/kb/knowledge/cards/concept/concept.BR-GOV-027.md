---
id: concept.BR-GOV-027
type: concept
title: "Sign-ins, permission changes and sensitive views are logged with source and outcome"
summary: "Every sign-in attempt, permission change and privileged data access is logged with who, when, from where and what the result was."
br_ids: [BR-GOV-027]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-027"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [bridge.BR-GOV-027, concept.BR-GOV-025]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every sign-in attempt, permission change and privileged data access is logged with who, when, from where and what the result was.

## What the rule says

BR-GOV-027 (Must, BRD 4.3, PDF page 23) says every authentication attempt, permission change and privileged data access is logged with user, timestamp, source address and outcome.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bank must be able to investigate suspicious access after the fact, and the log is the evidence.

## Example

Someone tries three wrong passwords from an unfamiliar network address and then succeeds. The log shows each attempt with the time, the account, the address and whether it failed or passed.

## Terms to know

- **Authentication attempt:** any try to sign in, successful or not.
- **Source address:** the network address the request came from.
- **Privileged data access:** opening data that needs a special permission.
- **Outcome:** whether the action succeeded or failed.
