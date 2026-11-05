---
id: bridge.BR-GOV-012
type: bridge
title: "One vocabulary across every screen, report and extract"
summary: "Not analysed. The team has not compared BR-GOV-012 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-012]
brd_section: 3.4
doctypes: [Loan]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.json]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-012"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p20"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p20"
related: [concept.BR-GOV-012]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-012 with Frappe Lending, so there is no verdict.

## Business need

“Terminology shall be identical across every user interface, every report and every extract. Where the Bank's existing systems use different terminology for an equivalent state, the Bank's terminology shall be adopted so that one vocabulary describes one loan.” (BR-GOV-012, BRD 3.4, PDF page 20). See `concept.BR-GOV-012` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-012 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan** is the document for a loan, and it holds the loan's status.
- The status options of Loan are in `lending/loan_management/doctype/loan/loan.json`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-012 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the status words shown on the loan document and in its reports.
2. Compare them with the status names in BRD section 5.3 and with NRB's own words.
3. Ask NRB for its list of terms to adopt.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
