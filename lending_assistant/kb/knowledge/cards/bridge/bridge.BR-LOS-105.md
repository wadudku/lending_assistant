---
id: bridge.BR-LOS-105
type: bridge
title: A partner's first-loss guarantee terms are recorded for servicing to use
summary: "Not analysed. The team has not compared BR-LOS-105 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-105]
brd_section: 6.1
doctypes: [Loan Partner]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_partner/loan_partner.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-105"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [concept.BR-LOS-105]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-105 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall record, for each partner, the first-loss default guarantee terms or other risk-sharing arrangement where one exists, and shall make those terms available to servicing for partner economics.” (BR-LOS-105, BRD 6.1, PDF page 29). See `concept.BR-LOS-105` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-105 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Partner** is the Frappe Lending document for a co-lending partner.
- The code for Loan Partner is in `lending/loan_management/doctype/loan_partner/loan_partner.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-105 sits in section 6.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the partner document above that hold sharing terms.
2. Read the partner code for any use of those terms in a later calculation.
3. Ask NRB for the guarantee terms in the partner agreement and how servicing will use them.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
