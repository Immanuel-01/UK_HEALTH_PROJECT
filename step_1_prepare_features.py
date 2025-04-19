import pandas as pd
from sklearn.preprocessing import StandardScaler

# === Load cleaned UK dataset ===
uk_data_path = "Data/Processed/UK_Health_Disparity.csv"
uk_cleaned_df = pd.read_csv(uk_data_path)

# === (Optional Check) Column Health
print("\n🧠 Column Overview:")
print(uk_cleaned_df.info())

# === Drop unnecessary columns ===
model_df = uk_cleaned_df.drop(columns=["Year", "Disease Name"])

# === One-hot encode categorical features ===
model_df_encoded = pd.get_dummies(model_df, columns=[
    "Gender", "Age Group", "Disease Category", "Treatment Type"
], drop_first=True)

# === Separate features and target ===
X = model_df_encoded.drop(columns=["Mortality Rate (%)"])
y = model_df_encoded["Mortality Rate (%)"]

# === Standardize features ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === Preview
print("✅ Feature preparation complete.")
print("📊 X shape:", X_scaled.shape)
print("🎯 y shape:", y.shape)
