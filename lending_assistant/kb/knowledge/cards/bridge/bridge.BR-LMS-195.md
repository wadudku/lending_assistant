---
id: bridge.BR-LMS-195
type: bridge
title: Write-off has its own trigger
summary: "Covered. The Company has a separate setting, Days Past Due Threshold for Auto Write Off, and the nightly classification writes a loan off when it passes it. The setting is one value for the whole company, and a manual write-off is checked only against the pending principal, not against a threshold."
br_ids: [BR-LMS-195]
brd_section: 7.10
doctypes: [Company, Loan Write Off, Process Loan Classification]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Company.Days Past Due Threshold for Auto Write Off]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1359-1361"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-195"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-195"
  - "sources/verification/verification_report.md#BR-LMS-195"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-195"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-195"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [concept.BR-LMS-195, decision.write-off, bridge.BR-LMS-191, devitem.D8]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The Company has a separate setting, Days Past Due Threshold for Auto Write Off, and the nightly classification writes a loan off when it passes it. The setting is one value for the whole company, and a manual write-off is checked only against the pending principal, not against a threshold.

## Business need

Write-off eligibility must be tested against its own threshold, separate from the classification bands (BR-LMS-195 in section 7.10, BRD PDF page 54). See `concept.BR-LMS-195`. The ways a loan can be written off, and what the tolerance on the product does, are in `decision.write-off`.

## Frappe Lending today

The **Company** has a field **Days Past Due Threshold for Auto Write Off** (`lending/install.py:143`). The nightly classification reads it for each company and, when a loan's days past due are above it, creates a **Loan Write Off** for that loan (`lending/loan_management/doctype/loan/loan.py:1359-1361`). The bands that give the grade are a different table (see `bridge.BR-LMS-191`). In the test the company value was 1,080 days. A loan 1,126 days late was written off by the classification run in the same run: a write-off of 100,000 was created and submitted, with the interest waived and the suspense journal posted.

## Match or gap, and why

This is **covered**, and the verification confirmed the verdict (J8). The limits found in the test:

- There is one threshold for the company. The product has no value of its own.
- A manual Loan Write Off is checked only for the amount: it must equal the pending principal (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:63-95`); no check reads days past due or the threshold. A loan with 0 days past due was written off (the write-off was cancelled afterwards). A write-off of 50,000 on a loan whose pending principal was 100,000 was refused.
- The automatic write-off has no approver (DEF-35).

## What to do today

Set the company threshold with Credit Risk's agreement, and have a second person look at every write-off in the Loan Write Off list the morning after the classification runs.

## Planned fix

No development item is assigned. The approval of write-offs comes under D8 (see `decision.write-off`).
