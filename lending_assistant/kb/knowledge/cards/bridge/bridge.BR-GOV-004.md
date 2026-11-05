---
id: bridge.BR-GOV-004
type: bridge
title: The platform's status is checked against the bank's core system every day
summary: "Not analysed. The team has not compared BR-GOV-004 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-004]
brd_section: 3.4
doctypes: [Loan, Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-004]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-004 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall maintain its own status for every application and every loan, and shall reconcile that status against CBS daily. Where the two differ, CBS is authoritative for all post-booking facts and the difference shall be raised as an exception requiring documented closure.” (BR-GOV-004, BRD 3.4, PDF page 19). See `concept.BR-GOV-004` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-004 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the document for a loan, and it holds the loan's status.
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan is in `lending/loan_management/doctype/loan/loan.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-004 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List where a status is stored for an application and for a loan in the documents above.
2. Read the scheduled jobs in `lending/hooks.py` to see which run daily and what they compare.
3. Ask NRB what the CBS exposes for a daily status comparison and who closes the exceptions.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
