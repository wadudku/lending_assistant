---
id: bridge.BR-LMS-114
type: bridge
title: The order in which a payment is used
summary: "Partly covered. The four payment orders can be set. In the test, the Interest component was never paid, one order paid a bill twice, and the Company logic setting is not read. The coverage analysis rated it covered."
br_ids: [BR-LMS-114]
brd_section: 7.2
doctypes: [Company, Loan Product, Loan Repayment]
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:1817", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:2525", "lending/install.py:129"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-114"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-114"
  - "sources/verification/verification_report.md#BR-LMS-114"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-114"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-114"
related: [concept.BR-LMS-114, brd_section.7.2, bridge.BR-LMS-164, glossary.allocation-order]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The four payment orders can be set. In the test, the Interest component was never paid, one order paid a bill twice, and the Company logic setting is not read. The coverage analysis rated it covered.

## Business need

The bank wants the order in which a payment clears charges, penalty, interest and principal to be configurable by asset class and collection type (BR-LMS-114, BRD 7.2, PDF page 47). See `concept.BR-LMS-114`.

## Frappe Lending today

Four payment orders (**Loan Demand Offset Order**) can be set on the Company and overridden on the **Loan Product**: Standard, Sub Standard, Written Off and Settlement. The repayment picks one in this order (`loan_repayment.py` lines 1817-1838): the Written Off order for a written-off loan; the Settlement order for the repayment types Partial Settlement, Full Settlement, Principal Adjustment and Principal Capitalization, or for a Settled loan (except the three waiver types); the Sub Standard order when the loan has the NPA flag; otherwise the Standard order. The product's order is used first, then the Company's (`loan_repayment.py` lines 2525-2541). The Company setting **Collection Offset Logic Based On** (NPA Flag or Days Past Due) is not read by any Python code in 16.5.1 (grep: it appears only in `install.py` line 129 and line 139, where the field is created).

## Match or gap, and why

This is **partly covered**. The coverage analysis rated it covered; verification found that the orders do not all work (verification_report.md:55, 134, 669). In the test, the site's NPA order skipped 259.88 of billed interest, because the Interest component is never matched (DEF-3; the cause is explained in `bridge.BR-LMS-164`). In the test, an order that named Principal and the EMI component paid one bill twice (DEF-8). In the tests, only orders built from the EMI component worked, and they pay interest first within each EMI. In the test, the settlement order skipped interest too: a full settlement of 84,000 paid principal of 80,000, refunded 3,332.13 to the borrower, and waived 4,277.18 of interest. The days-past-due option in the Company setting has no effect, because the order is chosen by the NPA flag (`loan_repayment.py` line 1833), not by days past due.

## What to do today

Build the orders from the EMI component and Additional Interest, and open Repayment Details after each payment to confirm interest was cleared. Do not pick Days Past Due in the Company setting expecting a change.

## Planned fix

ND-10 in the verification report fixes the Interest component, stops one bill being paid twice, and validates the order form. An NPA order of "principal, then interest" can only be offered after that.
