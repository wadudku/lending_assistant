---
id: bridge.BR-LOS-137
type: bridge
title: Some applications are always reviewed under seven mandatory rules
summary: "Not analysed. The team has not compared BR-LOS-137 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-137]
brd_section: 6.5
doctypes: [Loan Application]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-137"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-116"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-309"
related: [concept.BR-LOS-137]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-137 with Frappe Lending, so there is no verdict.

## Business need

“In addition to the random rate, the platform shall support rule-based mandatory sampling, configurable by Credit Risk, covering at minimum: applications above a configurable amount threshold; applications from a partner within its first configurable number of batches; applications flagged as cross-partner duplicates; applications the scorecard referred or that fall in a configured risk grade band; applications where a score override has been requested; applications from a partner whose recent sample rejection rate exceeds a configured threshold; and a configurable proportion of applications from any newly added district or upazila.” (BR-LOS-137, BRD 6.5, PDF page 36). See `concept.BR-LOS-137` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-137 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Application** is the document Frappe Lending uses for applications.
- The code for Loan Application is in `lending/loan_management/doctype/loan_application/loan_application.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-137 sits in section 6.5. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the fields on the application document above that each of the seven rules would read.
2. Check which of the rules need a field that is not on the document.
3. Ask NRB for the thresholds and counts in the rules.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
