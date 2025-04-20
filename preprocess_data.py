import pandas as pd

def preprocess(df):
    """
    Cleans and preprocesses the NYC Taxi dataset.
    - Removes missing values
    - Filters out trips with unrealistic durations or distances
    - Converts datetime columns for time-based analysis
    """
    # Drop rows with missing values
    df = df.dropna()

    # Convert pickup and dropoff times to datetime
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # Calculate trip duration in minutes
    df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60

    # Remove unrealistic trips (too short or too long)
    df = df[(df['trip_duration'] > 1) & (df['trip_duration'] < 180)]

    # Remove trips with zero or negative fare
    df = df[df['total_amount'] > 0]

    print("Preprocessing complete. Data ready for analysis.")
    
    return df

if __name__ == "__main__":
    df = pd.read_parquet("data/yellow_tripdata_2025-01.parquet")  # Load dataset
    df_cleaned = preprocess(df)  
    df_cleaned.to_parquet("data/cleaned_data.parquet", index=False)  # Save cleaned data
