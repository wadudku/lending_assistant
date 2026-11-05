---
id: concept.BR-LOS-321
type: concept
title: Automatic sanction only inside every configured threshold
summary: "The platform sanctions automatically only where the application is within every auto-sanction threshold; thresholds are set by amount band, risk grade, tenor, product and partner, versioned, effective-dated and approved by a second person."
br_ids: [BR-LOS-321]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-321"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-322"
related: [bridge.BR-LOS-321, glossary.maker-checker, concept.BR-LOS-322, glossary.scorecard, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform sanctions automatically only where the application is within every auto-sanction threshold; thresholds are set by amount band, risk grade, tenor, product and partner, versioned, effective-dated and approved by a second person.

## What the rule says

BR-LOS-321 (Must, BRD 6.6, PDF page 37) says the platform sanctions automatically only where the application falls within every configured auto-sanction threshold. Thresholds are configurable by amount band, risk grade, tenor, product and partner, and are versioned, effective-dated and subject to maker-checker. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.6 introduction: sanction is the Bank's decision to lend, on stated terms, to a named applicant. The scorecard and product configuration should carry the routine cases, and a credit officer should see everything above that line. Sanction happens before assignment, so that no field officer is sent to meet an applicant the Bank has not agreed to lend to (PDF page 37).

## Example

Thresholds: loans up to 100,000, grades A and B, tenor up to 12 months. An application for 80,000, grade B, 12 months is within all of them, so the system sanctions it. An application for 80,000 at grade C is outside one, so it goes to a person.

## Terms to know

- **Auto-sanction:** the platform sanctions without a person deciding.
- **Threshold:** a limit that an application must stay within.
- **Maker-checker:** one person proposes and another approves. See `glossary.maker-checker`.
- **Amount band:** a range of loan amounts.
