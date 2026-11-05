---
id: concept.BR-LOS-177
type: concept
title: Too many failed liveness tries stop the check and refer the applicant to the Bank
summary: "If an applicant exceeds the liveness attempt limit the verification halts and the applicant is referred to the Bank, and the application is not simply failed."
br_ids: [BR-LOS-177]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-177"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [bridge.BR-LOS-177, concept.BR-LOS-175]
version: 1
status: approved
approved_by: Owner
---
**In short:** If an applicant exceeds the liveness attempt limit the verification halts and the applicant is referred to the Bank, and the application is not simply failed.

## What the rule says

BR-LOS-177 (Must, BRD 6.7.3, PDF page 41) says "exceeding the liveness attempt limit shall halt verification and refer the applicant to the Bank, not fail the application outright". The outcome is a halt and a referral. The application is not rejected at that point.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that repeated failures can come from a poor camera or poor light as well as from a wrong person, so the bank wants a person at the Bank to look at the case before it is closed.

## Example

An applicant fails the liveness check on every allowed attempt. The app stops the verification and tells the officer the applicant is referred to the Bank. The application stays open for the Bank to decide.

## Terms to know

- **Refer to the Bank:** pass the case to Bank staff to decide.
- **Halt:** stop the verification where it is.
