---
id: concept.BR-GOV-011
type: concept
title: "Any past date can be reproduced: status, configuration and rules then in force"
summary: "For any application or loan, the platform can show the status it had on a past date and the configuration and rule versions that applied that day."
br_ids: [BR-GOV-011]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-011"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p20"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p20"
related: [bridge.BR-GOV-011, glossary.schedule-version, concept.BR-GOV-009]
version: 1
status: approved
approved_by: Owner
---
**In short:** For any application or loan, the platform can show the status it had on a past date and the configuration and rule versions that applied that day.

## What the rule says

BR-GOV-011 (Must, BRD 3.4, PDF page 20) says the platform can reproduce, for any application or loan at any past date, the status it held on that date and the configuration and rule versions then in force.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that auditors and regulators ask what the bank knew and which rules applied on a given day.

## Example

An auditor asks why a loan was classed as standard on 15 March. The platform shows the loan's status on 15 March and the classification rule version that was in force that day, even though both have changed since.

## Terms to know

- **Reproduce:** show again exactly as it was on a past date.
- **Rule version:** a numbered copy of a rule, so older cases can be checked against the rule of their time.
- **Configuration:** the settings in force, such as rates and bands.
- **Status history:** the list of statuses a record had, with dates.
