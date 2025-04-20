import pandas as pd

# Load the Parquet dataset
df = pd.read_parquet("data/yellow_tripdata_2025-01.parquet")

# Display basic info
print(df.info())
print(df.head())
