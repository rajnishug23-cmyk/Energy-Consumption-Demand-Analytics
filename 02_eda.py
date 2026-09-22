import pandas as pd

# Load cleaned dataset
df = pd.read_csv("energy_cleaned.csv")

# Convert year to integer
df["year"] = df["year"].astype(int)

# --------------------------------------------------
# 1. Basic dataset information
# --------------------------------------------------

print("Dataset shape:")
print(df.shape)

print("\nYears covered:")
print(df["year"].min(), "to", df["year"].max())

print("\nNumber of countries/entities:")
print(df["country"].nunique())

# --------------------------------------------------
# 2. Select major countries
# --------------------------------------------------

countries = [
    "India",
    "China",
    "United States",
    "World"
]

selected = df[df["country"].isin(countries)].copy()

print("\nSelected countries:")
print(selected["country"].unique())

# --------------------------------------------------
# 3. Latest available data
# --------------------------------------------------

latest_year = selected["year"].max()

latest = selected[selected["year"] == latest_year]

print("\nLatest available year:", latest_year)

print("\nLatest energy consumption:")
print(
    latest[
        [
            "country",
            "year",
            "primary_energy_consumption",
            "energy_per_capita"
        ]
    ].to_string(index=False)
)

# --------------------------------------------------
# 4. India's historical energy consumption
# --------------------------------------------------

india = selected[selected["country"] == "India"].copy()

print("\nIndia energy consumption:")
print(
    india[
        [
            "year",
            "primary_energy_consumption",
            "energy_per_capita"
        ]
    ].tail(10).to_string(index=False)
)

# --------------------------------------------------
# 5. Energy source comparison
# --------------------------------------------------

energy_sources = [
    "oil_consumption",
    "gas_consumption",
    "coal_consumption",
    "nuclear_consumption",
    "hydro_consumption",
    "solar_consumption",
    "wind_consumption",
    "renewables_consumption"
]

print("\nIndia's latest energy mix:")

india_latest = india[india["year"] == india["year"].max()]

print(
    india_latest[
        ["year"] + energy_sources
    ].to_string(index=False)
)

# --------------------------------------------------
# 6. Growth calculation
# --------------------------------------------------

india = india.sort_values("year")

india["energy_growth_%"] = (
    india["primary_energy_consumption"]
    .pct_change() * 100
)

print("\nIndia's recent energy consumption growth:")

print(
    india[
        [
            "year",
            "primary_energy_consumption",
            "energy_growth_%"
        ]
    ].tail(10).to_string(index=False)
)