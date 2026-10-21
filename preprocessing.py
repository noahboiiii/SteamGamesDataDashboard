import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

# Name of dataset file on Kaggle link
file_path = "games.csv"

# Load the dataset
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "fronkongames/steam-games-dataset",
  file_path,
)

# Checking for any completely null columns
nullPercentages = df.isna().mean() * 100
print(nullPercentages)

# Upon inspection, Movies columns is completely null so this is dropped
cleanedData = pd.DataFrame(df, copy=True)
cleanedData = cleanedData.drop(columns="Movies")
print(f"cleanedData columns after dropping Movies column: {cleanedData.columns}")

# Decide metrics to display on dashboard

# Remove columns
#             - Not needed for chosen metrics
#             - Unable to be used for visualisations (e.g urls)                  
#             - Which can be calculated with existing columns

# Assess remaining columns with blank values and formatting issues and fix accordingly

# Combat multi valued attributes accordinglyW

