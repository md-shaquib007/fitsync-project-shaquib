import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Generate date range for the past 365 days leading up to today
end_date = datetime.now()
start_date = end_date - timedelta(days=364)
dates = [start_date + timedelta(days=i) for i in range(365)]

# Generate synthetic data
steps = np.random.normal(loc=8500, scale=2200, size=365).clip(3000, 18000)
sleep_hours = np.random.normal(loc=7.2, scale=1, size=365).clip(4.5, 9.5)
heart_rate = np.random.normal(loc=68, scale=10, size=365).clip(48, 110)
calories_burned = np.random.randint(1800, 4200, size=365)
active_minutes = np.random.randint(20, 180, size=365)

# Create DataFrame
fitness_data = pd.DataFrame({
    'Date': dates,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Introduce 5% missing values randomly in each column
for column in fitness_data.columns[1:]:  # exclude 'Date' column
    fitness_data.loc[fitness_data.sample(frac=0.05).index, column] = np.nan

# Save to CSV
fitness_data.to_csv('data/health_data.csv', index=False)

print("Synthetic fitness data generated and saved to 'data/health_data.csv'")
