---
id: brd_section.8.2
type: brd_section
title: BRD 8.2 Servicing reporting and statements
summary: "Section 8.2 lists 14 servicing reports with their purpose, then asks for a servicing dashboard, report headers that state how the report was produced, and export and scheduling."
br_ids: []
brd_section: 8.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#8.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p57"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-240"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-241"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-242"
related: [brd_section.8, brd_section.7, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 8.2 lists 14 servicing reports with their purpose, then asks for a servicing dashboard, report headers that state how the report was produced, and export and scheduling.

## What this section says

BRD 8.2 (PDF pages 57 and 58) starts with a table of 14 reports, each with a business purpose: statement of account (per loan); scheduled borrower statements; loan outstanding report; future cash flow report; past cash flow report; ageing / asset-liability report; repayment and closure report; delinquency and DPD report; provisioning report; security exposure reports; write-off and recovery report; restructuring register; disbursement analysis; and partner economics report. Three requirements follow on PDF page 58, all Must. BR-LMS-240: a servicing dashboard showing book size and composition, collection performance against demand, DPD distribution, classification movement, provision position and exception queue volumes. BR-LMS-241: every report states when it was generated, the parameters used and the data cut-off applied. BR-LMS-242: reports exportable to XLSX and CSV, schedulable, and deliverable to configured recipients.

## Why the bank wants it

The BRD gives one reason for all of Section 8 on PDF page 57: Credit Risk, Finance, Compliance and Internal Audit each need a view that the current process cannot produce reliably at volume. It doesn't say why 8.2 in particular asks for these 14 reports.

## How it meets Frappe Lending

The team's analysis covered Section 7 only. BR-LMS-240 to BR-LMS-242 carry the LMS prefix but sit in Section 8.2, outside the 103 requirements of Section 7, so none of the 3 was analysed and the team makes no statement about them. The 14 reports in the table are not requirement rows. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.8`. Term: `glossary.dpd`.
