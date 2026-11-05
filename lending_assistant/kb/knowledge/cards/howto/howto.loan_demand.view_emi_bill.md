---
id: howto.loan_demand.view_emi_bill
type: howto
title: How to see the EMI bill and check what it leaves out
summary: "The EMI bill is two demands, interest and principal, with the due date and amount; instalment charges are not added to it and there is no CBS journal reference on it."
br_ids: [BR-LMS-130, BR-LMS-131, BR-LMS-134]
brd_section: 7.4
doctypes: [Loan Demand]
dev_items: [D13]
journeys: [J3, J4]
actions: ["Loan Demand:view_emi_bill"]
fields: [Loan Demand.Demand Type, Loan Demand.Demand Subtype, Loan Demand.Demand Amount, Loan Demand.Outstanding Amount, Loan Demand.Demand Date]
options: [Loan Demand.Demand Type=EMI]
menus: [Lending > Loan Management > Loan Demand]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S2-03_demand-list.png, /assets/lending_assistant/kb_img/J3/J3-S2-04_demand-emi-interest.png, /assets/lending_assistant/kb_img/J3/J3-S2-05_demand-emi-principal.png, /assets/lending_assistant/kb_img/J3/J3-S2-06_gap-no-cbs-journal-ref.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.3"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.4"
related: [howto.process_loan_demand.run, howto.loan_demand.view, bridge.BR-LMS-130, bridge.BR-LMS-131, bridge.BR-LMS-134, journey.J3, screen.loan_demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** The EMI bill is two demands, interest and principal, with the due date and amount; instalment charges are not added to it and there is no CBS journal reference on it.

## Before you start

⚠ This card is view only. You need read permission on **Loan Demand**. The bill exists only after the demand run (`howto.process_loan_demand.run`). Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Loan Management > Loan Demand and filter the list by loan.
2. Look at the rows with **Demand Type** EMI and the **Demand Date** of the due date.
3. Open each row to read **Demand Amount** and **Outstanding Amount**.
4. Open the **References** section of a demand.

![The demand list for the due date](/assets/lending_assistant/kb_img/J3/J3-S2-03_demand-list.png)

## What you should see

Two Submitted demands, one with **Demand Subtype** Interest and one with Principal. In the walkthrough's e.g. Rahim's 100,000 loan the first EMI of 8,979 split into 1,150.68 interest and 7,828.32 principal, both fully outstanding before payment. The interest demand is posted as a debit to Interest Receivable and a credit to Interest Accrued.

![The interest demand](/assets/lending_assistant/kb_img/J3/J3-S2-04_demand-emi-interest.png)

![The principal demand](/assets/lending_assistant/kb_img/J3/J3-S2-05_demand-emi-principal.png)

## If it looks wrong

Charges: The BRD wants fees attached to a loan to be billed with their instalment (BR-LMS-131, partly covered). Only fees billed separately work, as a Sales Invoice that becomes a charges demand. A disbursement charge set to be added to the first repayment is put into the schedule row but never billed as a demand (ND-11, DEF-4). The workaround in the verification is to raise the fee as a Sales Invoice linked to the loan. See `bridge.BR-LMS-131`.

CBS reference: The References section holds only internal links (Loan, Loan Product, Loan Repayment Schedule, Loan Disbursement, Sales Invoice). The BRD wants each bill sent to the CBS and its journal reference kept (BR-LMS-134, gap needing the CBS link); the verification names D13 for the posting adapter. See `bridge.BR-LMS-134`.

![Demand references: internal only](/assets/lending_assistant/kb_img/J3/J3-S2-06_gap-no-cbs-journal-ref.png)
