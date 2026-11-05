---
id: bridge.BR-LMS-194
type: bridge
title: Unpaid interest waits in suspense
summary: "Partly covered. Interest is moved to suspense automatically when a loan turns NPA, but collections while it stays NPA release nothing, and the whole amount is released at once only when the loan is upgraded, settled or written off. The original analysis said covered."
br_ids: [BR-LMS-194]
brd_section: 7.10
doctypes: [Loan, Loan Repayment, Process Loan Classification]
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1654", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:762", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:3584"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-194"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-194"
  - "sources/verification/verification_report.md#BR-LMS-194"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-194"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-194"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-194, lifecycle.NPA, bridge.BR-LMS-191, bridge.BR-LMS-182]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Interest is moved to suspense automatically when a loan turns NPA, but collections while it stays NPA release nothing, and the whole amount is released at once only when the loan is upgraded, settled or written off. The original analysis said covered.

## Business need

Unpaid interest and charges must go to income suspense after NPA treatment and return to income only on actual recovery (BR-LMS-194 in section 7.10, BRD PDF page 54). See `concept.BR-LMS-194`. The NPA state is described in `lifecycle.NPA`.

## Frappe Lending today

When a loan is classified NPA, the code moves its unpaid interest and its receivable charges to suspense accounts (`lending/loan_management/doctype/loan/loan.py:1613-1626`). The release goes the other way when the classification run upgrades the loan: it returns the suspense entries to income through `write_off_suspense_entries` (`lending/loan_management/doctype/loan/loan.py:1654`, and in the back-dated path `lending/loan_management/doctype/loan/loan.py:1603`). The code that would release suspense in step with a payment exists: `post_suspense_entries` on the repayment passes the interest and penalty paid to `write_off_suspense_entries` (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:478`). But it has only two callers: the cancellation of a repayment (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:762`) and the job for Charges Waiver credit notes (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:3584`). The classification run of a Settled loan releases it too (`lending/loan_management/doctype/loan/loan.py:1575`), and a Loan Write Off also calls `write_off_suspense_entries` (`lending/loan_management/doctype/loan_write_off/loan_write_off.py:159`).

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J4).

- A partial collection on a loan that stays NPA releases nothing. In the test, repayments of 259.88 and 65.52 of interest left the suspense unchanged. The BRD example, where 1,151 of 3,300 goes back to income, does not happen (DEF-15).
- When a loan was cleared in full, the payment itself released nothing. The upgrade needed a second classification run, then released everything at once: 2,052.44 in one test. After the first run the loan was STD with the NPA flag still on.
- In another test 424.56 was released, but 1,045.04 stayed in suspense, because a catch-up journal was dated after the reversal date (DEF-9).
- Unticking a manual NPA left 129.36 in suspense (DEF-13).
- Restructuring an NPA loan moved 5,612.92 of interest that had only been capitalised, not collected, to income (DEF-22). That breaks the rule "restored only on actual recovery".

## What to do today

After any recovery on an NPA loan, check the suspense balance against the interest you have actually collected, and post the release by hand. Run the classification twice after a full payment.

## Planned fix

No development item is assigned. The final report proposes ND-14 and ND-15 (NPA and suspense integrity), ND-25 (clear caches, serialise classification per loan) and ND-22 (a restructure that does not release suspense).
