---
id: concept.BR-LOS-104
type: concept
title: Partner administrators manage only their own organisation's users
summary: "Partner administrators can create, suspend and remove users inside their own organisation only, up to a maximum number of users set by the Bank."
br_ids: [BR-LOS-104]
brd_section: 6.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-104"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [bridge.BR-LOS-104, glossary.partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partner administrators can create, suspend and remove users inside their own organisation only, up to a maximum number of users set by the Bank.

## What the rule says

BR-LOS-104 (Should, BRD 6.1, PDF page 29) says Partner Admins can create, suspend and remove users within their own organisation only, subject to a maximum user count set by the Bank. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the Bank does not want to manage every partner user itself, but must still limit how many people can reach its systems.

## Example

The administrator at Partner A adds a new clerk and removes one who left. The administrator cannot see or change Partner B's users. When Partner A reaches its limit of 10 users, adding an eleventh is refused.

## Terms to know

- **Partner Admin:** a partner staff member allowed to manage that partner's users.
- **Number of users:** the number of user accounts a partner may have.
- **Own organisation only:** no access to another partner's records or users.
- **Should:** a requirement with priority Should, not Must.
