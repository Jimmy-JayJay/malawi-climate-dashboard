# Climate Change Dashboard 🌍

An interactive dashboard visualizing historical temperature trends and climate change data for major global cities.

## Features

- **Historical Data**: Fetches daily weather data from 1950 to present using the [Open-Meteo API](https://open-meteo.com/).
- **Interactive Charts**:
  - Yearly Average Temperature Trends (with 5-year moving average).
  - "Warming Stripes" Anomaly Visualization.
- **Global Coverage**: Switch between cities like Lilongwe, London, New York, and Tokyo.

## Tech Stack

- **Python 3.8+**
- **Streamlit**: Web framework.
- **Pandas**: Data processing.
- **Plotly**: Interactive visualizations.
- **Requests**: API fetching.

## How to Run Locally

1.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the App**:

    ```bash
    streamlit run app.py
    ```

3.  **View**: Open your browser at `http://localhost:8501`.
