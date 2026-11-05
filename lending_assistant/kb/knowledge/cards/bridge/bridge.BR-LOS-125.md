---
id: bridge.BR-LOS-125
type: bridge
title: "If the bank's system is down, rows wait and retry; a timeout is never a pass"
summary: "Not analysed. The team has not compared BR-LOS-125 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-125]
brd_section: 6.3
doctypes: [RQ Job, Error Log]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-125"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-LOS-125]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-125 with Frappe Lending, so there is no verdict.

## Business need

“Where the Core Banking System is unreachable, an automation session cannot be established, or the outcome indicates unavailability rather than a business result, affected rows shall be held pending and re-attempted automatically on a configurable schedule. The partner shall see a clear message stating that validation is in progress and shall not be required to re-upload the file. A timeout shall never be recorded as a validation pass.” (BR-LOS-125, BRD 6.3, PDF page 32). See `concept.BR-LOS-125` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-125 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **RQ Job** is Frappe's list of background jobs.
- **Error Log** is Frappe's list of errors raised by the code.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-125 sits in section 6.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how a failed background job is recorded in the two items above.
2. Check whether a failed job can be tried again on a schedule.
3. Ask NRB which outcomes count as unavailability and how long between retries.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
