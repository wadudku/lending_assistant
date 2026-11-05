---
id: howto.data_import.migrate_loan
type: howto
title: How to bring an old loan over with Data Import
summary: "A migrated loan is a normal Loan with Is Imported, Migration Date and an opening balance row, loaded through Data Import. It needs Administrator today."
br_ids: []
brd_section: 7.1
doctypes: [Data Import, Loan, Loan Import Details]
dev_items: [D3]
journeys: [J1]
actions: ["Loan:import"]
fields: [Data Import.Document Type, Data Import.Import Type, Data Import.Submit After Import, Loan.Is Imported, Loan.Migration Date, Loan Import Details.Opening Principal Outstanding, Loan Import Details.Opening Interest Outstanding]
options: [Data Import.Import Type=Insert New Records]
menus: [Data > Data Import]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S5-02_test-user-no-import-permission.png, /assets/lending_assistant/kb_img/J1/J1-S5-03_is-imported-read-only.png, /assets/lending_assistant/kb_img/J1/J1-S5-04_admin-data-import-filled.png, /assets/lending_assistant/kb_img/J1/J1-S5-05_admin-download-template.png, /assets/lending_assistant/kb_img/J1/J1-S5-06_admin-file-attached-preview.png, /assets/lending_assistant/kb_img/J1/J1-S5-08_admin-import-log-success.png, /assets/lending_assistant/kb_img/J1/J1-S5-09_migrated-loan-is-imported.png, /assets/lending_assistant/kb_img/J1/J1-S5-10_migrated-loan-import-details.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.4"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.6"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.5"
  - "sources/verification/FINAL_REPORT.md#D3"
related: [howto.customer.create, howto.loan_demand.view, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** A migrated loan is a normal Loan with Is Imported, Migration Date and an opening balance row, loaded through Data Import. It needs Administrator today.

## Before you start

⚠ In 16.5.1 no role has the Import permission on **Loan**. A Loan Manager who tries gets "You do not have import permission for Loan", and **Is Imported** and **Migration Date** are read-only on the Loan form. The walkthrough ran the import as Administrator. Create the borrower first (`howto.customer.create`). Names you see in the screenshots, such as customer and loan names, are test records on the dev site.

![Import permission refused for a Loan Manager](/assets/lending_assistant/kb_img/J1/J1-S5-02_test-user-no-import-permission.png)

![Is Imported is read-only on the Loan form](/assets/lending_assistant/kb_img/J1/J1-S5-03_is-imported-read-only.png)

## Steps

1. Open **Data > Data Import** and click **+ Add Data Import**.
2. Set **Document Type** to **Loan**, **Import Type** to **Insert New Records**, and tick **Submit After Import**. Click **Save**.
3. Click **Download Template**, choose CSV and **Blank Template**, click **Unselect All**, then tick the Loan fields (Applicant Type, Applicant, Company, Posting Date, Is Imported, Migration Date, Loan Product, Loan Amount, Rate of Interest, Repayment Method, Tenure, Repayment Frequency, Repayment Start Date, Cost Center) and, under Loan Import Details, Loan Disbursement ID, Disbursement Date, Disbursed Amount, Opening Principal Outstanding and Opening Interest Outstanding. Click **Export**.
4. Fill one row per old loan, with dates as dd-mm-yyyy and Opening Principal Outstanding no larger than the disbursed amount.
5. Attach the file under **Import File** and check the preview.
6. Click **Start Import**.

![Data Import form filled](/assets/lending_assistant/kb_img/J1/J1-S5-04_admin-data-import-filled.png)

![Download Template field choice](/assets/lending_assistant/kb_img/J1/J1-S5-05_admin-download-template.png)

![File attached with preview](/assets/lending_assistant/kb_img/J1/J1-S5-06_admin-file-attached-preview.png)

## What you should see

The status becomes **Success** and the log reads "Successfully imported 1 out of 1 records". The new Loan is Disbursed with **Is Imported** ticked, a **Migration Date** and a **Loan Import Details** tab. The import also creates a disbursement named after the old system's ID and an active schedule in which rows before the migration date are marked as already billed.

![Import log showing Success](/assets/lending_assistant/kb_img/J1/J1-S5-08_admin-import-log-success.png)

![Migrated loan with Is Imported and Migration Date](/assets/lending_assistant/kb_img/J1/J1-S5-09_migrated-loan-is-imported.png)

![Loan Import Details tab](/assets/lending_assistant/kb_img/J1/J1-S5-10_migrated-loan-import-details.png)

## If it looks wrong

⚠ Missing control (BR-LMS-105 is partly covered; ND-4, D3): Data Import has no control totals and no sign-off, and posts at once. An opening principal larger than the loan is accepted with no warning, and nothing compares the figure you typed with the balance the schedule itself implies. Workaround: reconcile the count and totals from the old system's extract against a Loan and Loan Demand (bill) report after a trial load, and record sign-off outside the system. The final report also found that migration cannot go live on the standard code (DEF-6). See `howto.loan_demand.view` for what the import bills.
