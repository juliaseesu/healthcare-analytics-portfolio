import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "Estimates_of_Emergency_Department_Visits_in_the_United_States_from_2016-2022_20260219.csv"
)

df = pd.read_csv(DATA_PATH)

# Clean numeric columns
numeric_cols = [
    "Estimate",
    "Standard Error",
    "Lower 95% CI",
    "Upper 95% CI"
]

for col in numeric_cols:
    df[col] = (
        df[col]
        .str.replace(",", "", regex=False)
        .astype(float)
    )

# Filter for national totals
df_total = df[
    (df["Group"] == "Total") &
    (df["Estimate Type"] == "Visit count") &
    (df["Reliable"] == "Yes")
]

# Aggregate total visits by year
annual_trend = (
    df_total
    .groupby("Year")["Estimate"]
    .sum()
    .reset_index()
    .sort_values("Year")
)

print("\nNational Emergency Department Visit Counts by Year:")
print(annual_trend)

annual_trend["pct_change"] = annual_trend["Estimate"].pct_change() * 100

print("\nNational ED Visit Trend with Year-over-Year % Change:")
print(annual_trend)