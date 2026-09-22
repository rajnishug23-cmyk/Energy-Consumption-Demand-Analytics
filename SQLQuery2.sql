use EnergyAnalytics;


-- 1. Dataset overview
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT country) AS total_countries,
    MIN(year) AS first_year,
    MAX(year) AS latest_year
FROM energy_data;


-- 2. India's energy consumption trend
SELECT
    year,
    primary_energy_consumption,
    energy_per_capita
FROM energy_data
WHERE country = 'India'
ORDER BY year;


-- 3. Latest available data for India
SELECT TOP 1
    country,
    year,
    primary_energy_consumption,
    energy_per_capita,
    oil_consumption,
    gas_consumption,
    coal_consumption,
    nuclear_consumption,
    hydro_consumption,
    solar_consumption,
    wind_consumption
FROM energy_data
WHERE country = 'India'
ORDER BY year DESC;


-- 4. India vs China vs United States
SELECT
    country,
    year,
    primary_energy_consumption
FROM energy_data
WHERE country IN ('India', 'China', 'United States')
ORDER BY year, country;


-- 5. India's year-over-year growth
SELECT
    year,
    primary_energy_consumption,
    LAG(primary_energy_consumption)
        OVER (ORDER BY year) AS previous_year_consumption,

    (
        primary_energy_consumption
        - LAG(primary_energy_consumption)
          OVER (ORDER BY year)
    )
    /
    NULLIF(
        LAG(primary_energy_consumption)
        OVER (ORDER BY year),
        0
    ) * 100 AS yoy_growth_percent

FROM energy_data
WHERE country = 'India'
ORDER BY year;


-- 6. Highest-consuming countries/entities
SELECT TOP 10
    country,
    primary_energy_consumption
FROM energy_data
WHERE year = (
    SELECT MAX(year)
    FROM energy_data
)
AND primary_energy_consumption IS NOT NULL
ORDER BY primary_energy_consumption DESC;


-- 7. India's energy sources over time
SELECT
    year,
    oil_consumption,
    gas_consumption,
    coal_consumption,
    nuclear_consumption,
    hydro_consumption,
    solar_consumption,
    wind_consumption,
    renewables_consumption
FROM energy_data
WHERE country = 'India'
ORDER BY year;