import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("data/energy_cleaned.csv")

# Select India
india = df[df["country"] == "India"].copy()

# Remove missing values
india = india.dropna(
    subset=["year", "primary_energy_consumption"]
)

# Convert to numeric
india["year"] = pd.to_numeric(india["year"])
india["primary_energy_consumption"] = pd.to_numeric(
    india["primary_energy_consumption"]
)

# Sort by year
india = india.sort_values("year")

# Actual values
x = india["year"].values
actual = india["primary_energy_consumption"].values

# Fit linear trend
slope, intercept = np.polyfit(x, actual, 1)

# Predicted historical values
predicted = slope * x + intercept

# Calculate errors manually
errors = actual - predicted

mae = np.mean(np.abs(errors))

rmse = np.sqrt(np.mean(errors ** 2))

# Print results
print("MODEL EVALUATION")
print("----------------")

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")

print("\nNumber of historical observations:", len(actual))

print("\nInterpretation:")
print("MAE = average absolute prediction error.")
print("RMSE = prediction error with greater weight given to larger errors.")

print("\nModel evaluation completed successfully!")