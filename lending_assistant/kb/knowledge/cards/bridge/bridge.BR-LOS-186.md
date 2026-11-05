---
id: bridge.BR-LOS-186
type: bridge
title: Officer performance is reported on five measures
summary: "Not analysed. The team has not compared BR-LOS-186 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-186]
brd_section: 6.7.4
doctypes: [Report]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-186"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.4"
related: [concept.BR-LOS-186, concept.BR-LOS-162]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-186 with Frappe Lending, so there is no verdict.

## Business need

“Officer performance shall be reported: verifications completed, average elapsed time per verification, abandonment rate, bureau pass rate and disbursement conversion.” (BR-LOS-186, BRD 6.7.4, PDF page 42). See `concept.BR-LOS-186` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-186 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Report** is Frappe's document for saved reports.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-186 sits in section 6.7.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB who reads the officer performance report and how often, since the BRD gives no schedule.
2. Ask NRB how disbursement conversion is counted, for example per verification or per applicant.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
