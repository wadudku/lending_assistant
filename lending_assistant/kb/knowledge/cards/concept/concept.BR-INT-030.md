---
id: concept.BR-INT-030
type: concept
title: "The bureau inquiry runs from a designated host, through automation, under the same controls"
summary: "A bureau inquiry runs from a designated host inside the bank's permitted network, through robotic process automation driving the bureau interface, under the same controls as section 9.3."
br_ids: [BR-INT-030]
brd_section: 9.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-030"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-030, brd_section.9.3, glossary.rpa, glossary.cib]
version: 1
status: approved
approved_by: Owner
---
**In short:** A bureau inquiry runs from a designated host inside the bank's permitted network, through robotic process automation driving the bureau interface, under the same controls as section 9.3.

## What the rule says

BR-INT-030 (Must, BRD 9.5, PDF page 64) says the bureau inquiry runs from a designated host within the bank's permitted network perimeter, through robotic process automation driving the bureau interface. It is subject to the same controls as Section 9.3. CIB is the Credit Information Bureau of Bangladesh Bank (BRD 1.5).

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bureau interface is reached by driving its screens, like the core banking system, so it needs the same safeguards on credentials and location.

## Example

The credit check on an applicant is sent from one named machine inside the bank's network. The automation signs in to the bureau's interface, reads the result and returns it. The same rules as for the core banking system automation apply.

## Terms to know

- **Bureau inquiry:** a request for a borrower's credit history.
- **Designated host:** the machine the bank has named for the inquiry.
- **RPA:** software that drives screens like an operator. See `glossary.rpa`.
