---
id: bridge.BR-INT-020
type: bridge
title: The handoff to servicing carries the full package and is idempotent
summary: "Not analysed. The team has not compared BR-INT-020 with Frappe Lending, so there is no verdict."
br_ids: [BR-INT-020]
brd_section: 9.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-020"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [concept.BR-INT-020]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-INT-020 with Frappe Lending, so there is no verdict.

## Business need

“The handoff of a confirmed funded loan from origination to servicing shall carry the complete package specified in BR-LOS-010 and shall be idempotent.” (BR-INT-020, BRD 9.4, PDF page 64). See `concept.BR-INT-020` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-INT-020 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- BR-LMS-100 (`bridge.BR-LMS-100`) is a related servicing requirement the team analysed, about accepting only loans that are really paid out. Its result does not apply to BR-INT-020.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-INT-020 sits in section 9.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BR-LOS-010 in the BRD for the list of items in the package.
2. Ask NRB how the handoff is to be sent.
3. List the data Frappe Lending needs to create a loan.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
