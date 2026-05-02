import pandas as pd

# Function to load and process health data from a CSV file
def load_data():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/health_data.csv')
    
    # Fill missing 'Steps' with the median of that column
    df['Steps'] = df['Steps'].fillna(df['Steps'].median())
    
    # Fill missing 'Sleep_Hours' with a default value of 7.0
    df['Sleep_Hours'] = df['Sleep_Hours'].fillna(7.0)
    
    # Fill missing 'Heart_Rate_bpm' with a default value of 68
    df['Heart_Rate_bpm'] = df['Heart_Rate_bpm'].fillna(68)
    
    # Fill other columns with their respective median
    df = df.fillna(df.median(numeric_only=True))
    
    # Convert 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    
    return df

# Function to calculate recovery score and add it to the DataFrame
def calculate_recovery_score(df):
    # Initialize Recovery_Score with a base value of 50
    df['Recovery_Score'] = 50

    # Adjust score based on Sleep_Hours
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20  # Good sleep
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 20   # Poor sleep

    # Adjust score inversely based on Heart_Rate_bpm
    df['Recovery_Score'] -= (df['Heart_Rate_bpm'] - 60) * 0.3  # Lower heart rate is better

    # Adjust score for high activity
    df['Recovery_Score'] -= (df['Steps'] - 10000) / 1000  # High steps might slightly reduce recovery

    # Ensure Recovery_Score stays within 0 to 100
    df['Recovery_Score'] = df['Recovery_Score'].clip(0, 100)

    return df

def process_data():
    df = load_data()  # Call to load and clean the data
    df = calculate_recovery_score(df)  # Add the recovery score
    return df  # Return the final processed DataFrame

