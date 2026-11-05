---
id: brd_section.12
type: brd_section
title: BRD 12 Dependencies on NRB Bank Limited
summary: "Section 12 is a table of 25 things NRB must supply, each with the point at which it is needed."
br_ids: []
brd_section: "12"
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#12"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p70"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p71"
related: [brd_section.9.2, brd_section.15, brd_section.11]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 12 is a table of 25 things NRB must supply, each with the point at which it is needed.

## What this section says

BRD 12 (PDF pages 70 and 71) begins: “The following items are outside the supplier's control and on the critical path. Each is stated with the point at which it is needed.” Its table has 25 dependencies, each with a number, a description and a “Needed by” column. They include access to the Core Banking System for the automation, confirmation of its concurrent-session ceiling, agreement on the durable field for the unique reference, a process for change notices, bureau, election database and SMS gateway arrangements, Bangladesh Bank bands, provisioning percentages and return formats, product configuration, the first scorecard, sampling policy, a delegated authority matrix, opening-balance data, a hosting decision and decisions on repayment collection. The first one, access for the automation, is needed at the “Start of build”, with the words “nothing proceeds without it”. The table does not say that any dependency is in place. This card does not repeat the BRD's dependency numbers, because the team's own development items use similar numbers.

## Why the bank wants it

The BRD gives its reason in the first sentence: the items are “outside the supplier's control and on the critical path” (PDF page 70).

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it.

## Related cards

Related sections: `brd_section.9.2`, `brd_section.11`, `brd_section.15` (change control).
