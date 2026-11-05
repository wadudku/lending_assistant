---
id: brd_section.6.8
type: brd_section
title: BRD 6.8 Credit bureau verification
summary: "Section 6.8 holds eight requirements for the credit bureau check, which the BRD calls the step with the highest information-security sensitivity in origination."
br_ids: [BR-LOS-190, BR-LOS-191, BR-LOS-192, BR-LOS-193, BR-LOS-194, BR-LOS-195, BR-LOS-196, BR-LOS-197]
brd_section: 6.8
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-190"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-192"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-193"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-194"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-195"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-196"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-197"
related: [bridge.BR-LOS-190, bridge.BR-LOS-191, bridge.BR-LOS-192, bridge.BR-LOS-193, bridge.BR-LOS-194, bridge.BR-LOS-195, bridge.BR-LOS-196, bridge.BR-LOS-197, brd_section.6.7.2, brd_section.6, glossary.cib, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.8 holds eight requirements for the credit bureau check, which the BRD calls the step with the highest information-security sensitivity in origination.

## What this section says

BRD 6.8 (PDF page 42) opens with a short paragraph and holds eight requirements, BR-LOS-190 to BR-LOS-197, all Must. They cover routing the inquiry and returning only pass or fail (190), keeping all bureau detail off the device (191), neutral guidance after a fail (192), central retention and a logged, restricted panel (193), versioned decision rules with maker-checker (194), holding and retrying when the bureau is unavailable (195), logging every inquiry (196) and reusing a kept response for repeat inquiries (197).

## Why the bank wants it

The BRD gives the reason on PDF page 42: "This step carries the highest information-security sensitivity in origination. Bureau data concerning an individual's borrowings at other institutions must not be exposed to a field officer standing in a village meeting, nor cached on a device that may be lost."

## How it meets Frappe Lending

The team has not analysed the LOS (the origination system, BRD section 6), so this section carries no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7. None of the eight rows is among the 103 requirements the team verified.

## Related cards

Rows: `bridge.BR-LOS-190` to `bridge.BR-LOS-197`. The offline rule for credit bureau verification is in `brd_section.6.7.2`. Parent section: `brd_section.6`.
