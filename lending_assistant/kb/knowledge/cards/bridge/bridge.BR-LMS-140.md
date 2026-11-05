---
id: bridge.BR-LMS-140
type: bridge
title: Count interest every day (accrual)
summary: "Covered. A daily Process Loan Interest Accrual run counts interest from the balance, rate and the Company day-count convention."
br_ids: [BR-LMS-140]
brd_section: 7.5
doctypes: [Process Loan Interest Accrual, Loan Interest Accrual, Company]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/hooks.py:188", "lending/install.py:81", "lending/loan_management/doctype/loan_interest_accrual/loan_interest_accrual.json:179"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-140"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-140"
  - "sources/verification/verification_report.md#BR-LMS-140"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-140"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-140"
related: [concept.BR-LMS-140, brd_section.7.5, bridge.BR-LMS-111, glossary.bpi]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A daily Process Loan Interest Accrual run counts interest from the balance, rate and the Company day-count convention.

## Business need

The bank wants normal interest counted on the product's accrual frequency from the balance, rate, day-count convention and dates (BR-LMS-140, BRD 7.5, PDF page 49). See `concept.BR-LMS-140`.

## Frappe Lending today

The daily job `schedule_accrual` (`hooks.py` line 188) runs **Process Loan Interest Accrual**. The Company has an accrual frequency field (`install.py` line 81) and the **Interest Day-Count Convention** (`install.py` line 67; see `bridge.BR-LMS-111`). Each accrual is a **Loan Interest Accrual** with an interest type, Normal Interest or Penal Interest (`loan_interest_accrual.json` line 179).

## Match or gap, and why

This is **covered**. In the test, a run scoped to one loan created 33 daily accruals of 19.18 (50,000 x 14% / 365 on the Actual/365 convention), totalling 632.94 against 632.87 billed (verification_report.md:181). The 0.07 difference is the kind of gap that BR-LMS-145 asks a report to explain. Penal interest also accrued daily as separate rows. The coverage analysis rated this row covered, and verification confirmed it.

## What to do today

Let the daily accrual run, or run Process Loan Interest Accrual for a date and loan to check a day.

## Planned fix

Nothing is needed for the accrual itself.
