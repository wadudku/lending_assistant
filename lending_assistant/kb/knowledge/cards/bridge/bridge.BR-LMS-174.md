---
id: bridge.BR-LMS-174
type: bridge
title: Release collateral only after checks and approval
summary: "Partly covered. A release request is checked against the loan, but approval re-checks nothing, two requests can be stacked past the limit, and a whitelisted call releases an assignment with no check. The original analysis said covered."
br_ids: [BR-LMS-174]
brd_section: 7.8
doctypes: [Loan Security Release, Loan Security Assignment]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Security Release.Status]
options: [Loan Security Release.Status=Requested, Loan Security Release.Status=Approved]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_security_release/loan_security_release.py:39-41", "lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.py:257-265"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-174"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-174"
  - "sources/verification/verification_report.md#BR-LMS-174"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-174"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-174"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-174, bridge.BR-LMS-171c, devitem.D8]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A release request is checked against the loan, but approval re-checks nothing, two requests can be stacked past the limit, and a whitelisted call releases an assignment with no check. The original analysis said covered.

## Business need

Collateral may be released only after the platform validates the exposure and someone approves (BR-LMS-174 in section 7.8, BRD PDF page 52). See `concept.BR-LMS-174`. The release at loan closure is a separate row (BR-LMS-232).

## Frappe Lending today

A **Loan Security Release** is a request that goes from Requested to Approved. When it is saved or submitted, the code checks that the quantity is pledged and that the loan-to-value would still hold after the release (`lending/loan_management/doctype/loan_security_release/loan_security_release.py:39-41`, and lines 126 to 131 of the same file). In the test, on a 100,000 loan, 90 units were blocked, 87 units (exactly the excess) were accepted, and the pledged quantity fell only when the status was set to Approved. The test covered an open loan only.

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J7).

- Approval is a status edit that does not repeat the check: on update after submit the code only runs the approve step (lines 143 to 152 of the same file). In the test, two requests of 14 units each passed alone and both were approved, leaving 75.4% against a 70% limit (DEF-30).
- The requester and the approver were the same user in the test, and there is no approver field.
- A whitelisted function, `release_loan_security_assignment`, sets an assignment to Released with only a write-permission check (`lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.py:257-265`). In the test it released a 200-unit assignment while 83,231 was outstanding. The screen never offers it, so the hole is for scripts and API calls.
- Assignments stay Pledged after a release.

## What to do today

Check every release by hand against the whole list of pending requests, not one at a time, and have a second person approve outside the system. Remove write access to the Loan Security Assignment from anyone who should not be able to release it.

## Planned fix

No development item is assigned in the verified list. The final report proposes ND-30 (pledge lifecycle and release controls, medium). Maker-checker on releases belongs to D8.
