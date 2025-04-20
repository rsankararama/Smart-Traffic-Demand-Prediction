import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze(df):
    """
    Analyzes and visualizes traffic demand trends.
    - Plots ride demand trends over time
    - Displays demand distribution over different hours
    - Generates a heatmap of pickups
    """
    # Set up Seaborn style
    sns.set_style("darkgrid")

    # Plot hourly ride demand
    df['hour'] = df['tpep_pickup_datetime'].dt.hour
    plt.figure(figsize=(10, 5))
    sns.countplot(x=df['hour'], palette="viridis")
    plt.title("Hourly Ride Demand")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Rides")
    plt.xticks(range(24))
    plt.show()

    # Heatmap of trip pickup locations (requires latitude/longitude data)
    plt.figure(figsize=(8, 6))
    sns.histplot(df['PULocationID'], bins=50, kde=True, color='blue')
    plt.title("Distribution of Pickup Locations")
    plt.xlabel("Pickup Location ID")
    plt.ylabel("Number of Rides")
    plt.show()

    print("Analysis complete. Insights generated.")

if __name__ == "__main__":
    df_cleaned = pd.read_parquet("data/cleaned_data.parquet")  
    analyze(df_cleaned)
