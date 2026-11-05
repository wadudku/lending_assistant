---
id: bridge.BR-LMS-190
type: bridge
title: "Count days late every day, and keep the history"
summary: Covered. A daily classification run works out days past due for each loan and writes one Days Past Due Log row per loan per day. The history can be rewritten by back-dated payments and edited by two roles without a trace.
br_ids: [BR-LMS-190]
brd_section: 7.10
doctypes: [Process Loan Classification, Days Past Due Log, Loan]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1495-1518", "lending/hooks.py:191"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-190"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-190"
  - "sources/verification/verification_report.md#BR-LMS-190"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-190"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-190"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D15"
related: [concept.BR-LMS-190, bridge.BR-LMS-192, devitem.D15]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A daily classification run works out days past due for each loan and writes one Days Past Due Log row per loan per day. The history can be rewritten by back-dated payments and edited by two roles without a trace.

## Business need

The platform must calculate days past due every day from unpaid demands and keep a daily history for every loan (BR-LMS-190 in section 7.10, BRD PDF page 53). See `concept.BR-LMS-190`.

## Frappe Lending today

A **Process Loan Classification** run is created every day by the scheduler (`lending/hooks.py:191`). For each loan it finds an unpaid EMI demand, works out the days past due as the days since the demand date with the demand date itself counted as day 1 (`lending/loan_management/doctype/loan/loan.py:1313`), stores the figure on the **Loan**, and writes a **Days Past Due Log** row with the loan, the date and the days past due. If a row already exists for the same loan and date, the code updates it, so there is one row per loan per day (`lending/loan_management/doctype/loan/loan.py:1495-1518`). In the test, 180 daily runs on one loan wrote 180 rows, from 1 to 180 days, with no gaps. The due date counts as day 1.

## Match or gap, and why

This is **covered**, and the verification confirmed the verdict (J4). The caveats from the test:

- A repayment with an earlier value date rewrites the log from that date. The history is replayed, not frozen.
- A classification run entered by hand for yesterday wrote the log row but not the days past due on the Loan (DEF-14).
- The Days Past Due Log is not submittable and has no change tracking. The System Manager and Loan Manager roles can write and delete rows. In the test a row was changed from 0 to 5 and back through the API with no Version row and no activity entry.

## What to do today

Use the log for the daily figure, and treat a past row as correct only if no back-dated payment has been entered since. Limit the Loan Manager and System Manager roles, and keep an outside copy of month-end figures.

## Planned fix

No development item is assigned. The final report proposes ND-15 (append-only logs, with the classification history, D15) and ND-17 (the classification run date, DEF-14).
