import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Add caching for data processing step
def load_data():
    return process_data()

# Set up the page configuration
st.set_page_config(layout="wide", page_title="Trends & Insights")

# Add a title to the app
st.title("Trends & Insights")

# Process and load the data with caching
df = st.cache_data(load_data)()
# Sidebar for filters
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Filter the dataframe based on the time range
df['Date'] = pd.to_datetime(df['Date'])
if time_range == "Last 7 Days":
    filtered_df = df[df['Date'] >= pd.to_datetime('today') - pd.Timedelta(days=7)]
elif time_range == "Last 30 Days":
    filtered_df = df[df['Date'] >= pd.to_datetime('today') - pd.Timedelta(days=30)]
else:
    filtered_df = df

# Ensure 'Date' is a datetime object and handle errors
try:
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], errors='coerce')
    if filtered_df['Date'].isnull().any():
        st.warning("Some dates in the dataset are invalid and will not be used in the monthly calculations.")
except Exception as e:
    st.error(f"An error occurred while converting dates: {e}")

# Calculate summary statistics
summary = filtered_df.agg({
    "Recovery_Score": ['mean', 'min', 'max'],
    "Sleep_Hours": ['mean', 'min', 'max'],
    "Steps": ['mean', 'min', 'max'],
    "Calories_Burned": ['mean', 'min', 'max'],
}).T

# Display summary statistics
st.subheader("Summary Statistics")
st.dataframe(summary)

# Line chart for average Recovery Score month-wise
to_resample_df = filtered_df.dropna(subset=['Date'])  # Drop rows where 'Date' conversion failed
monthly_avg_recovery = to_resample_df.resample('M', on='Date').mean(numeric_only=True)
line_chart_recovery = px.line(
    monthly_avg_recovery, y='Recovery_Score',
    title="Average Monthly Recovery Score",
    labels={'Recovery_Score': 'Average Recovery Score'},
    template="plotly_white"
)

# Display line chart
st.plotly_chart(line_chart_recovery, use_container_width=True)

# Histograms
hist_steps = px.histogram(filtered_df, x='Steps', title='Distribution of Steps', template="plotly_white")
hist_calories = px.histogram(filtered_df, x='Calories_Burned', title='Distribution of Calories Burned', template="plotly_white")
hist_recovery = px.histogram(filtered_df, x='Recovery_Score', title='Distribution of Recovery Score', template="plotly_white")
hist_sleep = px.histogram(filtered_df, x='Sleep_Hours', title='Distribution of Sleep Hours', template="plotly_white")

# Display histograms
st.subheader("Distributions of Key Metrics")
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(hist_steps, use_container_width=True)
    st.plotly_chart(hist_recovery, use_container_width=True)

with col2:
    st.plotly_chart(hist_calories, use_container_width=True)
    st.plotly_chart(hist_sleep, use_container_width=True)

