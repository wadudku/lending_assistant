---
id: bridge.BR-LMS-222
type: bridge
title: Close repaid credit lines automatically
summary: Covered. A daily job closes every active credit-line loan whose end date has passed and whose utilised limit is 0. It has no setting on the product.
br_ids: [BR-LMS-222]
brd_section: 7.13
doctypes: [Loan]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:2144-2165", "lending/hooks.py:192"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-222"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-222"
  - "sources/verification/verification_report.md#BR-LMS-222"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-222"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-222"
related: [concept.BR-LMS-222, bridge.BR-LMS-221]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A daily job closes every active credit-line loan whose end date has passed and whose utilised limit is 0. It has no setting on the product.

## Business need

Fully repaid revolving facilities must be closed by scheduled processing, subject to the product's configured behaviour (BR-LMS-222 in section 7.13, BRD PDF page 55). This is a Should requirement. See `concept.BR-LMS-222`.

## Frappe Lending today

The scheduler runs `auto_close_loc_loans` every day (`lending/hooks.py:192`). It picks the submitted **Loan** records whose status is Active, whose repayment schedule type is Line of Credit, whose limit end date is on or before the posting date and whose utilised limit is 0. It sets their status to Closed and their closure date to the posting date it was given (`lending/loan_management/doctype/loan/loan.py:2144-2165`). In the test, a credit line with a limit of 100,000 ending on 31 October 2026 was drawn for 20,000 and repaid in full. A dry run of the job's filter on 3 November matched only that loan, and calling the job closed it with the closure date set to the posting date.

## Match or gap, and why

This is **covered**, and the verification confirmed the verdict with caveats (J9).

- The job has no product-level switch. Its filter reads the loan type, the end date and the utilised limit, and no product setting. So the BRD's "subject to the product's configured behaviour" has nothing to attach to: every line-of-credit product is closed the same way.
- The job takes no loan filter. A single run acts on every matching loan on the site.
- In the test, a Normal Repayment was refused on the line, because nothing had been demanded against the drawdown, so the repayment was made as a Pre Payment.
- The job updates the loan's status and closure date directly in the database and does not touch anything else.

## What to do today

Check the list of line-of-credit loans that have passed their end date each morning, and run the closure for the ones that are due. If a product should not close automatically, extend the limit end date.

## Planned fix

No development item is assigned.
