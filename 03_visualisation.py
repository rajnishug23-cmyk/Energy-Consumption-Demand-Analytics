import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("energy_cleaned.csv")

# -----------------------------
# 1. India energy consumption
# -----------------------------

india = df[df["country"] == "India"].copy()

india = india.sort_values("year")

plt.figure(figsize=(10, 5))

plt.plot(
    india["year"],
    india["primary_energy_consumption"]
)

plt.title("India's Primary Energy Consumption Over Time")
plt.xlabel("Year")
plt.ylabel("Primary Energy Consumption")

plt.grid(True)
plt.tight_layout()
plt.show()


# -----------------------------
# 2. India energy consumption per capita
# -----------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    india["year"],
    india["energy_per_capita"]
)

plt.title("India's Energy Consumption Per Capita")
plt.xlabel("Year")
plt.ylabel("Energy Consumption Per Capita")

plt.grid(True)
plt.tight_layout()
plt.show()


# -----------------------------
# 3. Compare major countries
# -----------------------------

countries = [
    "India",
    "China",
    "United States"
]

comparison = df[df["country"].isin(countries)].copy()

plt.figure(figsize=(10, 5))

for country in countries:

    country_data = comparison[
        comparison["country"] == country
    ]

    plt.plot(
        country_data["year"],
        country_data["primary_energy_consumption"],
        label=country
    )

plt.title("Primary Energy Consumption Comparison")
plt.xlabel("Year")
plt.ylabel("Primary Energy Consumption")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()