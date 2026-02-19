import pandas as pd
import os

# -----------------------------------------
# Set file path relative to project root
# -----------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "healthcare_dataset.csv")

# -----------------------------------------
# Load dataset
# -----------------------------------------

try:
    df = pd.read_csv(DATA_PATH)
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("ERROR: File not found. Check your data folder.")
    print(f"Looking for file at: {DATA_PATH}")
    exit()

# -----------------------------------------
# Basic Exploration
# -----------------------------------------

print("First 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Shape:")
print(df.shape)
