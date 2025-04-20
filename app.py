import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="Smart Traffic Forecast", layout="wide")

# --- Load Parquet Locally ---
@st.cache_data
def load_local_parquet():
    return pd.read_parquet("demand_prediction.parquet")

df = load_local_parquet()

# --- Preprocess ---
df['ds'] = pd.to_datetime(df['ds'])
df['hour'] = df['ds'].dt.hour
df['date'] = df['ds'].dt.date

# --- Title & Description ---
st.title("📊 Smart Traffic Demand Prediction")
st.markdown("Hourly demand forecast using Prophet ML model on NYC Yellow Taxi data.")

# --- Time Filter Slider ---
min_time = df['ds'].min().to_pydatetime()
max_time = df['ds'].max().to_pydatetime()

selected_range = st.slider(
    "🕐 Select forecast window", 
    min_value=min_time, 
    max_value=max_time, 
    value=(min_time, max_time)
)

df_filtered = df[(df['ds'] >= selected_range[0]) & (df['ds'] <= selected_range[1])]

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("📈 Max Demand", f"{df_filtered['yhat'].max():,.0f}")
col2.metric("📉 Min Demand", f"{df_filtered['yhat'].min():,.0f}")
col3.metric("📊 Avg Demand", f"{df_filtered['yhat'].mean():,.0f}")

# --- Line Chart ---
fig = px.line(df_filtered, x='ds', y='yhat', title="Hourly Forecasted Traffic Demand")
st.plotly_chart(fig, use_container_width=True)

# --- Data Table (optional) ---
with st.expander("🔍 View Raw Forecast Data"):
    st.dataframe(df_filtered)

# --- Footer ---
st.caption("Built by Rahul Ram • Powered by Python, Streamlit, and ML")
