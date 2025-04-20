import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

def predict(df):
    """
    Predicts future traffic demand using Exponential Smoothing.
    - Aggregates ride demand per hour
    - Trains a forecasting model
    - Predicts demand for the next 24 hours
    """
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.floor('H')
    hourly_demand = df.groupby('pickup_hour').size()

    # Train a time series model
    model = ExponentialSmoothing(hourly_demand, seasonal='add', seasonal_periods=24).fit()
    future_demand = model.forecast(24)

    # Plot predictions
    plt.figure(figsize=(10, 5))
    plt.plot(hourly_demand.index, hourly_demand, label="Historical Demand")
    plt.plot(future_demand.index, future_demand, label="Predicted Demand", linestyle="dashed", color="red")
    plt.xlabel("Time")
    plt.ylabel("Number of Rides")
    plt.title("Traffic Demand Prediction for Next 24 Hours")
    plt.legend()
    plt.show()

    print("Prediction complete. Future demand forecasted.")

if __name__ == "__main__":
    df_cleaned = pd.read_parquet("data/cleaned_data.parquet")  
    predict(df_cleaned)
