---
id: bridge.BR-INT-005
type: bridge
title: Every instruction carries a unique reference the bank's record keeps
summary: "Not analysed. The team has not compared BR-INT-005 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-005]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-005"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [concept.BR-INT-005]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-005 with Frappe Lending, so there is no verdict.

## Business need

“Every instruction shall carry a platform-generated unique reference, written into a durable field of the Core Banking System record — narration, reference or equivalent — agreed with the Bank, so that the platform can later determine whether its own instruction executed.” (BR-INT-005, BRD 9.2.1, PDF page 61). See `concept.BR-INT-005` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-005 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-005 sits in section 9.2.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Ask NRB which field of the transaction record can carry the reference.
2. Ask NRB how many characters that field takes.
3. Compare that with the reference the platform would generate.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
