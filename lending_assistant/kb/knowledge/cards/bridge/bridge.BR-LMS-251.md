---
id: bridge.BR-LMS-251
type: bridge
title: Classification and provisioning returns for Bangladesh Bank
summary: "Not analysed. The team has not compared BR-LMS-251 with Frappe Lending, so there is no verdict."
br_ids: [BR-LMS-251]
brd_section: 8.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-251"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [concept.BR-LMS-251]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LMS-251 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall support classification and provisioning returns on the basis prescribed by Bangladesh Bank, produced from the same underlying records that drive the Bank's internal position.” (BR-LMS-251, BRD 8.3, PDF page 58). See `concept.BR-LMS-251` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-LMS-251 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-251 carries the LMS prefix but sits in BRD section 8.3, outside the 103 requirements of section 7, so it was not analysed.
- **Loan Classification Range** is the Frappe Lending document for classification ranges.
- **Loan IRAC Provisioning Configuration** is the Frappe Lending document for IRAC provisioning configuration.
- BR-LMS-188 (`bridge.BR-LMS-188`) is a related servicing requirement the team analysed, about reporting restructures and waivers to Bangladesh Bank. Its result does not apply to BR-LMS-251.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LMS-251 sits in section 8.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB for the layout and calendar of the classification and provisioning returns.
2. Read the two documents named above and list the settings each holds.
3. Compare those settings with the basis the return prescribes.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
