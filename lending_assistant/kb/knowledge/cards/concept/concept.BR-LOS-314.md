---
id: concept.BR-LOS-314
type: concept
title: The field officer's device never holds the score or its logic
summary: "The score, grade, attribute contributions and scorecard logic are never sent to, shown on, cached or logged by the field officer's device; the officer sees only the terms to confirm."
br_ids: [BR-LOS-314]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-314"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p35"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-308"
related: [bridge.BR-LOS-314, concept.BR-LOS-308, glossary.scorecard, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** The score, grade, attribute contributions and scorecard logic are never sent to, shown on, cached or logged by the field officer's device; the officer sees only the terms to confirm.

## What the rule says

BR-LOS-314 (Must, BRD 6.4, PDF page 35) says neither the score, the grade, the attribute contributions nor the scorecard logic is transmitted to, displayed on, cached or logged by the field officer device. The officer sees only the terms to be confirmed. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a field officer who knew the score could coach the applicant towards a better one, and a device can be lost.

## Example

The officer meets the borrower with a device showing the loan amount, tenor and rate to confirm. The device holds no score or grade, in memory or in its logs.

## Terms to know

- **Field officer device:** the device the Bank issues to the officer for the visit (BR-LOS-150).
- **Cached:** kept in the device's temporary storage.
- **Logged:** written to a log file.
- **Terms to be confirmed:** the loan offer the borrower is asked to agree to.
