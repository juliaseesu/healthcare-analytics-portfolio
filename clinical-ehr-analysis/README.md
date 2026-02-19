# Clinical EHR Data Analysis Project

## Project Overview

This project simulates an inpatient hospital analytics workflow using 55,500 electronic health record (EHR) admissions.

The objective was to normalize raw EHR data into a relational database and perform SQL-based analysis to evaluate:

- Length of stay (LOS)
- High-cost patient identification
- Insurance impact on utilization
- Hospital-level cost benchmarking
- Condition-based risk stratification

This project demonstrates applied healthcare data analysis and foundational clinical informatics concepts.

---

## Dataset Description

The dataset represents inpatient hospital admissions and includes:

- Patient demographics (age, gender, blood type)
- Admission and discharge dates
- Admission type (Emergency, Urgent, Elective)
- Medical condition
- Medication and test results
- Hospital and provider information
- Insurance provider
- Billing amount

Total Records: 55,500 admissions

---

## Database Architecture

The flat EHR dataset was normalized into a relational SQLite database consisting of four tables:

- `patients`
- `admissions`
- `diagnoses`
- `billing`

Relationships:

- One patient can have multiple admissions
- Each admission has associated diagnosis and billing records

This structure reflects how EHR systems organize clinical and financial data in practice.

---

## Technologies Used

- Python (pandas)
- SQLite
- SQL
- Visual Studio Code

---

## Clinical Metrics Engineered

### Length of Stay (LOS)
- Average LOS: 15.5 days
- Emergency admissions had the highest proportion of long-stay cases (~34%)

### High-Cost Admission Identification
- Top 20% billing threshold: $40,285
- 11,100 admissions flagged as high-cost
- Chronic conditions such as hypertension, asthma, and diabetes were most represented among high-cost cases

### Insurance-Based Utilization
- Medicare admissions showed the highest average LOS (15.63 days)
- This aligns with typical higher-acuity and older patient populations

### Hospital Cost Benchmarking
- Identified hospitals with the highest average billing using SQL aggregation
- Demonstrated ability to perform cost comparisons across facilities

---

## Example SQL Queries

### Average LOS by Insurance

```sql
SELECT 
    insurance_provider,
    ROUND(AVG(a.length_of_stay), 2) AS avg_los
FROM billing b
JOIN admissions a ON b.admission_id = a.admission_id
GROUP BY insurance_provider
ORDER BY avg_los DESC;

----
### High-Cost Rate by Medical Condition

''''sql
SELECT 
    d.medical_condition,
    COUNT(*) AS total_cases,
    SUM(b.high_cost_flag) AS high_cost_cases,
    ROUND(100.0 * SUM(b.high_cost_flag) / COUNT(*), 2) AS high_cost_percentage
FROM diagnoses d
JOIN billing b ON d.admission_id = b.admission_id
GROUP BY d.medical_condition
ORDER BY high_cost_percentage DESC;


## Skills Demonstrated

Through this project, I applied core healthcare data analysis skills including:

- Structuring and normalizing EHR-style data into a relational database
- Writing multi-table SQL queries to analyze clinical and financial metrics
- Developing healthcare-specific measures such as length of stay and high-cost admission flags
- Performing utilization and cost comparisons across hospitals and insurance providers
- Translating technical findings into healthcare-relevant insights

This project reflects both technical SQL proficiency and an understanding of how hospital data supports operational and clinical decision-making.

---

## Author

Julia Giles  
B.S. in Information Systems  

I am pursuing entry-level roles in Healthcare Data Analytics and Clinical Informatics, with a focus on applying data to improve hospital operations, patient outcomes, and healthcare reporting.
