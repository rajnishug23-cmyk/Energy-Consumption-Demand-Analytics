import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("energy_cleaned.csv")

# Select India
india = df[df["country"] == "India"].copy()

# Keep only rows where energy consumption is available
india = india.dropna(
    subset=["year", "primary_energy_consumption"]
)

# Sort by year
india = india.sort_values("year")

# Convert columns to numeric
india["year"] = pd.to_numeric(india["year"])
india["primary_energy_consumption"] = pd.to_numeric(
    india["primary_energy_consumption"]
)

# --------------------------------------------------
# Train model using historical data
# --------------------------------------------------

x = india["year"].values
y = india["primary_energy_consumption"].values

# Fit a linear trend
slope, intercept = np.polyfit(x, y, 1)

# Historical fitted values
india["predicted_consumption"] = (
    slope * india["year"] + intercept
)

# --------------------------------------------------
# Forecast next 5 years
# --------------------------------------------------

last_year = int(india["year"].max())

future_years = np.arange(
    last_year + 1,
    last_year + 6
)

future_predictions = (
    slope * future_years + intercept
)

forecast = pd.DataFrame({
    "year": future_years,
    "forecasted_energy_consumption": future_predictions
})

# --------------------------------------------------
# Display forecast
# --------------------------------------------------

print("Historical data ends in:", last_year)

print("\nForecast for the next 5 years:")
print(forecast.to_string(index=False))

# --------------------------------------------------
# Save forecast
# --------------------------------------------------

forecast.to_csv(
    "data/india_energy_forecast.csv",
    index=False
)

# --------------------------------------------------
# Plot historical + forecast
# --------------------------------------------------

plt.figure(figsize=(11, 6))

plt.plot(
    india["year"],
    india["primary_energy_consumption"],
    label="Historical Consumption"
)

plt.plot(
    future_years,
    future_predictions,
    linestyle="--",
    label="Forecast"
)

plt.title(
    "India's Primary Energy Consumption: Historical Trend and Forecast"
)

plt.xlabel("Year")
plt.ylabel("Primary Energy Consumption")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("india_energy_forecast.png")

plt.show()

print("\nForecast completed successfully!")