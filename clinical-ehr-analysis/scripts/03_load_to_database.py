import pandas as pd
import sqlite3
import os

# -----------------------------------------
# Setup paths
# -----------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "healthcare_dataset.csv")
DB_PATH = os.path.join(BASE_DIR, "clinical_ehr.db")

# -----------------------------------------
# Load dataset
# -----------------------------------------

df = pd.read_csv(DATA_PATH)

# Convert dates
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])
df["Length_of_Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days

# Risk flags
cost_threshold = df["Billing Amount"].quantile(0.80)
df["High_Cost_Flag"] = df["Billing Amount"] > cost_threshold
df["Long_Stay_Flag"] = df["Length_of_Stay"] > 20

# -----------------------------------------
# Connect to database
# -----------------------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Clear tables before reload (for development only)
cursor.execute("DELETE FROM billing")
cursor.execute("DELETE FROM diagnoses")
cursor.execute("DELETE FROM admissions")
cursor.execute("DELETE FROM patients")
conn.commit()

# -----------------------------------------
# Insert Patients
# -----------------------------------------

patients_df = df[["Name", "Age", "Gender", "Blood Type"]].drop_duplicates()
patients_df.columns = ["name", "age", "gender", "blood_type"]
patients_df.to_sql("patients", conn, if_exists="append", index=False)

print("Patients loaded.")

# Create patient ID mapping
patient_lookup = pd.read_sql("SELECT * FROM patients", conn)
df = df.merge(
    patient_lookup,
    left_on=["Name", "Age", "Gender", "Blood Type"],
    right_on=["name", "age", "gender", "blood_type"],
    how="left"
)

# -----------------------------------------
# Insert Admissions
# -----------------------------------------

admissions_df = df[[
    "patient_id",
    "Hospital",
    "Doctor",
    "Admission Type",
    "Date of Admission",
    "Discharge Date",
    "Length_of_Stay"
]].copy()

admissions_df.columns = [
    "patient_id",
    "hospital",
    "doctor",
    "admission_type",
    "admission_date",
    "discharge_date",
    "length_of_stay"
]

admissions_df.to_sql("admissions", conn, if_exists="append", index=False)

print("Admissions loaded.")

# Create admission ID mapping
admission_lookup = pd.read_sql("SELECT * FROM admissions", conn)
df["admission_id"] = admission_lookup["admission_id"]

# -----------------------------------------
# Insert Diagnoses
# -----------------------------------------

diagnoses_df = df[[
    "admission_id",
    "Medical Condition",
    "Test Results",
    "Medication"
]].copy()

diagnoses_df.columns = [
    "admission_id",
    "medical_condition",
    "test_results",
    "medication"
]

diagnoses_df.to_sql("diagnoses", conn, if_exists="append", index=False)

print("Diagnoses loaded.")

# -----------------------------------------
# Insert Billing
# -----------------------------------------

billing_df = df[[
    "admission_id",
    "Insurance Provider",
    "Billing Amount",
    "Room Number",
    "High_Cost_Flag",
    "Long_Stay_Flag"
]].copy()

billing_df.columns = [
    "admission_id",
    "insurance_provider",
    "billing_amount",
    "room_number",
    "high_cost_flag",
    "long_stay_flag"
]

billing_df.to_sql("billing", conn, if_exists="append", index=False)

print("Billing loaded.")

conn.commit()
conn.close()

print("\nDatabase successfully populated.")
