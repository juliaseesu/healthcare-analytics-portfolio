
# CMS Medicare Inpatient Utilization Data Wrangling Case Study

## Overview

This project demonstrates the transformation of a formatted CMS inpatient hospital utilization report into a structured, analysis-ready dataset.

The source data originates from the Centers for Medicare & Medicaid Services (CMS) and was distributed as a multi-sheet Excel file designed for publication rather than analysis.

The objective of this project was to clean, restructure, and export the data into a reproducible, machine-readable format suitable for healthcare analytics.

---

## Data Source

Centers for Medicare & Medicaid Services (CMS)  
Original Medicare – Inpatient Hospital Utilization Report (2023)

The original Excel file contained:

- Multiple sheets
- Merged-style headers
- Blank separator rows
- Hierarchical category labels
- Publication formatting artifacts

---

## Key Challenges

The dataset was not analysis-ready. Issues included:

- Header rows located several rows below the top of the sheet
- Blank rows and formatting placeholders (“BLANK” rows)
- Hierarchical category structure (e.g., All Beneficiaries, Aged Beneficiaries)
- Year values embedded within category rows
- Special characters in column names (¹, ²)

---

## Cleaning Process

The following transformation steps were implemented using Python and pandas:

1. Identified and applied the correct header row
2. Removed blank and formatting rows
3. Forward-filled entitlement category labels
4. Extracted numeric year values from mixed category column
5. Filtered only valid year rows
6. Standardized column names (removed special characters, replaced spaces)
7. Exported cleaned dataset to CSV format

---

## Final Output

The final cleaned dataset:

- 27 rows
- 29 structured variables
- Includes:
  - `year`
  - `entitlement_type`
  - Medicare utilization metrics
  - Payment metrics
  - Discharge statistics

Cleaned file location:
data/cleaned/cms_inpatient_utilization_cleaned.csv


---

## Skills Demonstrated

- Healthcare data wrangling
- Government dataset restructuring
- Excel publication format cleaning
- Hierarchical data transformation
- Reproducible data engineering workflow
- pandas data manipulation

---

## Project Structure

cms-medicare-inpatient-analysis/
│
├── data/
│ ├── MDCR INPT HOSP_CPS_05UIP_2023.xlsx
│ └── cleaned/
│ └── cms_inpatient_utilization_cleaned.csv
│
├── scripts/
│ └── 01_explore_cms.py
│
└── README.md


---

## Summary

This project highlights the ability to convert complex, formatted healthcare reports into structured analytical datasets suitable for downstream modeling, reporting, and healthcare operations analysis.