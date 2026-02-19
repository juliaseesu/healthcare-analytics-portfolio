import pandas as pd
import os

# -----------------------------------------
# Load dataset
# -----------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "healthcare_dataset.csv")

df = pd.read_csv(DATA_PATH)

# -----------------------------------------
# Convert date columns to datetime
# -----------------------------------------

df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])

# -----------------------------------------
# Create Length of Stay (LOS)
# -----------------------------------------

df["Length_of_Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days

# -----------------------------------------
# Basic LOS statistics
# -----------------------------------------

print("Average Length of Stay:", df["Length_of_Stay"].mean())
print("Max Length of Stay:", df["Length_of_Stay"].max())
print("Min Length of Stay:", df["Length_of_Stay"].min())

print("\nLength of Stay by Admission Type:")
print(df.groupby("Admission Type")["Length_of_Stay"].mean())

print("\nLength of Stay by Medical Condition (Top 5):")
print(df.groupby("Medical Condition")["Length_of_Stay"].mean().sort_values(ascending=False).head())

# -----------------------------------------
# Billing vs Length of Stay
# -----------------------------------------

print("\nAverage Billing Amount:", df["Billing Amount"].mean())

print("\nBilling by Admission Type:")
print(df.groupby("Admission Type")["Billing Amount"].mean())

print("\nTop 5 Most Expensive Conditions:")
print(
    df.groupby("Medical Condition")["Billing Amount"]
    .mean()
    .sort_values(ascending=False)
    .head()
)

# Correlation between LOS and Billing
correlation = df["Length_of_Stay"].corr(df["Billing Amount"])
print("\nCorrelation between LOS and Billing:", correlation)

# -----------------------------------------
# Risk Stratification
# -----------------------------------------

# High Cost Flag (Top 20% billing)
cost_threshold = df["Billing Amount"].quantile(0.80)
df["High_Cost_Flag"] = df["Billing Amount"] > cost_threshold

# Long Stay Flag (LOS > 20 days)
df["Long_Stay_Flag"] = df["Length_of_Stay"] > 20

print("\nHigh Cost Threshold:", cost_threshold)

print("\nNumber of High Cost Patients:")
print(df["High_Cost_Flag"].sum())

print("\nNumber of Long Stay Patients:")
print(df["Long_Stay_Flag"].sum())

print("\nHigh Cost Patients by Medical Condition:")
print(
    df[df["High_Cost_Flag"]]
    .groupby("Medical Condition")
    .size()
    .sort_values(ascending=False)
    .head()
)
