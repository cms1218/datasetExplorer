import pandas as pd
from os import path


# Implement CSV Loading Functionality and return dataframe 
def load_csv(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"CSV file loaded successfully from {path}")
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        exit(1)

# Handle missing values in the dataframe
def check_missing_values(df):
    # Returns number of missing values in each column
    return df.isnull().sum()
# Create histogram for a specified column

# Create scatter plot for two specified columns

# Generate summary statistics for the dataframe


