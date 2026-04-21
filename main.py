import streamlit as st
from modules.processor import process_data
import pandas as pd

# Set up the page configuration
st.set_page_config(layout="wide", page_title="FitSync")

# Add a title to the app
st.title("FitSync - Personal Health Analytics")

# Process and load the data
df = process_data()

# Sidebar for filters
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Filter the dataframe based on the selected time range
if time_range == "Last 7 Days":
    df = df[df['Date'] >= pd.to_datetime('today') - pd.Timedelta(days=7)]
elif time_range == "Last 30 Days":
    df = df[df['Date'] >= pd.to_datetime('today') - pd.Timedelta(days=30)]

# Re-calculate average values from the filtered DataFrame
average_steps = df['Steps'].mean()
average_sleep_hours = df['Sleep_Hours'].mean()
average_recovery_score = df['Recovery_Score'].mean()

# Display metrics in the columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Average Steps", value=int(average_steps), delta=None)

with col2:
    st.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)

with col3:
    st.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)

# Display a section for the processed data
st.subheader("Processed Health Data")
st.dataframe(df)

# Future sections for more detailed analytics and visualizations
# st.subheader("Additional Insights")
# st.write("Additional insights and visualizations will be added here.")

