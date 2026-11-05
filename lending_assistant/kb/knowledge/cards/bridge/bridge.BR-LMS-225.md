---
id: bridge.BR-LMS-225
type: bridge
title: Alerts when jobs fail
summary: "Partly covered. Frappe records job runs and errors, and ships an Error Log notification that is switched off. No code in the lending app alerts anyone when a job fails."
br_ids: [BR-LMS-225]
brd_section: 7.13
doctypes: [Loan]
verdict: partial
analysis_status: verified
dev_items: [D9]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-225"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-225"
  - "sources/verification/verification_report.md#BR-LMS-225"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-225"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-225"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D9"
related: [concept.BR-LMS-225, bridge.BR-LMS-223, bridge.BR-LMS-224, devitem.D9]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Frappe records job runs and errors, and ships an Error Log notification that is switched off. No code in the lending app alerts anyone when a job fails.

## Business need

Scheduled and integration jobs must be monitored, and must alert on failure or repeated failure instead of failing silently (BR-LMS-225 in section 7.13, BRD PDF page 55). See `concept.BR-LMS-225`.

## Frappe Lending today

Frappe keeps a Scheduled Job Log and an Error Log. Frappe also ships a notification template named Error Log, which sends an email to the System Manager role for each new Error Log row. It is shipped switched off (in the Frappe app, the Error Log template file has enabled set to 0). In the test, after a demand run failed for two loans, the Scheduled Job Log still said Complete, and no email, notification or ToDo was created.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J11). The means exist and none is on.

- The Scheduled Job Log recorded 436 Complete and 2 Failed in all its history, so a job that catches its own error and logs it still counts as complete.
- The shipped notification would email every new Error Log row, which needs outgoing email to be set up. It sends no SMS, has no rule for a run of consecutive failures, and puts no loan information in the subject.
- So a failure goes unnoticed today; the BRD asks for the opposite.

## What to do today

Switch on the Error Log notification in a test copy of the site and check what it sends. Until an alert is in force, have a named person open the Error Log and the Scheduled Job Log every morning and record that it was done.

## Planned fix

Dev item D9 (batch run and exception framework, sized large) covers this row. The final report proposes ND-44 (a failure queue and an alert, medium). It also lists question Q10 to NRB about who owns a failed night and after how many failures to alert.
