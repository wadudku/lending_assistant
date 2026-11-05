---
id: brd_section.6.3
type: brd_section
title: BRD 6.3 Pre-submission account validation
summary: "Section 6.3 holds eight rules for checking the borrower's bank account before submission and again before payout, run as a queued background process."
br_ids: [BR-LOS-120, BR-LOS-121, BR-LOS-122, BR-LOS-123, BR-LOS-126, BR-LOS-127, BR-LOS-124, BR-LOS-125]
brd_section: 6.3
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p33"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-121"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-122"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-123"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-126"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-127"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-124"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-125"
related: [bridge.BR-LOS-120, bridge.BR-LOS-121, bridge.BR-LOS-122, bridge.BR-LOS-123, bridge.BR-LOS-126, bridge.BR-LOS-127, bridge.BR-LOS-124, bridge.BR-LOS-125]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.3 holds eight rules for checking the borrower's bank account before submission and again before payout, run as a queued background process.

## What this section says

BRD 6.3 (PDF pages 32 and 33) calls pre-submission account validation the single most important control in the Partner Portal. Because the Core Banking System has no programmatic interface, the check is done by robotic process automation driving the CBS enquiry screens (Section 9.2), which makes it a queued background process. It holds eight requirements, BR-LOS-120 to BR-LOS-127: the account is checked for existence, active status, permitted type, a title that agrees with the applicant and current KYC (120); names are normalised before comparison (121); one account number holds one open application platform-wide (122); a result expires after a set time, seven days by default (123); validation runs in the background and shows progress (126); requests are queued and paced to what the CBS and the automation can take (127); the account is checked again just before payout (124); and if the CBS is unreachable, rows wait and retry, and a timeout is never recorded as a pass (125). The BRD order is 120 to 123, 126, 127, 124, 125.

## Why the bank wants it

The BRD gives the reason in the section introduction: the purpose is to guarantee that a disbursement instruction issued weeks later lands in a live, correctly titled, eligible account belonging to the named applicant, because a failure here shows up as a failed or misdirected payout at the point of greatest cost (PDF page 32).

## How it meets Frappe Lending

The section holds 8 requirements (BR-LOS-120 to BR-LOS-127). The team has not analysed them: the analysis covered the 103 servicing requirements of BRD section 7, so this card gives no verdict. Each row has a concept card with the rule and a not-analysed bridge card with pointers only.

## Related cards

Requirement cards: `concept.BR-LOS-120` to `concept.BR-LOS-127` with matching bridge cards. Section: `brd_section.6.3.1`. Terms: `glossary.cbs`, `glossary.rpa`.
