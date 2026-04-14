import pandas as pd

# Load the CSV file
df = pd.read_csv('data/health_data.csv')

# Print the first 5 rows
print("First 5 rows:")
print(df.head())

# Calculate the number of missing values in each column
missing_values = df.isna().sum()

# Print the number of missing values
print("\nNumber of missing values in each column:")
print(missing_values)