---
id: bridge.BR-LOS-232
type: bridge
title: "All configuration is versioned and dated, with a change history"
summary: "Not analysed. The team has not compared BR-LOS-232 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-232]
brd_section: 6.11
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-232"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.11"
related: [concept.BR-LOS-232, concept.BR-LOS-233, glossary.maker-checker, glossary.effective-date]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-232 with Frappe Lending, so there is no verdict.

## Business need

“All configuration shall be versioned and effective-dated, with a change history showing before value, after value, maker, checker, timestamp and justification.” (BR-LOS-232, BRD 6.11, PDF page 45). See `concept.BR-LOS-232` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-232 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's document for the history of changes to other documents.
- The team analysed a related servicing requirement, BR-LMS-117 (product rules have versions, start dates and approval). That is not a comparison with BR-LOS-232.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-232 sits in section 6.11. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which settings count as "all configuration".
2. Read BR-LOS-194, which asks for versioned decision rules with maker-checker.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
