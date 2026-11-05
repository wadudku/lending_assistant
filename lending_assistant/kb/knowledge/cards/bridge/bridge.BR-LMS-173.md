---
id: bridge.BR-LMS-173
type: bridge
title: Track how a shortfall is fixed
summary: "Partly covered. A shortfall record is closed by the app when security is added or a payment is made, but it has no remedy type, owner, due date or approved exception, and it can close too early or too much."
br_ids: [BR-LMS-173]
brd_section: 7.8
doctypes: [Loan Security Shortfall, Loan Security Assignment, Loan Repayment]
verdict: partial
analysis_status: verified
dev_items: [D20]
fields: [Loan Security Shortfall.Status]
options: [Loan Security Shortfall.Status=Pending, Loan Security Shortfall.Status=Completed]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-173"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-173"
  - "sources/verification/verification_report.md#BR-LMS-173"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-173"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-173"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D20"
related: [concept.BR-LMS-173, bridge.BR-LMS-172, devitem.D20]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A shortfall record is closed by the app when security is added or a payment is made, but it has no remedy type, owner, due date or approved exception, and it can close too early or too much.

## Business need

The platform must track how each shortfall is fixed, with an owner and a due date (BR-LMS-173 in section 7.8, BRD PDF page 52). See `concept.BR-LMS-173`.

## Frappe Lending today

The **Loan Security Shortfall** record has 10 fields and a Status of Pending or Completed. It has no remedy type, owner, due date, approved exception or notes (checked in the metadata). The app closes it, not a person: a new pledge on the loan reduces it, and a repayment triggers a queued update. The form has an Add Loan Security button that opens a new Loan Security Assignment. In the test, a record of 16,000 fell to 10,000 after a top-up pledge worth 6,000; a further 12,000 completed it. When the price recovered, the next run closed the loan-wise record.

## Match or gap, and why

This is **partly covered**, and the verification found it worse than the analysis said (J7).

- A top-up reduced the record by the full pledge value, not the value times the loan-to-value, so the true gap was 11,800, not 10,000. In the test, a further pledge marked it Completed while the true gap was still 3,400; the next run did not reopen it but created a new record.
- Applicant-wise records were never closed by anything in the test.
- The amount, time and run link of a re-run record are overwritten, and closing a record leaves no Version row.
- A repayment made while a loan-wise record was Pending was posted twice for principal (DEF-26), and the record then closed too early (DEF-28).

The record has no field for an approver.

## What to do today

Keep the remedy, owner, due date and any approved exception in a separate log, and check every Completed record against a fresh run before you accept it. Do not take a repayment on a loan with a Pending record without checking the postings.

## Planned fix

Dev item D20 (small items) covers this row; the final report sizes it medium and names a shortfall workflow (ND-28). The two defects that sit under it are ND-26 (the double count) and ND-27 (scope and clean the run).
