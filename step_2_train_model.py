import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib
import os

# === Ensure models folder exists ===
os.makedirs("uk_mortality_app/models", exist_ok=True)

# === Load dataset ===
df = pd.read_csv("Data/Processed/UK_Health_Disparity.csv")
df = df.drop(columns=["Year", "Disease Name"])

# === Encode categorical variables ===
df_encoded = pd.get_dummies(df, columns=[
    "Gender", "Age Group", "Disease Category", "Treatment Type"
], drop_first=True)

# === Split features and target ===
X = df_encoded.drop(columns=["Mortality Rate (%)"])
y = df_encoded["Mortality Rate (%)"]

# === Scale features ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === Split data ===
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# === Train model ===
model = LinearRegression()
model.fit(X_train, y_train)

# === Evaluate ===
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model trained!")
print(f"📉 Mean Squared Error: {mse:.4f}")
print(f"📈 R² Score: {r2:.4f}")

# === Save model and scaler ===
model.feature_names = X.columns.tolist()  # <-- NEW LINE
joblib.dump(model, "uk_mortality_app/models/uk_mortality_risk_model.pkl")
joblib.dump(scaler, "uk_mortality_app/models/uk_mortality_scaler.pkl")
print("💾 Model and scaler saved in 'models/' folder!")

