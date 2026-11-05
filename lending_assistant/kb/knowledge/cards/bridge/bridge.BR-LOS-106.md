---
id: bridge.BR-LOS-106
type: bridge
title: Partner performance is visible on one partner record
summary: "Not analysed. The team has not compared BR-LOS-106 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-106]
brd_section: 6.1
doctypes: [Loan Partner]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-106"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [concept.BR-LOS-106]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-106 with Frappe Lending, so there is no verdict.

## Business need

“Partner performance — submission volume, validation failure rate, sampling rejection rate, disbursement conversion and, where available from servicing, arrears performance — shall be visible to the Bank on a single partner record.” (BR-LOS-106, BRD 6.1, PDF page 29). See `concept.BR-LOS-106` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-106 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Partner** is the Frappe Lending document for a co-lending partner.
- The file `loan_partner_dashboard.py` in the same folder lists the Loans linked to a partner on its form.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-106 sits in section 6.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Open the partner document above and list what it shows about a partner's loans.
2. Compare that list with the five measures in the BRD.
3. Ask NRB where each measure comes from, since two depend on the LOS.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
