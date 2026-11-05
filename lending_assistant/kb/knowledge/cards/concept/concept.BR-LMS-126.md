---
id: concept.BR-LMS-126
type: concept
title: Only an approved change may rebuild a plan
summary: "A repayment plan may be rebuilt only because of an approved change, and the new plan records the reason."
br_ids: [BR-LMS-126]
brd_section: 7.3
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-126"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-126"
  - "sources/verification/verification_report.md#BR-LMS-126"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-126"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-126"
related: [bridge.BR-LMS-126, brd_section.7.3, devitem.D6, decision.restructure, glossary.restructuring, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** A repayment plan may be rebuilt only because of an approved change, and the new plan records the reason.

## What the rule says

BR-LMS-126 (priority Must, BRD 7.3, PDF page 48) says schedule regeneration is triggered by, and only by, an approved change: a rate change, tenor change, prepayment, advance payment, restructuring, rescheduling, moratorium grant or scheduled disbursement. The trigger is recorded against the new version.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a plan changes what a borrower owes, so a change that nobody approved would make the figures impossible to defend. The BRD's governing principle is that every posting traces to an approved event (BRD 7 opening, PDF page 46).

## Example

A clerk cannot click "regenerate" to "fix" the numbers. The new plan always says why it exists, for example "trigger: prepayment of 20,000 on 20 August 2026".

## Terms to know

- **Regeneration:** building the plan again.
- **Approved change:** a change that went through the bank's approval for that kind of event (for a restructure, maker-checker; see `glossary.maker-checker`).
- **Trigger:** the event recorded as the reason for the new plan.
- **Restructuring:** see `glossary.restructuring` and `decision.restructure`.
