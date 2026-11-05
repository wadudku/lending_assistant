---
id: concept.BR-GOV-025
type: concept
title: Sensitive personal data is permissioned apart and every look is logged
summary: "Credit bureau data, identity images, biometrics and a borrower's full financial position need their own permission, and every access is logged with who, which record and when."
br_ids: [BR-GOV-025]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-025"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [bridge.BR-GOV-025, concept.BR-GOV-020, concept.BR-GOV-027]
version: 1
status: approved
approved_by: Owner
---
**In short:** Credit bureau data, identity images, biometrics and a borrower's full financial position need their own permission, and every access is logged with who, which record and when.

## What the rule says

BR-GOV-025 (Must, BRD 4.3, PDF page 23) says access to credit bureau data, identity images, biometric captures and full borrower financial position is separately permissioned from ordinary operational access. Every access is logged with user, record and timestamp.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that this data is the most sensitive the bank holds, so only staff who need it should see it, and the bank should be able to show who did.

## Example

A collections officer can open a loan but not the borrower's identity image. A credit analyst with the extra permission can open it, and the system records the analyst, the record and the time.

## Terms to know

- **Credit bureau data:** a borrower's credit history held by an outside bureau.
- **Biometric capture:** a fingerprint or face image used to identify a person.
- **Separately permissioned:** needs its own permission on top of ordinary access.
- **Access log:** a record of who opened what, and when.
