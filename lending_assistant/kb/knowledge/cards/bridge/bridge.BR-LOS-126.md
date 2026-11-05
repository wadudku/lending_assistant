---
id: bridge.BR-LOS-126
type: bridge
title: Account checks run in the background and show progress
summary: "Not analysed. The team has not compared BR-LOS-126 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-126]
brd_section: 6.3
doctypes: [RQ Job, Notification]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-126"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
related: [concept.BR-LOS-126]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-126 with Frappe Lending, so there is no verdict.

## Business need

“Validation shall run as a queued background process. On upload the partner shall be shown the batch's validation progress, an expected completion time and a per-row state, shall be able to leave the screen and return, and shall be notified when the batch reaches a terminal validation state.” (BR-LOS-126, BRD 6.3, PDF page 32). See `concept.BR-LOS-126` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-126 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **RQ Job** is Frappe's list of background jobs.
- **Notification** is Frappe's document for rules that send alerts.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-126 sits in section 6.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the two items above show the progress of a background job.
2. Check whether a job's progress can be tied to a row or a batch.
3. Ask NRB how the partner is to be notified and through which channel.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
