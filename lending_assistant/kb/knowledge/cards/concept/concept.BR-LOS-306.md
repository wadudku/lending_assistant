---
id: concept.BR-LOS-306
type: concept
title: The risk grade can set limits and extra steps on the loan offered
summary: "The risk grade can drive a cap on amount, a cap on tenor, a pricing tier, extra verification or a security requirement, and a capped amount keeps both the requested and capped figures."
br_ids: [BR-LOS-306]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-306"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-002"
related: [bridge.BR-LOS-306, concept.BR-LOS-002]
version: 1
status: approved
approved_by: Owner
---
**In short:** The risk grade can drive a cap on amount, a cap on tenor, a pricing tier, extra verification or a security requirement, and a capped amount keeps both the requested and capped figures.

## What the rule says

BR-LOS-306 (Must, BRD 6.4, PDF page 34) says the risk grade can drive product treatment as configured: a cap on the amount offered, a cap on tenor, a pricing tier, a requirement for additional verification steps, or a requirement for security. Where the grade caps the amount, both the requested and the capped figures are retained and surfaced. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a riskier borrower may be offered a smaller or shorter loan, at a different price, instead of being refused outright. The 6.4.1 table gives examples (PDF page 35).

## Example

A borrower asks for 200,000 over 24 months and is graded moderate risk. The grade caps the offer at 150,000 over 18 months. The record shows both the 200,000 asked and the 150,000 offered.

## Terms to know

- **Cap:** an upper limit.
- **Pricing tier:** a rate level linked to risk.
- **Additional verification:** an extra check before the loan goes ahead.
- **Security:** something pledged to back the loan.
