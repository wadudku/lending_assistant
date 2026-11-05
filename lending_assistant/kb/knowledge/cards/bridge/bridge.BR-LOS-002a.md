---
id: bridge.BR-LOS-002a
type: bridge
title: "Only the origination system sanctions, never the servicing system"
summary: "Not analysed. The team has not compared BR-LOS-002a with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-002a]
brd_section: 5.2
doctypes: [Loan Application, Loan]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-002a"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
related: [concept.BR-LOS-002a]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-002a with Frappe Lending, so there is no verdict.

## Business need

“Sanction shall never be set by the servicing system. The LOS is the sanctioning authority, acting either as a system decision within configured thresholds or through a credit approver within delegated authority, as specified in Section 6.6.” (BR-LOS-002a, BRD 5.2, PDF page 27). See `concept.BR-LOS-002a` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LOS-002a in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- **Loan** is the document for a loan.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-002a sits in section 5.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List where an amount or limit is set on a loan after it is booked.
2. Read the code for any step that changes the sanctioned amount.
3. Ask NRB which changes after booking are treated as a new sanction.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
