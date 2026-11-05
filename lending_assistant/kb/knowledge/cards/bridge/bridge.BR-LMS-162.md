---
id: bridge.BR-LMS-162
type: bridge
title: Apply each payment only once
summary: "Gap. Reference Number exists but is not unique, and the test showed one reference accepted twice, with both payments posted to the accounts."
br_ids: [BR-LMS-162]
brd_section: 7.7
doctypes: [Loan Repayment]
verdict: gap
analysis_status: verified
dev_items: [D12]
fields: [Loan Repayment.Reference Number]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment/loan_repayment.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-162"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-162"
  - "sources/verification/verification_report.md#BR-LMS-162"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-162"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-162"
related: [concept.BR-LMS-162, devitem.D12, bridge.BR-LMS-160, bridge.BR-LMS-161]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. Reference Number exists but is not unique, and the test showed one reference accepted twice, with both payments posted to the accounts.

## Business need

A payment must be applied exactly once, keyed on the CBS transaction reference, however often it is reported (BR-LMS-162, BRD 7.7.1, PDF page 51). See `concept.BR-LMS-162`.

## Frappe Lending today

**Loan Repayment** has a **Reference Number** field. It is a plain text field: not unique and not mandatory. The verification test submitted a Normal Repayment and then a Pre Payment, both with the same reference. Both were accepted and both posted accounting entries. The duplicate Pre Payment also created a Loan Restructure (a record that changes the loan's terms) on its own and rescheduled the loan.

## Match or gap, and why

This is a **gap**. Nothing in Frappe Lending checks the reference, so a single repeated entry changes the loan twice, and with a Pre Payment it even changes the repayment plan. Undoing it is hard: in 16.5.1 no role is allowed to cancel the Loan Restructure the duplicate created, so only Administrator can reverse it (ND-9 in the verification report).

## What to do today

Before submitting any repayment, search the Loan Repayment list for the same reference. Do this especially for Pre Payment and Advance Payment, which also reshape the schedule. Do not rely on the form to stop a repeat.

## Planned fix

D12 (`devitem.D12`) adds a uniqueness check on the reference (together with the channel) across submitted repayments. The verification added ND-6: also block duplicate Pre Payment and Advance Payment, because they trigger a restructure.
