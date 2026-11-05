---
id: journey.J2
type: journey
title: "Journey J2: set up or change a loan product"
summary: "A product owner picks the repayment method, rate, fees and payment order, accounting mode and partners; the BRD wants every change approved, dated and versioned, which Frappe Lending 16.5.1 does not do."
br_ids: []
brd_section: 7.2
doctypes: [Loan Product, Loan Demand Offset Order, Loan Partner]
dev_items: [D4, D5, D13]
journeys: [J2]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-6"
  - "sources/verification/reqs.json#BR-LMS-110"
  - "sources/verification/reqs.json#BR-LMS-117"
related: [howto.loan_product.duplicate, howto.loan_product.set_repayment_method, howto.loan_product.set_rates, howto.item.create_fee, howto.loan_product.add_charge, howto.loan_demand_offset_order.create, howto.company.view_loan_settings, howto.loan_partner.create, howto.loan_product.change_penalty_rate, screen.loan_product, screen.loan_partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** A product owner picks the repayment method, rate, fees and payment order, accounting mode and partners; the BRD wants every change approved, dated and versioned, which Frappe Lending 16.5.1 does not do.

## The process in plain words

A new product launches, or a rule such as the rate, the penalty or a grade band must change. The goal in the BRD is that product rules change only with approval and a start date, and that every loan knows which version applied. The product owner (the maker) sets the rules, and a second person (the checker) approves them. With one test user and no workflow, the checker step is shown as a gap. The walkthrough worked on a product copy.

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Choose repayment method | Product owner | Pick the repayment method and set the moratorium rule | Loan Product, copied first; the moratorium is keyed on the Loan, not the product. `howto.loan_product.duplicate`, `howto.loan_product.set_repayment_method` | BR-LMS-110, 112 |
| 2 Set the rate | Product owner | Store the rate, and fixed or floating with benchmark | Loan Product: one yearly rate and a penalty rate. `howto.loan_product.set_rates` | BR-LMS-111 |
| 3 Fees and payment order | Product owner | Define each fee and its accounts; set which debt a payment clears first | Loan Product, Charges table; Loan Demand Offset Order, set on the Company and overridable on the product. `howto.item.create_fee`, `howto.loan_product.add_charge`, `howto.loan_demand_offset_order.create` | BR-LMS-113, 114 |
| 4 Accounting and partners | Finance | Choose the platform ledger or the CBS-owned ledger; link co-lending partners | Company loan settings; Loan Partner and the product's Co Lending tab. `howto.company.view_loan_settings`, `howto.loan_partner.create` | BR-LMS-115, 116 |
| 5 Approve and version | Checker | Second person approves; the change gets a version and effective date | None today; the Version log is the only trace. `howto.loan_product.change_penalty_rate` | BR-LMS-117, 197 |

Stage 6 of the walkthrough is the end state: a Draft loan on the new product.

## Gaps met on the way

- Stage 1: the moratorium has no product setting, so loans of the same product can differ (BR-LMS-112, ND-2).
- Stage 2: one fixed rate; no fixed or floating choice, benchmark or repricing (BR-LMS-111, D4).
- Stage 3: the fee row on the product is not applied to loans (BR-LMS-113, ND-1), and an order with an Interest row skips interest (DEF-3).
- Stage 4: only the platform-ledger mode exists; no CBS posting option (BR-LMS-115, D13).
- Stage 5: a product change saves at once with no checker, version or effective date (BR-LMS-117, D5), and the same holds for grade and provision rules (BR-LMS-197).
- Journey map, as the verification report corrects it: the offset order is not stored on the loan; it is read from the product, then the Company, at each repayment.

## Outcome

A product copy is ready with its rate, penalty rate, a fee row, its own payment order and a linked partner, and a Draft loan on it shows the rate and accounts from the product. The journey's verified requirement results are: covered for 110 and 116; partly covered for 111, 112, 113, 114 and 115; gap for 117 and 197.
