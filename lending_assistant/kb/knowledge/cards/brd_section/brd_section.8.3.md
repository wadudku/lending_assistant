---
id: brd_section.8.3
type: brd_section
title: BRD 8.3 Bangladesh Bank regulatory obligations
summary: "Section 8.3 asks for the extracts and returns the bank files with Bangladesh Bank, their retention, and dated versioning of regulatory rules."
br_ids: []
brd_section: 8.3
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#8.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-250"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-250"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-251"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-252"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-040"
related: [brd_section.8, brd_section.7, glossary.bb, glossary.asset-classification, glossary.provisioning]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 8.3 asks for the extracts and returns the bank files with Bangladesh Bank, their retention, and dated versioning of regulatory rules.

## What this section says

BRD 8.3 (PDF page 58) has 5 requirements, all Must. BR-LOS-250: the data extracts for Bangladesh Bank agricultural and rural credit reporting, in formats the bank supplies. BR-LMS-250: the monthly CIB contribution extract, in a format the bank supplies. BR-LMS-251: classification and provisioning returns on the basis Bangladesh Bank prescribes, produced from the same records as the bank's internal position. BR-LMS-252: every generated regulatory extract kept with its parameters and generating user for the full retention period, so a return can be reproduced exactly. BR-GOV-040: a regulatory rule change made as a versioned, effective-dated configuration change, with prior-period returns keeping the old rules. A boxed note under the table, headed “Regulatory interpretation rests with the Bank”, is quoted in the next part.

## Why the bank wants it

The BRD doesn't say why. Its boxed note, headed “Regulatory interpretation rests with the Bank”, reads: “Polygon implements to NRB Bank Limited's stated compliance requirements. The supplier does not determine regulatory obligations. The Bank is asked to supply the authoritative rule set, the required return formats and the submission calendar before configuration is baselined.” (PDF page 58).

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section holds 5 requirement rows and none was analysed, so the team makes no statement about them. BR-LMS-250 to BR-LMS-252 carry the LMS prefix but sit in Section 8.3, outside the 103 requirements of Section 7. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.8`. Terms: `glossary.bb`, `glossary.asset-classification`, `glossary.provisioning`.
