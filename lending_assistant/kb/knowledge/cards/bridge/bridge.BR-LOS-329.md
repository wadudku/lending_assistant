---
id: bridge.BR-LOS-329
type: bridge
title: Cases awaiting approval age visibly and escalate on their own
summary: "Not analysed. The team has not compared BR-LOS-329 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-329]
brd_section: 6.6
doctypes: [Notification, Report]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-329"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-322"
related: [concept.BR-LOS-329]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-329 with Frappe Lending, so there is no verdict.

## Business need

“Applications awaiting credit approval shall age visibly, shall escalate automatically after a configurable period, and shall be reported with their ageing so that a queue does not silently delay a scheduled meeting event.” (BR-LOS-329, BRD 6.6, PDF page 38). See `concept.BR-LOS-329` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-329 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Notification** is Frappe's document for rules that send alerts.
- **Report** is Frappe's document for defining a report.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-329 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List what the two items above can do on a date or a period passing.
2. Check whether the application documents show how long they have been in a status.
3. Ask NRB for the waiting period before escalation.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
