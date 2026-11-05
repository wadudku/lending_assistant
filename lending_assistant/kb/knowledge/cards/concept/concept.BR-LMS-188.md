---
id: concept.BR-LMS-188
type: concept
title: Report restructures and waivers to Bangladesh Bank
summary: "Every restructure, reschedule and waiver must be reported to Bangladesh Bank and given the classification treatment its rules require, and the platform records which treatment it applied."
br_ids: [BR-LMS-188]
brd_section: 7.9
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-188"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-188"
  - "sources/verification/verification_report.md#BR-LMS-188"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-188"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-188"
related: [bridge.BR-LMS-188, brd_section.7.9, glossary.bb, glossary.asset-classification, decision.restructure]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every restructure, reschedule and waiver must be reported to Bangladesh Bank and given the classification treatment its rules require, and the platform records which treatment it applied.

## What the rule says

BR-LMS-188 in section 7.9 (Must, BRD PDF page 53) says a restructuring, rescheduling or waiver shall be reported to Bangladesh Bank and flagged in classification treatment in accordance with the applicable rules. The platform shall record the regulatory treatment applied to each such event.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the regulator sets how a restructured loan may be graded, so the bank must show it followed the rules for each event.

## Example

Rahim's loan is rescheduled while it is Sub-Standard. Under the Bangladesh Bank rules the record says, for example, "1st reschedule; stays SS until 3 EMIs are paid".

## Terms to know

- **Bangladesh Bank (BB):** the central bank and regulator. See `glossary.bb`.
- **Classification treatment:** how the regulator lets the loan be graded after the event. See `glossary.asset-classification`.
- **Regulatory treatment:** the rule applied, recorded on the event.
