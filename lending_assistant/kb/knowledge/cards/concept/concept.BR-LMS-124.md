---
id: concept.BR-LMS-124
type: concept
title: "\"What-if\" view with nothing saved"
summary: "Staff can show a borrower the effect of a proposed change on screen before it is committed, and nothing is posted or saved."
br_ids: [BR-LMS-124]
brd_section: 7.3
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-124"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-124"
  - "sources/verification/verification_report.md#BR-LMS-124"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-124"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-124"
related: [bridge.BR-LMS-124, brd_section.7.3, devitem.D6, glossary.schedule-version]
version: 1
status: approved
approved_by: Owner
---
**In short:** Staff can show a borrower the effect of a proposed change on screen before it is committed, and nothing is posted or saved.

## What the rule says

BR-LMS-124 (priority Must, BRD 7.3, PDF page 48) says the platform produces a non-posting schedule simulation. Staff use it to show a borrower the effect of a proposed change before it is committed.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a borrower deciding on an extra payment or a change of term needs to see the result first, and trying options must not leave records or change the loan.

## Example

"If you pay 20,000 extra today, your EMI stays 8,979 and you finish 2 to 3 months earlier." It is shown on screen only; nothing is posted.

## Terms to know

- **Simulation (what-if):** a calculation shown on screen that changes nothing.
- **Non-posting:** no accounting entry and no change to the loan record.
- **Schedule version:** one state of the repayment plan. See `glossary.schedule-version`.
