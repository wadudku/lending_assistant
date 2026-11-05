---
id: concept.BR-LOS-206
type: concept
title: "On a screen the automation does not recognise, the platform stops and does not guess"
summary: "If the automation reaches an unrecognised screen, an unexpected message or an ambiguous outcome, the platform halts, holds the application, captures the session evidence and raises an exception, and does not guess."
br_ids: [BR-LOS-206]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-206"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-064"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-LOS-206, glossary.rpa, concept.BR-LOS-204]
version: 1
status: approved
approved_by: Owner
---
**In short:** If the automation reaches an unrecognised screen, an unexpected message or an ambiguous outcome, the platform halts, holds the application, captures the session evidence and raises an exception, and does not guess.

## What the rule says

BR-LOS-206 (Must, BRD 6.9, PDF page 43) says that where the automation encounters "an unrecognised screen, an unexpected message or an ambiguous outcome", the platform shall "halt, hold the application, capture the session evidence and raise an exception for manual resolution". "It shall not guess and shall not proceed to the next step." So there are three triggers and four actions.

## Why the bank wants it

The BRD doesn't say why for this row; the usual reason is that guessing after an unclear result could cause a wrong or repeated payment. The BRD's context for 6.9 on PDF page 43 is that "a screen-driven session gives a weaker guarantee of what did and did not happen than an application interface does".

## Example

During disbursement the automation meets a message it does not recognise. The platform stops, holds the application, saves the evidence of the session and raises an exception for a person to resolve. It does not go on to the next step.

## Terms to know

- **Session evidence:** what is captured from the automation session; BR-INT-064 (BRD 9.3, PDF page 63) says each automation run keeps "the screens traversed, the values entered and the values read back".
- **Manual resolution:** a person deals with the exception.
