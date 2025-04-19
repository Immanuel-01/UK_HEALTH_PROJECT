import pandas as pd
import os

# === Define file paths ===
raw_data_path = "Data/Raw/Global Health Statistics.csv"
uk_data_output_path = "Data/Processed/UK_Health_Disparity.csv"

# === Ensure processed folder exists ===
os.makedirs("Data/Processed", exist_ok=True)

# === Load global dataset ===
global_health_df = pd.read_csv(raw_data_path)

# === Filter for UK only (case-insensitive match) ===
uk_health_df = global_health_df[global_health_df["Country"].str.upper() == "UK"]

# === Select relevant columns ===
selected_columns = [
    "Year", "Disease Name", "Disease Category", "Gender", "Age Group",
    "Mortality Rate (%)", "Recovery Rate (%)", "Healthcare Access (%)",
    "Average Treatment Cost (USD)", "Treatment Type", "DALYs"
]
uk_cleaned_df = uk_health_df[selected_columns]

# === Save cleaned dataset ===
uk_cleaned_df.to_csv(uk_data_output_path, index=False)
print("✅ Cleaned UK dataset saved successfully!")
print(uk_cleaned_df.head())
