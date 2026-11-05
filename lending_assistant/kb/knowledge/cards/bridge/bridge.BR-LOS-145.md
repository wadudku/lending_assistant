---
id: bridge.BR-LOS-145
type: bridge
title: Sampling outcomes feed partner quality figures and can raise a partner's rate
summary: "Not analysed. The team has not compared BR-LOS-145 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-145]
brd_section: 6.5.1
doctypes: [Notification, Report]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-145"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-137"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-106"
related: [concept.BR-LOS-145]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-145 with Frappe Lending, so there is no verdict.

## Business need

“Sampling outcomes shall roll up into partner quality metrics: sample rejection rate overall and by reason code, trend over time, and comparison across partners. Where a partner's rejection rate breaches a configurable threshold the platform shall alert the Bank and, subject to configuration, shall escalate that partner's sampling rate automatically.” (BR-LOS-145, BRD 6.5.1, PDF page 37). See `concept.BR-LOS-145` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-145 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Notification** is Frappe's document for rules that send alerts.
- **Report** is Frappe's document for defining a report.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-145 sits in section 6.5.1. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List what the two items above can send or show about the records of one partner.
2. Check whether a threshold on a figure can trigger a message.
3. Ask NRB for the rejection-rate threshold and whether the automatic increase is wanted.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
