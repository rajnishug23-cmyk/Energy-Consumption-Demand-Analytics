# Energy Consumption Demand Analytics

## 📌 Project Overview

This project analyzes global energy consumption patterns using historical energy data, with a specific focus on India.

The project combines **Python, SQL Server, and Power BI** to perform data cleaning, exploratory analysis, energy-source analysis, trend analysis, and a baseline forecast of India's future primary energy consumption.

The goal is to transform raw energy data into meaningful insights that can support understanding of energy demand, consumption trends, and changes in the energy mix.

---

## 🎯 Objectives

- Analyze historical energy consumption trends.
- Compare energy consumption across major countries/entities.
- Examine India's energy consumption and energy-per-capita trends.
- Analyze India's energy mix across different sources.
- Identify year-over-year changes in energy consumption.
- Develop a 5-year baseline forecast for India's primary energy consumption.
- Build an interactive Power BI dashboard for communicating findings.

---

## 🗂️ Dataset

The project uses the **Our World in Data Energy Dataset**.

The original dataset contains historical information on energy consumption, production, population, GDP, and different energy sources across countries and other entities.

For this analysis, the dataset was filtered to:

- India
- China
- United States
- World

The cleaned dataset includes variables related to:

- Population
- GDP
- Primary energy consumption
- Energy per capita
- Energy per GDP
- Oil consumption
- Gas consumption
- Coal consumption
- Nuclear consumption
- Hydropower consumption
- Solar consumption
- Wind consumption
- Renewable energy consumption

---

## 🛠️ Tools & Technologies

- **Python**
  - Pandas
  - NumPy
  - Matplotlib
- **SQL Server**
  - Data querying
  - Aggregation
  - Window functions
  - Year-over-year analysis
- **Power BI**
  - Interactive dashboards
  - KPI cards
  - Trend analysis
  - Country comparison
  - Energy-source analysis
- **Excel / CSV**
  - Data storage and transfer

---

## 🔄 Project Workflow

### 1. Data Cleaning

The original dataset was loaded using Pandas and filtered to the selected countries/entities.

The cleaning process included:

- Selecting relevant variables
- Filtering the analytical population
- Removing records without a valid year
- Sorting data by country and year
- Exporting the cleaned dataset to CSV

Main script:

`01_data_cleaning.py`

---

### 2. Exploratory Data Analysis

Exploratory analysis was performed to understand:

- Dataset dimensions
- Available years
- Countries/entities included
- Latest available observations
- India's historical energy consumption
- India's energy-source composition
- Year-over-year energy consumption growth

Main script:

`02_eda.py`

---

### 3. Data Visualization

Python visualizations were created to examine:

- India's primary energy consumption trend
- India's energy consumption per capita
- Energy consumption comparison between major countries

Main script:

`03_visualization.py`

---

### 4. Energy Mix Analysis

India's consumption across different energy sources was analyzed, including:

- Oil
- Gas
- Coal
- Nuclear
- Hydropower
- Solar
- Wind

Main script:

`04_energy_mix.py`

---

### 5. Forecasting

A **linear trend baseline model** was used to estimate India's primary energy consumption for the next five years based on historical observations.

The forecast is intended as a baseline analytical exercise rather than a definitive prediction of future energy demand.

Main script:

`05_forecasting.py`

The resulting forecast is stored in:

`data/india_energy_forecast.csv`

---

### 6. Model Evaluation

The historical trend model was evaluated using:

- **MAE — Mean Absolute Error**
- **RMSE — Root Mean Squared Error**

These metrics provide a measure of how closely the fitted trend represents the historical observations.

Main script:

`06_model_evaluation.py`

---

## 🗄️ SQL Analysis

The cleaned dataset was imported into **SQL Server** for analytical querying.

SQL analysis includes:

- Dataset overview
- India's energy consumption trend
- Latest available Indian energy data
- India vs China vs United States comparison
- Year-over-year growth
- Highest-consuming entities
- India's energy-source trends

SQL files:

```text
sql/
├── 01_create_table.sql
├── 02_analysis_queries.sql
└── 03_insights.sql
