---
id: bridge.BR-LOS-333
type: bridge
title: Sanction activity is reported
summary: "Not analysed. The team has not compared BR-LOS-333 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-333]
brd_section: 6.6
doctypes: [Report, Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-333"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-321"
related: [concept.BR-LOS-333]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-333 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall report sanction activity: auto-sanctioned against approver-sanctioned volume, decline rate and reasons, revision rate and average reduction, approver throughput and queue ageing, and escalation volume by authority level.” (BR-LOS-333, BRD 6.6, PDF page 39). See `concept.BR-LOS-333` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-333 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Report** is Frappe's document for defining a report.
- **Loan Application** is the document Frappe Lending uses for applications.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-333 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the reports that the first item above defines for loan applications.
2. Compare the BRD's measures with the fields held on the documents above.
3. Ask NRB which measures to include at launch.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
