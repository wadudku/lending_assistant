---
id: concept.BR-LOS-203
type: concept
title: "If the account opens but payment fails, the application holds and an exception is raised"
summary: "If account opening succeeds and disbursement fails, the application holds at account opened and an exception is raised, with no silent retry loop."
br_ids: [BR-LOS-203]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-203"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [bridge.BR-LOS-203, concept.BR-LOS-202, concept.BR-LOS-204]
version: 1
status: approved
approved_by: Owner
---
**In short:** If account opening succeeds and disbursement fails, the application holds at account opened and an exception is raised, with no silent retry loop.

## What the rule says

BR-LOS-203 (Must, BRD 6.9, PDF page 43) says that where account opening succeeds and disbursement fails, "the application shall hold at account opened and an exception shall be raised". It adds "It shall not be silently retried in a loop." So there is a named holding state, a raised exception and a ban on retrying silently.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a payment that keeps being retried unseen could end up being made twice, which the BRD names as the controlling risk for 6.9 on PDF page 43.

## Example

A loan account is opened but the disbursement fails. The application stays at account opened and an exception is raised for someone to look at. The platform does not keep trying by itself.

## Terms to know

- **Account opened:** the state the BRD says the application holds at.
- **Exception:** an item raised for a person to deal with; see the exceptions workspace in BR-LOS-213.
