import pandas as pd

# Load ORIGINAL dataset
df = pd.read_csv("energy_data.csv")

# Countries/entities for our analysis
selected_countries = [
    "India",
    "China",
    "United States",
    "World"
]

# Keep only selected countries
df = df[df["country"].isin(selected_countries)].copy()

# Keep useful columns
columns_to_keep = [
    "country",
    "year",
    "population",
    "gdp",
    "primary_energy_consumption",
    "energy_per_gdp",
    "energy_per_capita",
    "oil_consumption",
    "gas_consumption",
    "coal_consumption",
    "nuclear_consumption",
    "hydro_consumption",
    "solar_consumption",
    "wind_consumption",
    "renewables_consumption"
]

df = df[columns_to_keep]

# Remove rows where year is missing
df = df.dropna(subset=["year"])

# Sort data
df = df.sort_values(["country", "year"])

# Reset index
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("energy_cleaned.csv", index=False)

# -----------------------------
# CHECK THE RESULT
# -----------------------------

print("Cleaned dataset shape:")
print(df.shape)

print("\nCountries included:")
print(df["country"].unique())

print("\nFirst 10 rows:")
print(df.head(10).to_string(index=False))

print("\nIndia sample:")
print(
    df[df["country"] == "India"]
    .head(10)
    .to_string(index=False)
)

print("\nMissing values:")
print(df.isnull().sum())