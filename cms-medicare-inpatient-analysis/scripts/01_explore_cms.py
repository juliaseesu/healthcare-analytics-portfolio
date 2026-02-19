import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "MDCR INPT HOSP_CPS_05UIP_2023.xlsx")

sheet_name = "MDCR INPT HOSP 1_CPS_05UIP"

# Load with correct header row
df = pd.read_excel(DATA_PATH, sheet_name=sheet_name, header=3)

# Rename first column
df = df.rename(columns={"Type of Entitlement and Calendar Year": "entitlement_or_year"})

# Remove BLANK rows
df = df[df["entitlement_or_year"] != "BLANK"]

# Forward fill category labels
df["entitlement_or_year"] = df["entitlement_or_year"].ffill()

# Identify year rows (numeric values only)
df["year"] = pd.to_numeric(df["entitlement_or_year"], errors="coerce")

# Separate category and year
df["entitlement_type"] = df["entitlement_or_year"].where(df["year"].isna())

# Forward fill entitlement type
df["entitlement_type"] = df["entitlement_type"].ffill()

# Keep only rows where year exists
df_clean = df[df["year"].notna()].copy()

# Drop helper column
df_clean = df_clean.drop(columns=["entitlement_or_year"])

print("\nCleaned Data Preview:")
print(df_clean.head())

print("\nShape After Cleaning:")
print(df_clean.shape)

# Create cleaned folder if it doesn't exist
cleaned_path = os.path.join(BASE_DIR, "data", "cleaned")
os.makedirs(cleaned_path, exist_ok=True)

# Save cleaned dataset
output_file = os.path.join(cleaned_path, "cms_inpatient_utilization_cleaned.csv")
df_clean.to_csv(output_file, index=False)

print("\nCleaned file saved to:")
print(output_file)

# Clean column names (remove special characters and spaces)
df_clean.columns = (
    df_clean.columns
    .str.replace("¹", "", regex=False)
    .str.replace("²", "", regex=False)
    .str.replace(" ", "_")
    .str.replace(",", "")
    .str.replace("/", "_")
)

print("\nColumns After Cleaning:")
print(df_clean.columns)