---
id: concept.BR-LOS-323
type: concept
title: The credit approver sees the whole case on one screen
summary: "The credit approver sees on one screen the KYC, account result, grade and reasons, bureau data, flags, sampling outcome, partner context, borrower exposure and proposed terms."
br_ids: [BR-LOS-323]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-323"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-305"
related: [bridge.BR-LOS-323, concept.BR-LOS-320, concept.BR-LOS-305, glossary.sampling, glossary.scorecard, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** The credit approver sees on one screen the KYC, account result, grade and reasons, bureau data, flags, sampling outcome, partner context, borrower exposure and proposed terms.

## What the rule says

BR-LOS-323 (Must, BRD 6.6, PDF page 38) says the credit approver sees, on one screen: the submitted KYC; the account validation result; the risk grade, recommended decision and principal adverse reason codes; bureau data in full where the inquiry has been performed at this stage; duplicate and mandatory-sampling flags; the sampling outcome and reviewer's note where the application was sampled; partner context and track record; the borrower's aggregate exposure; and the proposed terms. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.6 introduction: sanction is the Bank's decision to lend, on stated terms, to a named applicant. The scorecard and product configuration should carry the routine cases, and a credit officer should see everything above that line. Sanction happens before assignment, so that no field officer is sent to meet an applicant the Bank has not agreed to lend to (PDF page 37).

## Example

An approver opens a case and, without leaving the screen, reads the applicant's KYC, the account check, grade B with its reasons, the bureau report, the partner's record, the borrower's total exposure and the proposed terms.

## Terms to know

- **KYC:** know-your-customer: the identity details a bank keeps.
- **Bureau data:** a person's credit history held by a credit bureau.
- **Principal adverse reason codes:** the main coded reasons that pushed the result towards review or refusal.
- **Partner context:** how the partner's earlier loans have done.
