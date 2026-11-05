---
id: bridge.BR-LMS-171c
type: bridge
title: The life of a pledge
summary: "Partly covered. The pledge statuses match the BRD, but in the test only Pledge Requested and Pledged were used, there is no approval step, and a secured loan was disbursed with no pledge. The original analysis said covered."
br_ids: [BR-LMS-171]
brd_section: 7.8
doctypes: [Loan Security Assignment, Loan Security Release, Loan]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Security Assignment.Status]
options: [Loan Security Assignment.Status=Pledge Requested, Loan Security Assignment.Status=Pledged, Loan Security Assignment.Status=Release Requested, Loan Security Assignment.Status=Released, Loan Security Assignment.Status=Repossessed, Loan Security Assignment.Status=Cancelled]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.py:56-58", "lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.js:6"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-171c"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-171c"
  - "sources/verification/verification_report.md#BR-LMS-171c"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-171"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-171"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-171c, bridge.BR-LMS-171r, bridge.BR-LMS-170c, devitem.D8]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The pledge statuses match the BRD, but in the test only Pledge Requested and Pledged were used, there is no approval step, and a secured loan was disbursed with no pledge. The original analysis said covered.

## Business need

A pledge must move through set states, each move authorised and recorded (BR-LMS-171 in section 7.8, BRD PDF page 52). See `concept.BR-LMS-171c`. This is the collateral row. The 7.7 row with the same number has its own cards (`bridge.BR-LMS-171r`).

## Frappe Lending today

The **Loan Security Assignment** has a Status field with the BRD's names: Pledge Requested, Pledged, Release Requested, Released, Repossessed and Cancelled, plus Unpledged (`lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.json:83`). In the test only two moves happened: a draft was Pledge Requested, and submitting it made it Pledged at once, with no approver. The code does this on submit when there is no Loan Application (`lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.py:56-58`). Cancelling sets Cancelled (line 83 of the same file). Releasing collateral is a separate record, the **Loan Security Release**, which goes from Requested to Approved; in the test, after an approved release of 87 units, all three assignments were still Pledged.

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J7).

- The Status field is read-only on the form (`lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.json:78-86`). The Release button is shown only for Release Requested (`lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.js:6`), so in the test it never appeared.
- Completeness check: a search of the installed app code finds Release Requested, Unpledged and Repossessed only in the list of options, a type annotation, the list-view colours, one report filter and that button test. No code sets them. Pledged is set at line 58 of the assignment code and in `lending/loan_management/doctype/loan/loan.py:637`, Cancelled at line 83, and Released only by a whitelisted call (lines 257 to 265).
- In the test the site had no workflow on the assignment; its only workflows were on Loan Lead and Loan Application.
- A secured loan was disbursed with no pledge, and a pledge of 160,000 doubled the typed maximum loan amount to 320,000 (DEF-31).

## What to do today

Treat the Pledge Requested to Pledged step as one person's action, and record any approval outside the system. Do not use Release Requested, Unpledged or Repossessed statuses: nothing moves a pledge into them. Check by hand that a secured loan has its pledge before disbursement.

## Planned fix

No development item is assigned in the verified list. The final report proposes ND-30 (pledge lifecycle and release controls, medium) and ND-31 (secured-loan integrity and a coverage report, medium). Approval controls in general belong to D8.
