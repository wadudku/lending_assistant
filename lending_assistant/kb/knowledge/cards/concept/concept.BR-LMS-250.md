---
id: concept.BR-LMS-250
type: concept
title: A monthly extract for the Credit Information Bureau
summary: "The platform produces the monthly CIB contribution extract, with every field Bangladesh Bank requires for each reportable loan; the bank is to supply the format."
br_ids: [BR-LMS-250]
brd_section: 8.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-250"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [bridge.BR-LMS-250, glossary.bb, glossary.cib]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform produces the monthly CIB contribution extract, with every field Bangladesh Bank requires for each reportable loan; the bank is to supply the format.

## What the rule says

BR-LMS-250 (Must, BRD 8.3, PDF page 58) says the platform supports the monthly CIB contribution extract, carrying every field Bangladesh Bank requires for each reportable loan. The required format is to be supplied by the bank. CIB is the Credit Information Bureau of Bangladesh Bank (BRD 1.5). The id carries the LMS prefix, but the row sits in Section 8.3, outside the 103 requirements of Section 7.

## Why the bank wants it

A note on PDF page 58 says the regulatory obligations are the Bank's to set, not the supplier's, and that the Bank supplies the rule set, the return formats and the submission calendar. The BRD doesn't say why the extract is monthly; the usual reason is that the bureau collects each member bank's borrower data on a fixed monthly cycle.

## Example

After month end, the platform produces the file of every loan that must be reported, with the fields the bureau asks for on each. The bank reviews it and submits it. If one loan has a field missing, that loan is listed, so the gap is fixed before the file is sent.

## Terms to know

- **CIB:** the Credit Information Bureau of Bangladesh Bank, the source of borrower credit history.
- **Contribution extract:** the file a bank sends to the bureau with its loans' data.
- **Reportable loan:** a loan that the bureau's rules say must be included.
