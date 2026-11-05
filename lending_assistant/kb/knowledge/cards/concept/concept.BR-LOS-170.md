---
id: concept.BR-LOS-170
type: concept
title: An officer starts a verification from the list or by manual lookup
summary: "An officer starts a verification by picking an assigned applicant or, for someone not on the list, by entering an account number and a mobile number."
br_ids: [BR-LOS-170]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-170"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [bridge.BR-LOS-170]
version: 1
status: approved
approved_by: Owner
---
**In short:** An officer starts a verification by picking an assigned applicant or, for someone not on the list, by entering an account number and a mobile number.

## What the rule says

BR-LOS-170 (Must, BRD 6.7.3, PDF page 40) gives the officer two ways to start. One is selecting from the assigned list. The other is "entering an account number together with a mobile number for an applicant not on the list". In the second case the platform "shall confirm that the applicant holds a valid and unexpired sanction before allowing the officer to proceed", and it records that the verification was started by manual lookup rather than by assignment.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an applicant may turn up at a meeting without having been assigned, and the bank still wants to check that a sanction is valid before any capture, and to be able to tell later which verifications were not assigned.

## Example

An applicant at a meeting is not on the officer's list. The officer enters the applicant's account number and mobile number. The platform finds a valid, unexpired sanction and lets the officer go on. The verification is marked as started by manual lookup.

## Terms to know

- **Assigned list:** the applications that the bank has assigned to this officer.
- **Manual lookup:** the BRD's term for starting a verification by account number and mobile number instead of from the list.
- **Unexpired sanction:** a sanction whose validity period has not run out.
