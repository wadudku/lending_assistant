---
id: bridge.BR-GOV-006
type: bridge
title: Every outside system sits behind a replaceable adapter
summary: "Not analysed. The team has not compared BR-GOV-006 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-006]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-006]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-006 with Frappe Lending, so there is no verdict.

## Business need

“Every integration shall be implemented behind an adapter, such that replacing a counterparty system requires a new adapter and no change to the origination or servicing engine.” (BR-GOV-006, BRD 3.4, PDF page 19). See `concept.BR-GOV-006` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-006 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-006 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List every outside system the BRD names in section 8 and the code that would talk to each.
2. Read `lending/hooks.py` for places where another app's behaviour is hooked in.
3. Ask NRB which counterparty systems may be replaced, so the adapter boundary can be drawn.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
