---
id: concept.BR-LOS-121
type: concept
title: Names are tidied before they are compared with the account title
summary: "Before scoring, names are normalised by case folding, removing titles such as Md., Mohammad, Mst. and Begum, and collapsing spaces; the similarity threshold is configurable and defaults to requiring identical names after normalisation."
br_ids: [BR-LOS-121]
brd_section: 6.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-121"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
related: [bridge.BR-LOS-121, concept.BR-LOS-120]
version: 1
status: approved
approved_by: Owner
---
**In short:** Before scoring, names are normalised by case folding, removing titles such as Md., Mohammad, Mst. and Begum, and collapsing spaces; the similarity threshold is configurable and defaults to requiring identical names after normalisation.

## What the rule says

BR-LOS-121 (Must, BRD 6.3, PDF page 32) says name comparison applies normalisation before scoring: case folding, removal of honorifics and titles such as Md., Mohammad, Mst. and Begum, and whitespace collapse. The similarity threshold is configurable, defaulting to an exact match after normalisation. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the same person's name is written differently in different places, and a fair comparison should ignore case, titles and stray spaces.

## Example

The application says “MD.  Rahim Uddin” and the account title says “rahim uddin”. After case folding, removing “Md.” and collapsing the double space, both read “rahim uddin”, which is an exact match.

## Terms to know

- **Normalisation:** making two spellings of a name comparable.
- **Honorific:** a title such as Md. or Begum.
- **Similarity threshold:** how close two names must be to count as a match.
- **Case folding:** treating capital and small letters as the same.
