---
id: concept.BR-LOS-151
type: concept
title: The app is tied to one registered officer and one device
summary: "The field app may be installed and used only on a device tied to one registered officer, and a change of device needs an administrator."
br_ids: [BR-LOS-151]
brd_section: 6.7.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-151"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.1"
related: [bridge.BR-LOS-151, concept.BR-LOS-150, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** The field app may be installed and used only on a device tied to one registered officer, and a change of device needs an administrator.

## What the rule says

BR-LOS-151 (Must, BRD 6.7.1, PDF page 39) says the application shall install and operate only on a device "bound to a registered officer". The binding is managed centrally, not by the officer, and a device change "shall require administrative action". An officer cannot move the app to a new device on their own.

## Why the bank wants it

The BRD gives the operating context for all of section 6.7 (PDF page 39): field officers work at gatherings arranged by the partner, often in rural places with unreliable mobile data. They stand rather than sit, work under time pressure with a queue of applicants waiting, and serve applicants who may have limited literacy. The BRD doesn't say why a device is bound to one officer; the usual reason is that the app holds applicant identity data, so the bank wants to know which person and which device produced every capture, and to cut off a lost device.

## Example

An officer's device is stolen. The officer cannot install the app on a borrowed device. A bank administrator records the replacement device against the officer, and only then does the app start working on it.

## Terms to know

- **Device binding:** the app installs and operates only on a device bound to a registered officer.
- **Administrative action:** a change made by a bank administrator, not by the officer.
