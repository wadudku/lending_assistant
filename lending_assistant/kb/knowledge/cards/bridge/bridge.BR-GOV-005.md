---
id: bridge.BR-GOV-005
type: bridge
title: "Product behaviour is set by configuration, not code"
summary: "Not analysed. The team has not compared BR-GOV-005 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-005]
brd_section: 3.4
doctypes: [Loan Product]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_product/loan_product.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-005"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-005]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-005 with Frappe Lending, so there is no verdict.

## Business need

“Product behaviour — ceilings, tenors, rates, eligibility rules, required fields, sampling rates, decision rules, offset sequences, classification bands and provisioning percentages — shall be configuration, not code.” (BR-GOV-005, BRD 3.4, PDF page 19). See `concept.BR-GOV-005` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-005 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Product** is the document that holds the settings of a loan product.
- The code for Loan Product is in `lending/loan_management/doctype/loan_product/loan_product.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-005 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List each item named in the rule, from ceilings to provisioning percentages.
2. Open the product document above and find where each item is set, or note that it is not there.
3. Read the code for any place an item is fixed in the program instead of a setting.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
