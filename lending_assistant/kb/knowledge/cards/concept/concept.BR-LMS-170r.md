---
id: concept.BR-LMS-170r
type: concept
title: Catch payments made directly in the CBS
summary: "If someone records or reverses a payment directly in the CBS without the loan system knowing, reconciliation must find it, raise an exception and fix it by a controlled repost."
br_ids: [BR-LMS-170]
brd_section: 7.7
doctypes: []
verdict: gap_cbs
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-170r"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-170r"
  - "sources/verification/verification_report.md#BR-LMS-170r"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-170"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-170"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-004"
related: [bridge.BR-LMS-170r, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** If someone records or reverses a payment directly in the CBS without the loan system knowing, reconciliation must find it, raise an exception and fix it by a controlled repost.

## What the rule says

BR-LMS-170 in section 7.7 (Must, BRD PDF page 51) says a repayment or reversal made directly in the Core Banking System, outside the platform's knowledge, is detected by reconciliation, raised as an exception and applied through a controlled repost. It must never produce a silent divergence between the two positions. The BRD uses the number 170 twice: this is the repayment one (card suffix r). The other, in section 7.8, is about the collateral master.

## Why the bank wants it

The BRD gives the reason in its principles. The CBS is authoritative for every financial fact after booking (BRD 3.3, PDF page 19). The platform keeps its own status for every loan, reconciles it against the CBS daily, and raises any difference as an exception that needs documented closure (BR-GOV-004, PDF page 19). And there is no interface from the CBS, so nothing notifies the platform of a payment made there (BRD 7.7.2, PDF page 52). Without a check, the two systems would quietly disagree about what the borrower owes, and the loan's days past due and grade would be wrong.

## Example

A branch reverses Rahim's 8,979 in the CBS. The next morning's reconciliation raises an exception: the CBS shows CBS-TXN-0001 as reversed, while the loan system still shows it as paid.

## Terms to know

- **Reconciliation:** comparing two records and reporting every difference.
- **Silent divergence:** two systems disagree and nobody notices.
- **Exception:** an item that needs a person to resolve it.
- **Repost:** redoing postings from a date while keeping the old entries.
- **CBS:** the bank's main system. See `glossary.cbs`.
