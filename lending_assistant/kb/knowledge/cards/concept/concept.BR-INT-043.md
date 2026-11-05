---
id: concept.BR-INT-043
type: concept
title: "Identity images are encrypted, access-logged and retained under bank policy"
summary: "Identity images and portraits are encrypted at rest, access-logged, and retained under bank policy."
br_ids: [BR-INT-043]
brd_section: 9.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-043"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-043]
version: 1
status: approved
approved_by: Owner
---
**In short:** Identity images and portraits are encrypted at rest, access-logged, and retained under bank policy.

## What the rule says

BR-INT-043 (Must, BRD 9.6, PDF page 64) says identity images and portraits are encrypted at rest, access-logged, and retained in accordance with bank policy. The three duties apply to identity images and to portraits alike. The BRD leaves the retention period to bank policy and does not give a number of years here.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that identity images are sensitive personal data, so the bank wants them unreadable if the storage is taken and wants every viewing recorded.

## Example

A portrait is stored in encrypted form. When a reviewer opens it, the system writes down who opened it and when. After the period set by bank policy, it is removed.

## Terms to know

- **Encrypted at rest:** stored in a form that cannot be read without a key.
- **Access-logged:** every viewing is recorded.
- **Bank policy:** the bank's own rules for how long to keep a record.
