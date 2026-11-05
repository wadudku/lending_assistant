---
id: bridge.BR-LMS-184
type: bridge
title: Limits on how much can be restructured
summary: "Gap. The pieces of a limit exist (a Company percentage, a log, a monthly job), but in the test the job could not select any loan and wrote no log row, and nothing checks a limit when a restructure is approved. The original analysis said covered."
br_ids: [BR-LMS-184]
brd_section: 7.9
doctypes: [Loan Restructure, Loan Restructure Limit Log, Process Loan Restructure Limit, Company, Branch, Loan]
verdict: gap
analysis_status: verified
dev_items: []
fields: [Company.Restructure Limit % (Overall)]
lending_version: 16.5.1
code_refs: ["lending/hooks.py:197", "lending/loan_management/doctype/process_loan_restructure_limit/process_loan_restructure_limit.py:26-96"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-184"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-184"
  - "sources/verification/verification_report.md#BR-LMS-184"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-184"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-184"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-184, decision.restructure, bridge.BR-LMS-182]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. The pieces of a limit exist (a Company percentage, a log, a monthly job), but in the test the job could not select any loan and wrote no log row, and nothing checks a limit when a restructure is approved. The original analysis said covered.

## Business need

The platform must enforce restructuring limits by branch and by period, and keep a log of use (BR-LMS-184 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-184`. The other missing controls on a restructure are in `decision.restructure`.

## Frappe Lending today

Three parts exist. The Company has a **Restructure Limit % (Overall)** field (`lending/install.py:55`). A **Loan Restructure Limit Log** document exists to hold the result. A monthly job, `calculate_monthly_restructure_limit`, is scheduled to fill it (`lending/hooks.py:197`). The job is written to read the limit from each Branch (falling back to the Company), sum the loans and the approved and initiated restructures of that branch, and write the log (`lending/loan_management/doctype/process_loan_restructure_limit/process_loan_restructure_limit.py:26-96`). In 16.5.1 on Frappe 16 it fails before it writes anything (see below). In the test the Company limit was 10% and the log had 0 rows.

## Match or gap, and why

This is a **gap**. The original analysis said covered, and the verification moved it from covered to gap (J6).

- The job filters the Loan and the Loan Restructure by a branch field (lines 138, 158 and 173 of the same file). Neither doctype has a field named branch in its definition (`lending/loan_management/doctype/loan/loan.json`, `lending/loan_management/doctype/loan_restructure/loan_restructure.json`). The list of doctypes that can receive an accounting dimension names Loan but not Loan Restructure (`lending/hooks.py:168-177`). So a Branch dimension would not by itself put a branch field on a restructure. In the test the site had no Branch dimension on either doctype, and 0 Branch records.
- The job reads two limit fields from the Branch, but the Branch doctype has only its name, and the app adds no limit field (`lending/install.py` has no Branch field). It also reads a delinquent limit from the Company, which the app does not create.
- In the test, the job's own queries failed under Frappe 16 ("SQL functions are not allowed as strings in SELECT").
- Nothing checks a limit when a restructure is approved, and nothing caps the restructures of one loan: the restructure count is only fetched into the Loan Restructure (`lending/loan_management/doctype/loan_restructure/loan_restructure.json:289-290`) and incremented (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:321-328`), and no code compares it with a cap (DEF-23).

## What to do today

Keep the branch limits and their use in a sheet outside the system, and have a second person check each restructure against it before approval. Do not rely on the monthly job.

## Planned fix

No development item is assigned. The final report proposes ND-24 (add a branch, fix the job, check at approval, medium).
