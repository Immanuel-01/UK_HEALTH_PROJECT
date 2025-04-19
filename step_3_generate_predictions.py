import pandas as pd
import joblib

# === Load cleaned UK dataset ===
uk_data_path = "Data/Processed/UK_Health_Disparity.csv"
uk_df = pd.read_csv(uk_data_path)

# === Keep original copy for exporting predictions ===
original_df = uk_df.copy()

# === Drop unneeded columns and encode ===
df_model = uk_df.drop(columns=["Year", "Disease Name"])
df_encoded = pd.get_dummies(df_model, columns=[
    "Gender", "Age Group", "Disease Category", "Treatment Type"
], drop_first=True)

# === Load trained model and scaler ===
model = joblib.load("uk_mortality_app/models/uk_mortality_risk_model.pkl")
scaler = joblib.load("uk_mortality_app/models/uk_mortality_scaler.pkl")

# === Prepare features and predict ===
X = df_encoded.drop(columns=["Mortality Rate (%)"])
X_scaled = scaler.transform(X)
y_pred = model.predict(X_scaled)

# === Append predictions to original dataset ===
original_df["Predicted Mortality Rate (%)"] = y_pred

# === Save to CSV for Power BI ===
original_df.to_csv("Data/Processed/UK_Mortality_Predictions.csv", index=False)
print("✅ Predictions saved to 'Data/Processed/UK_Mortality_Predictions.csv'")
