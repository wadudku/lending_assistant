---
id: concept.BR-LOS-174
type: concept
title: "A fingerprint is captured, with a quality score where hardware allows"
summary: "The app takes a fingerprint with a reader on the device and shows a quality score, or with the camera if there is no hardware, in which case it has no score and is only evidence of presence."
br_ids: [BR-LOS-174]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-174"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [bridge.BR-LOS-174, concept.BR-LOS-173]
version: 1
status: approved
approved_by: Owner
---
**In short:** The app takes a fingerprint with a reader on the device and shows a quality score, or with the camera if there is no hardware, in which case it has no score and is only evidence of presence.

## What the rule says

BR-LOS-174 (Must, BRD 6.7.3, PDF page 41) says a fingerprint "shall be captured through integrated hardware where available, with a displayed quality score and retry". Where hardware is unavailable "a fingerprint image shall be captured using the device camera; no quality score is produced in that case and the capture serves as evidence of presence rather than as a matchable biometric".

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a hardware scan can be scored and, in principle, matched, while a camera photo of a finger cannot, so the bank states plainly what each kind of capture is worth.

## Example

An officer's device has a fingerprint reader. The applicant presses a finger, sees a low quality score, and retries. On another device with no reader, the officer photographs the finger with the camera. No score is shown, and the image is kept only as evidence that the applicant was there.

## Terms to know

- **Integrated hardware:** a fingerprint reader built into the device.
- **Quality score:** the score displayed for a hardware capture.
- **Matchable biometric:** the BRD's term for a capture that can be matched; a camera image of a finger is not one.
