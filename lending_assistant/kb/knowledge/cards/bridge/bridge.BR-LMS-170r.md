---
id: bridge.BR-LMS-170r
type: bridge
title: Catch payments made directly in the CBS
summary: "Gap (needs the CBS link). Frappe Lending has no feed of CBS transactions, so it cannot see a payment or reversal made directly in the CBS."
br_ids: [BR-LMS-170]
brd_section: 7.7
doctypes: [Loan Repayment, Bank Transaction]
verdict: gap_cbs
analysis_status: verified
dev_items: [D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-170r"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-170r"
  - "sources/verification/verification_report.md#BR-LMS-170r"
  - "sources/verification/FINAL_REPORT.md#D13"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-170"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-170"
related: [concept.BR-LMS-170r, devitem.D13, bridge.BR-LMS-171r, bridge.BR-LMS-169]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap (needs the CBS link). Frappe Lending has no feed of CBS transactions, so it cannot see a payment or reversal made directly in the CBS.

## Business need

Payments and reversals made directly in the CBS must be detected by reconciliation and corrected by a controlled repost, which redoes the postings from a date (BR-LMS-170 in section 7.7, BRD PDF page 51). See `concept.BR-LMS-170r`. This is the 7.7 card; the collateral requirement with the same number, in section 7.8, has its own card.

## Frappe Lending today

Nothing. The team checked the installed 16.5.1 metadata: there is no CBS transaction feed document and no interface for one. ERPNext's Bank Transaction exists but has no loan field. The correction tool, Loan Repayment Repost, exists (see `bridge.BR-LMS-169`), but nothing tells it what to correct.

## Match or gap, and why

This is a **gap (needs the CBS link)**, not an ordinary gap. The missing piece is data: the loan system must be told what happened in the CBS, and that cannot be built inside Frappe alone. It depends on a decision NRB has not made. BRD section 7.7.2 says there is no interface and therefore no notification, so detection will be a pull: a scheduled transaction extract, an account-level read, or a file from the bank. The BRD adds that the cycle chosen sets how stale the platform's view of days past due can become (PDF page 52).

## What to do today

Compare the CBS statement with the submitted Loan Repayment list by hand, every day, and use a Loan Repayment Repost for corrections. Record every difference in a shared log.

## Planned fix

D13 (`devitem.D13`), the CBS and RPA posting bridge. It is sized L (over three weeks) and needs the accounting-date fix ND-12 first. The BRD's reconciliation reporting for this rule sits in `bridge.BR-LMS-171r` and D10.
