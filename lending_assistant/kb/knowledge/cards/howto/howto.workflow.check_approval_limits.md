---
id: howto.workflow.check_approval_limits
type: howto
title: How to check what approval limits exist for settlements and write-offs
summary: "There is no workflow, authorization rule or approver field on Loan Repayment, Loan Write Off or Loan Balance Adjustment; the same user makes, submits and cancels each record."
br_ids: [BR-LMS-201, BR-LMS-205]
brd_section: 7.11
doctypes: [Workflow, Authorization Rule, Loan Repayment, Loan Write Off, Loan Balance Adjustment, Loan Product]
dev_items: [D8]
journeys: [J8]
actions: ["Workflow:check_limits"]
fields: [Loan Repayment.Reference Number, Loan Repayment.Reference Date, Loan Repayment.Manual Remarks, Loan Write Off.Is Settlement Write Off, Loan Product.Auto Write Off Amount, Loan Product.Excess Amount Acceptance Limit]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J8/J8-S2-1a_no-workflow-loan-repayment.png, /assets/lending_assistant/kb_img/J8/J8-S2-1b_no-workflow-loan-write-off.png, /assets/lending_assistant/kb_img/J8/J8-S2-1d_no-authorization-rule.png, /assets/lending_assistant/kb_img/J8/J8-S2-2a_gap-loan-write-off-no-approver-fields.png, /assets/lending_assistant/kb_img/J8/J8-S2-2b_loan-repayment-reference-and-remarks.png]
sources:
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-2"
related: [howto.loan_write_off.create, howto.loan_repayment.settle, bridge.BR-LMS-201, bridge.BR-LMS-205, journey.J8, screen.loan_repayment, screen.loan_write_off, screen.loan_product]
version: 1
status: approved
approved_by: Owner
---
**In short:** There is no workflow, authorization rule or approver field on Loan Repayment, Loan Write Off or Loan Balance Adjustment; the same user makes, submits and cancels each record.

## Before you start

⚠ This is a read-only check; you need permission to read **Workflow** and **Authorization Rule** records. Type each name in the search bar, because they are not in the Lending menu. Names in the screenshots are test records on the dev site.

## Steps

1. Type Workflow in the search bar, open the list and filter on Document Type for Loan Repayment, Loan Write Off and Loan Balance Adjustment.
2. Type Authorization Rule in the search bar and open the list.
3. Open a **Loan Write Off** and look for an approver, an approval date or a reason field.
4. Open a **Loan Repayment** and look at **Reference Number**, **Reference Date** and **Manual Remarks**.

![No workflow for Loan Repayment](/assets/lending_assistant/kb_img/J8/J8-S2-1a_no-workflow-loan-repayment.png)

![No workflow for Loan Write Off](/assets/lending_assistant/kb_img/J8/J8-S2-1b_no-workflow-loan-write-off.png)

## What you should see

Each Workflow search finds nothing for these three doctypes, and the Authorization Rule list is empty.

![No authorization rule](/assets/lending_assistant/kb_img/J8/J8-S2-1d_no-authorization-rule.png)

The only amounts in the product are **Auto Write Off Amount** (a shortfall tolerance) and **Excess Amount Acceptance Limit**. A Loan Repayment keeps a reference number, a reference date and free-text **Manual Remarks**. A Loan Write Off has no such field; its only extra field is **Is Settlement Write Off**.

![Loan Write Off with no approver field](/assets/lending_assistant/kb_img/J8/J8-S2-2a_gap-loan-write-off-no-approver-fields.png)

![Loan Repayment reference and remarks](/assets/lending_assistant/kb_img/J8/J8-S2-2b_loan-repayment-reference-and-remarks.png)

## If it looks wrong

The BRD wants approval limits by role and amount (BR-LMS-201, partly covered) and a full record of who, when and why (BR-LMS-205, partly covered). Neither exists here, and the waivers and write-off that a settlement creates have no link back to the settlement repayment. The workaround is to type the reason in **Manual Remarks** and keep the offer letter outside the system. A workflow on Loan Repayment would also apply to repayments the system creates itself, so its conditions must exempt them; that was read from code, not tested. The fix is ND-32 and ND-34. See `bridge.BR-LMS-201`.
