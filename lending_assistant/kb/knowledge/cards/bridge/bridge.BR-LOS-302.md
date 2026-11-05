---
id: bridge.BR-LOS-302
type: bridge
title: Credit Risk owns the scorecard and changes it without a software release
summary: "Not analysed. The team has not compared BR-LOS-302 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-302]
brd_section: 6.4
doctypes: [Version, Authorization Rule]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-302"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
related: [concept.BR-LOS-302]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-302 with Frappe Lending, so there is no verdict.

## Business need

“Scorecards shall be configuration owned by Credit Risk. Attributes, bands, weights, exclusions and cut-offs shall be maintainable without a software release, and every change shall be versioned, effective-dated and subject to maker-checker with a stated justification.” (BR-LOS-302, BRD 6.4, PDF page 34). See `concept.BR-LOS-302` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-302 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Version** is Frappe's record of changes made to a document.
- **Authorization Rule** is ERPNext's document for approval limits; its list of documents holds sales and purchase documents only, such as Sales Order and Purchase Invoice.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-302 sits in section 6.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List how the two items above record who changed a setting and when.
2. Check whether a change can start on a future date.
3. Ask NRB who in Credit Risk makes and who approves a scorecard change.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
