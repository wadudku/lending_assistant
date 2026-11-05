---
id: concept.BR-LOS-150
type: concept
title: The field officer app runs on Android
summary: "The app that field officers use to verify applicants must run on Android, and the bank decides the lowest Android version."
br_ids: [BR-LOS-150]
brd_section: 6.7.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-150"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.1"
related: [bridge.BR-LOS-150, glossary.los, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** The app that field officers use to verify applicants must run on Android, and the bank decides the lowest Android version.

## What the rule says

BR-LOS-150 (Must, BRD 6.7.1, PDF page 39) says the field officer application shall run on Android. It does not name a version. The minimum supported version is "to be confirmed by the Bank based on the standard issued device", so the bank will set it after it knows which device it issues to officers. This is a rule about the officer's own device, in the origination side of the BRD (the LOS, section 6).

## Why the bank wants it

The BRD gives the operating context for all of section 6.7 (PDF page 39): field officers work at gatherings arranged by the partner, often in rural places with unreliable mobile data. They stand rather than sit, work under time pressure with a queue of applicants waiting, and serve applicants who may have limited literacy. The BRD doesn't say why Android is the platform; the usual reason is that low-cost Android devices are common in rural work and the bank can issue one standard model.

## Example

The bank buys one model of Android device for all its field officers. Before the app is built, the bank states the oldest Android version on that model, and the app is then required to run on that version and on newer ones.

## Terms to know

- **Field officer:** the BRD's definition: a bank staff member conducting in-person verification at a partner meeting.
- **Standard issued device:** the device the Bank issues to officers as standard (BR-LOS-150).
- **Minimum supported version:** the lowest Android version the app must run on.
