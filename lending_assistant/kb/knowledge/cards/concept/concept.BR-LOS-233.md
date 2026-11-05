---
id: concept.BR-LOS-233
type: concept
title: Every decision records the configuration version in force so it can be explained later
summary: "The platform records, against every decision, the configuration version in force at that moment, so a past decision can be explained by the rules then applying."
br_ids: [BR-LOS-233]
brd_section: 6.11
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-233"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.11"
related: [bridge.BR-LOS-233, concept.BR-LOS-232, concept.BR-LOS-194]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform records, against every decision, the configuration version in force at that moment, so a past decision can be explained by the rules then applying.

## What the rule says

BR-LOS-233 (Must, BRD 6.11, PDF page 45) says the platform "shall record, against every decision it takes, the configuration version in force at that moment, so that a past decision can be explained by reference to the rules then applying".

## Why the bank wants it

The BRD gives the reason in the row on PDF page 45: "so that a past decision can be explained by reference to the rules then applying".

## Example

An application is decided today. Months later the configuration has changed. The decision record still shows the configuration version in force on the day it was taken, so the bank can explain it by the rules of that day.

## Terms to know

- **Decision:** a decision the platform takes on an application, as the BRD uses the word.
- **Configuration version:** the version of the configuration in BR-LOS-232.
