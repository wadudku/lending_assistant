---
id: bridge.BR-LMS-170c
type: bridge
title: A master list of collateral
summary: "Partly covered. Frappe Lending keeps security types, securities and dated prices with a haircut, but a nested price row is accepted and the per-security value fields stay empty. The original analysis said covered."
br_ids: [BR-LMS-170]
brd_section: 7.8
doctypes: [Loan Security Type, Loan Security, Loan Security Price, Loan Security Assignment]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Security Type.Haircut %, Loan Security Type.Loan To Value Ratio, Loan Security Price.Valid From, Loan Security Price.Valid Upto]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_security_price/loan_security_price.py:64-79"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-170c"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-170c"
  - "sources/verification/verification_report.md#BR-LMS-170c"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-170"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-170"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-170c, bridge.BR-LMS-170r, glossary.ltv]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Frappe Lending keeps security types, securities and dated prices with a haircut, but a nested price row is accepted and the per-security value fields stay empty. The original analysis said covered.

## Business need

The platform must keep a security master with type, description, valuation, price history, haircut and eligible value (BR-LMS-170 in section 7.8, BRD PDF page 52). See `concept.BR-LMS-170c`. This is the collateral row. The same number in 7.7 is a different rule with its own cards (`bridge.BR-LMS-170r`).

## Frappe Lending today

Three records make up the master. A **Loan Security Type** holds the Haircut % and the Loan To Value Ratio. A **Loan Security** belongs to a type and inherits both. A **Loan Security Price** gives a price with Valid From and Valid Upto, so there is a price history. A pledge row on the **Loan Security Assignment** takes the price valid now and shows the amount and the amount after the haircut. In the test, a type with haircut 20 and loan-to-value 70 gave 200,000 and 160,000 for 200 units priced at 1,000. It refused a pledge with no valid price, a security twice in one pledge, a quantity of 0, and a price row starting inside another and ending after it.

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J7) for these reasons:

- A price row nested inside an existing one is accepted. In the test a row of 600 inside a row of 1,000 was saved; a pledge then used 600 while the shortfall check used 1,000 (DEF-29). The overlap query only looks for an existing row that starts or ends inside the new range (`lending/loan_management/doctype/loan_security_price/loan_security_price.py:64-79`). The whitelisted bulk price call writes prices and dates straight to the database and skips this check (`lending/api.py:67-72`).
- In the test, a type with haircut 150 and loan-to-value 250 was saved (then rolled back). The form has no 0 to 100 check.
- In the test the three per-security value fields stayed 0 after a pledge and a disbursement. Original Security Value is a field entered by hand on the **Loan Security** (`lending/loan_management/doctype/loan_security/loan_security.json:78-82`); the app code never writes it. Only once it is entered are the other two kept up to date by pledges and repayments (`lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.py:181-245`). The available value is computed from it (`lending/loan_management/doctype/loan_security/loan_security.py:38`).
- Haircut and loan-to-value are separate (CF-3): the haircut limits the loan value, the loan-to-value drives shortfall and releases.

## What to do today

Keep the price history by hand and never add a price row inside another one. Check every haircut and loan-to-value entry is between 0 and 100. Enter the Original Security Value on each Loan Security if the per-security values are wanted; otherwise do not rely on the three fields.

## Planned fix

No development item is assigned in the verified list. The final report proposes ND-29, sized small: a range-overlap test, one price lookup and 0 to 100 limits.
