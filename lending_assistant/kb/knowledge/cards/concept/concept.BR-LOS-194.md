---
id: concept.BR-LOS-194
type: concept
title: "Pass or fail rules are owned by Credit Risk, versioned and checked by a second person"
summary: "The rules that decide pass or fail are owned by Credit Risk, versioned and approved by maker-checker, and each decision records the rule version in force at its own time."
br_ids: [BR-LOS-194]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-194"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [bridge.BR-LOS-194, glossary.maker-checker, concept.BR-LOS-190]
version: 1
status: approved
approved_by: Owner
---
**In short:** The rules that decide pass or fail are owned by Credit Risk, versioned and approved by maker-checker, and each decision records the rule version in force at its own time.

## What the rule says

BR-LOS-194 (Must, BRD 6.8, PDF page 42) says the decision rules "shall be configuration owned by Credit Risk, versioned, and subject to maker-checker". The rule version applied "shall be recorded against every decision, so that two applications decided under different rule versions each show the version in force at their own decision time". So a change to the rules is made and approved by two people, and old decisions keep the version they were made under.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a decision can later be explained by the exact rules in force when it was made, even if the rules have changed since.

## Example

Credit Risk changes a decision rule, and a second person approves the change. An application decided before the change shows the earlier rule version. One decided after it shows the new version.

## Terms to know

- **Maker-checker:** the BRD's term for how changes to the decision rules are controlled; see the glossary term maker-checker.
- **Rule version:** the version of the decision rules the BRD says is recorded against every decision.
