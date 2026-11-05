---
id: glossary.effective-date
type: glossary
title: Effective date
summary: "The date from which a change of terms or rate applies. It is a different date from the value date, and the BRD asks for them to be kept apart."
br_ids: [BR-GOV-010, BR-LMS-117, BR-LMS-151]
brd_section: 1.5
doctypes: []
dev_items: []
terms: [effective date, start date of a change, date a change applies]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-117"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-151"
related: [glossary.value-date, glossary.posting-date]
version: 1
status: approved
approved_by: Owner
---
**In short:** The date from which a change of terms or rate applies. It is a different date from the value date, and the BRD asks for them to be kept apart.

## Plain meaning

The BRD defines the effective date as the date from which a term or rate change applies (BRD 1.5). It is not the value date, which is the date the core banking system recognises a transaction (`glossary.value-date`), nor the posting date. BR-GOV-010 says the effective date, posting date, value date and system timestamp are recorded and used as distinct concepts, and never conflated.

## Example

On 20 September the bank decides to raise the rate on Rahim's floating-rate loan, starting 1 October. The effective date is 1 October. The date the bank typed it in (the posting date) is 20 September.

## Why it matters here

BR-LMS-151 asks that a new rate starts on a set date, and BR-LMS-117 asks that product rules have versions and start dates. In the test, Frappe Lending had no effective date in any bulk rate change and none on product rules; both are gaps.

## See also

`glossary.value-date`, `glossary.posting-date`, `glossary.repricing`, `devitem.D5`.
