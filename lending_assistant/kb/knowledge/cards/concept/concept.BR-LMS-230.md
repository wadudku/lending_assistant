---
id: concept.BR-LMS-230
type: concept
title: Check everything is cleared before closing
summary: "Before a loan closes, the system checks that principal, interest, penalty, charges and every other amount are paid or formally settled, and says what is blocking the closure."
br_ids: [BR-LMS-230]
brd_section: 7.14
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-230"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-230"
  - "sources/verification/verification_report.md#BR-LMS-230"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-230"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-230"
related: [bridge.BR-LMS-230, brd_section.7.14, decision.waiver, decision.write-off, lifecycle.CLOSED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Before a loan closes, the system checks that principal, interest, penalty, charges and every other amount are paid or formally settled, and says what is blocking the closure.

## What the rule says

BR-LMS-230 in section 7.14 (Must, BRD PDF page 55) says that before closure the platform shall validate that principal, interest, penalty, charges and every tracked receivable are cleared or formally resolved, and shall state any residual item preventing closure.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a loan closed with something still owing, or with a hidden write-off, leaves the books and the borrower's record wrong, and a wrong closure is hard to reverse.

## Example

The officer tries to close Rahim's loan and the system answers "Cannot close: penalty of 44 still due." The officer pays the 44 or has it waived by an approved waiver, and only then can the loan close.

## Terms to know

- **Cleared:** paid in full, or waived or written off by a recorded decision.
- **Formally resolved:** settled by an approved waiver, write-off or settlement. See `decision.waiver` and `decision.write-off`.
- **Residual item:** the part still owing that stops the closure.
