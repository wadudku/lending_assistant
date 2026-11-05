---
id: glossary.repricing
type: glossary
title: Repricing
summary: "A change, from a chosen date onwards, to the interest rate of an eligible floating-rate loan."
br_ids: [BR-LMS-150]
brd_section: 7.6
doctypes: [Loan]
dev_items: []
terms: [repricing, rate reset, rate change]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-150"
related: [devitem.D11, devitem.D4]
version: 1
status: approved
approved_by: Owner
---
**In short:** A change, from a chosen date onwards, to the interest rate of an eligible floating-rate loan.

## Plain meaning

The BRD defines repricing as a prospective change to the interest rate of an eligible floating-rate loan (BRD 1.5). Prospective means it applies from a date forward; what has already been paid is not changed.

## Example

A benchmark rate goes up by 1 point. From 1 October, the rate on Rahim's floating-rate loan rises by 1 point. His earlier instalments stay as they were.

## Why it matters here

BRD 7.6 (BR-LMS-150 to BR-LMS-159) sets the rules for repricing many loans together. In the test, Frappe Lending had no bulk repricing; the closest tool is a single-loan restructure.

## See also

`devitem.D11`, `devitem.D4`, `glossary.effective-date`.
