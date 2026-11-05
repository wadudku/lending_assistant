---
id: concept.BR-LOS-190
type: concept
title: The platform asks the bureau and returns only pass or fail to the device
summary: "The platform sends the bureau inquiry through a designated host inside the Bank's permitted network, judges the response against configured rules, and gives the device only a pass or fail."
br_ids: [BR-LOS-190]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-190"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [bridge.BR-LOS-190, concept.BR-LOS-191]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform sends the bureau inquiry through a designated host inside the Bank's permitted network, judges the response against configured rules, and gives the device only a pass or fail.

## What the rule says

BR-LOS-190 (Must, BRD 6.8, PDF page 42) says the platform shall "route the bureau inquiry through a designated host within the Bank's permitted network perimeter", obtain the response, "evaluate it against configured decision rules", and "return only a pass or fail outcome to the device". So four things happen on the platform side, and the device sees one word.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bureau answer then never reaches the officer's device, which is the concern the BRD raises for this whole step on page 42 (see BR-LOS-191), and that bureau inquiries leave the Bank only from one known host.

## Example

An officer finishes the earlier steps for an applicant and the application is sent for bureau verification. The platform makes the inquiry from the designated host, applies the configured decision rules to the response, and tells the officer's device "pass". The device is told nothing else about the bureau's answer.

## Terms to know

- **Designated host:** the BRD's name for the host that sends the inquiry, within the Bank's permitted network perimeter.
- **Decision rules:** the configured rules that turn the bureau response into pass or fail (see BR-LOS-194).
