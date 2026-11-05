---
id: concept.BR-LOS-320
type: concept
title: "The proposed sanction is set from product, grade, headroom and borrower exposure"
summary: "The platform sets the proposed amount, tenor, rate and fees from the product setting, the risk grade's treatment, the partner's remaining headroom and the borrower's total exposure."
br_ids: [BR-LOS-320]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-320"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-306"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-331"
related: [bridge.BR-LOS-320, concept.BR-LOS-306, concept.BR-LOS-331, concept.BR-LOS-103, glossary.scorecard, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform sets the proposed amount, tenor, rate and fees from the product setting, the risk grade's treatment, the partner's remaining headroom and the borrower's total exposure.

## What the rule says

BR-LOS-320 (Must, BRD 6.6, PDF page 37) says the platform determines the proposed sanction (amount, tenor, applicable rate and fees) from the product configuration, the treatment attaching to the application's risk grade under BR-LOS-306, the partner's remaining exposure headroom, and the borrower's aggregate exposure under BR-LOS-331. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.6 introduction: sanction is the Bank's decision to lend, on stated terms, to a named applicant. The scorecard and product configuration should carry the routine cases, and a credit officer should see everything above that line. Sanction happens before assignment, so that no field officer is sent to meet an applicant the Bank has not agreed to lend to (PDF page 37).

## Example

A borrower asks for 200,000 over 24 months. The product allows it, the grade caps it at 150,000 over 18 months, the partner has 400,000 of headroom, and the borrower owes 20,000 elsewhere. The proposed sanction is 150,000 over 18 months at the rate and fees of that tier.

## Terms to know

- **Sanction:** the Bank's decision to lend an amount on stated terms.
- **Headroom:** the room left under a ceiling.
- **Aggregate exposure:** everything the borrower owes across loans.
- **Treatment:** what the risk grade does to the offer. See BR-LOS-306.
