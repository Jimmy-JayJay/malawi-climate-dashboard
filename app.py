import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

# --- Configuration ---
st.set_page_config(
    page_title="Malawi Climate Tracker",
    page_icon="📊",
    layout="wide"
)

# --- Constants ---
CITIES = {
    "Lilongwe (Central)": {"lat": -13.9626, "lon": 33.7741},
    "Blantyre (South)": {"lat": -15.7861, "lon": 35.0058},
    "Mzuzu (North)": {"lat": -11.4656, "lon": 34.0207}
}

# --- Helper Functions ---
@st.cache_data
def fetch_climate_data(lat, lon):
    """
    Fetches historical weather data from Open-Meteo API.
    """
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    # Fetch data from 1950 to present
    end_date = datetime.now().strftime("%Y-%m-%d")
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "1950-01-01",
        "end_date": end_date,
        "daily": "temperature_2m_mean",
        "timezone": "auto"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Create DataFrame
    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "temperature": data["daily"]["temperature_2m_mean"]
    })
    
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    
    return df

def calculate_yearly_avg(df):
    """Calculates yearly average temperature."""
    return df.groupby("year")["temperature"].mean().reset_index()

# --- Main Layout ---
st.title("Malawi Climate Tracker")
st.markdown("""
Interactive dashboard analyzing historical temperature trends across Malawi's 3 major cities from 1950 to present.  
Built to visualize warming patterns and climate anomalies, communicating climate change impacts at a local level.
""")

# Sidebar
st.sidebar.header("Select Region")
selected_city = st.sidebar.radio("City", list(CITIES.keys()))
coords = CITIES[selected_city]

# Fetch Data
with st.spinner(f"Analyzing climate data for {selected_city}..."):
    try:
        raw_df = fetch_climate_data(coords["lat"], coords["lon"])
        yearly_df = calculate_yearly_avg(raw_df)
        
        # Calculate Metrics
        baseline_temp = yearly_df[yearly_df["year"] < 1980]["temperature"].mean()
        recent_temp = yearly_df[yearly_df["year"] >= 2010]["temperature"].mean()
        warming = recent_temp - baseline_temp
        
        # --- Metrics Row ---
        col1, col2, col3 = st.columns(3)
        col1.metric("Historic Average (1950-79)", f"{baseline_temp:.1f}°C")
        col2.metric("Modern Average (2010s)", f"{recent_temp:.1f}°C")
        col3.metric("Warming Impact", f"{warming:+.1f}°C", delta_color="inverse")
        
        # --- Visualizations ---
        
        # 1. Line Chart
        st.subheader(f"Temperature Trend: {selected_city}")
        fig_line = px.line(
            yearly_df, 
            x="year", 
            y="temperature", 
            labels={"temperature": "Avg Temperature (°C)", "year": "Year"},
            color_discrete_sequence=["#008080"] # Teal color
        )
        
        # Add trendline (rolling average)
        yearly_df["5-year Avg"] = yearly_df["temperature"].rolling(window=5).mean()
        fig_line.add_scatter(
            x=yearly_df["year"], 
            y=yearly_df["5-year Avg"], 
            mode="lines", 
            name="5-Year Trend",
            line=dict(color="#FFA500", width=3) # Orange for contrast
        )
        
        fig_line.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_line, use_container_width=True)
        
        # 2. Warming Stripes (Simplified Bar Chart)
        st.subheader("Warming Stripes Visualization")
        st.markdown("Visualizing the shift from cooler years (Blue) to warmer years (Red).")
        
        yearly_df["anomaly"] = yearly_df["temperature"] - baseline_temp
        
        fig_bar = px.bar(
            yearly_df,
            x="year",
            y="anomaly",
            color="anomaly",
            color_continuous_scale="RdBu_r", # Red-Blue reversed
            range_color=[-1.5, 1.5],
            labels={"anomaly": "Deviation from Baseline (°C)"}
        )
        fig_bar.update_layout(
            showlegend=False,
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# Footer
st.markdown("---")
st.caption("Data Source: [Open-Meteo](https://open-meteo.com/) Historical Weather API | Built by [Jimmy Matewere](https://github.com/Jimmy-JayJay)")
