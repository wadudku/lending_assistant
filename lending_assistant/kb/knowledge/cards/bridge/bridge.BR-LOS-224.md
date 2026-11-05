---
id: bridge.BR-LOS-224
type: bridge
title: Partners can create and schedule four reports and export them as XLSX and CSV
summary: "Not analysed. The team has not compared BR-LOS-224 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-224]
brd_section: 6.10.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-224"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.2"
related: [concept.BR-LOS-224, concept.BR-LOS-225, concept.BR-LOS-220]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-224 with Frappe Lending, so there is no verdict.

## Business need

“Partners shall be able to generate and schedule reports covering batch summary, approval funnel, rejection reasons by category and disbursement register, exportable to XLSX and CSV.” (BR-LOS-224, BRD 6.10.2, PDF page 45). See `concept.BR-LOS-224` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-224 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Auto Email Report** is Frappe's document for reports sent on a schedule.
- **Report** is Frappe's document for saved reports.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-224 sits in section 6.10.2. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB what each of the four reports should show and how often it should run.
2. Read BR-LOS-225, which describes the partner dashboard.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
