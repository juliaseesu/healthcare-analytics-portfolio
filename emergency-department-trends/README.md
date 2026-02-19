# Emergency Department Visit Trends (2016–2022)

## Overview

This project analyzes national Emergency Department (ED) visit trends in the United States from 2016 to 2022 using publicly available data from the Centers for Disease Control and Prevention (CDC).

The objective was to clean, structure, and analyze ED visit counts to identify national utilization patterns and year-over-year changes.

---

## Data Source

Centers for Disease Control and Prevention (CDC)  
Estimates of Emergency Department Visits in the United States (2016–2022)

The dataset includes visit counts, rates, demographic breakdowns, and diagnostic categories.

---

## Data Preparation

Cleaning steps included:

- Converting numeric fields stored as comma-separated strings into floats
- Filtering for reliable national estimates
- Selecting visit counts (not rates)
- Aggregating total ED visits by year
- Calculating year-over-year percentage change

---

## National ED Visit Counts (Total)

| Year | ED Visits | % Change |
|------|------------|-----------|
| 2016 | 466,283,000 | — |
| 2017 | 445,283,000 | -4.5% |
| 2018 | 418,757,000 | -6.0% |
| 2019 | 484,203,000 | +15.6% |
| 2020 | 417,461,000 | -13.8% |
| 2021 | 445,910,000 | +6.8% |
| 2022 | 492,345,000 | +10.4% |

---

## Key Insights

- ED utilization declined in 2017 and 2018.
- 2019 saw a significant increase in visits.
- 2020 experienced a major decline consistent with COVID-19 pandemic effects.
- 2021 and 2022 show strong recovery, with 2022 reaching the highest level in the series.

---

## Skills Demonstrated

- Healthcare time-series analysis
- Public health trend analysis
- Data cleaning and numeric conversion
- Aggregation and grouped analysis in pandas
- Year-over-year percentage change calculation
- Structured analytical reporting

---

## Project Structure
emergency-department-trends/
│
├── data/
│ └── Estimates_of_Emergency_Department_Visits_2016-2022.csv
│
├── scripts/
│ └── 01_explore_ed.py
│
└── README.md

---

## Summary

This project demonstrates the ability to move from raw public health data to structured trend analysis and interpretable national insights relevant to healthcare operations and population health monitoring.