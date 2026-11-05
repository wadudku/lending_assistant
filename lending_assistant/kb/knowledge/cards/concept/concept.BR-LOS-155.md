---
id: concept.BR-LOS-155
type: concept
title: Screenshots are blocked on screens showing identity data or evidence
summary: The app should stop screenshots on any screen that shows a customer's identity data or the evidence captured from them.
br_ids: [BR-LOS-155]
brd_section: 6.7.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-155"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.1"
related: [bridge.BR-LOS-155, concept.BR-LOS-154, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** The app should stop screenshots on any screen that shows a customer's identity data or the evidence captured from them.

## What the rule says

BR-LOS-155 (Should, BRD 6.7.1, PDF page 40) says the application shall prevent screenshots "on screens displaying customer identity data or evidence". It is a Should, not a Must, so the BRD allows a justified exception. Other screens, which show no identity data or evidence, are not named by the rule.

## Why the bank wants it

The BRD gives the operating context for all of section 6.7 (PDF page 39): field officers work at gatherings arranged by the partner, often in rural places with unreliable mobile data. They stand rather than sit, work under time pressure with a queue of applicants waiting, and serve applicants who may have limited literacy. The BRD doesn't say why; the usual reason is that a screenshot copies a customer's identity data or evidence out of the controlled app into the device's gallery or a chat, where the bank can no longer manage it.

## Example

An officer looks at an applicant's portrait and national ID details on the confirmation screen. If the officer presses the screenshot buttons, no image is saved.

## Terms to know

- **Evidence:** the signature, fingerprint, liveness image and other captures taken as proof of a verification.
- **Should:** a BRD priority: required for a complete solution, but the Bank can go live without it.
