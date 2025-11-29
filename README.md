# Malawi Climate Tracker

Interactive dashboard analyzing historical temperature trends across Malawi's 3 major cities from 1950 to present. This project visualizes warming patterns and climate anomalies to communicate climate change impacts at a local level.

## Overview

This Streamlit application provides an accessible way to explore long-term temperature trends in Malawi, using data from the [Open-Meteo Historical Weather API](https://open-meteo.com/). The dashboard calculates temperature anomalies, displays warming trends, and helps communicate climate science to a broader audience.

### Cities Analyzed

- **Lilongwe** (Central Region)
- **Blantyre** (Southern Region)
- **Mzuzu** (Northern Region)

## Features

- **Historical Temperature Data**: Daily mean temperatures from 1950 to present
- **Interactive Visualizations**:
  - Yearly temperature trends with 5-year moving average
  - Warming stripes showing temperature anomalies from baseline (1950-1979)
- **Climate Metrics**:
  - Historic baseline average (1950-1979)
  - Modern average (2010-present)
  - Warming impact calculation

## Tech Stack

- **Python 3.8+**
- **Streamlit**: Interactive web framework
- **Pandas**: Data processing and aggregation
- **Plotly**: Interactive charts
- **Requests**: API data fetching

## Running Locally

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**:

   ```bash
   streamlit run app.py
   ```

3. **View**: Open your browser at `http://localhost:8501`

## Data Source

All temperature data is sourced from [Open-Meteo](https://open-meteo.com/), a free weather API providing historical climate data from 1950 onwards.

## Related Work

This dashboard complements my [statistical analysis of Malawi's temperature trends](https://github.com/Jimmy-JayJay/malawi_temp_trend_analysis), where I used Mann-Kendall trend tests to detect significant warming patterns from 1950-2014.

## Author

Built by [Jimmy Matewere](https://github.com/Jimmy-JayJay) - Climate Scientist & Data Analyst
