import pandas as pd

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

def missing_values_table(df : pd.DataFrame) -> pd.DataFrame:
    # Collect missing values
    missing_val = df.isnull().sum()

    # Determine percentage of missing values
    missing_val_percent = missing_val / len(df) * 100

    # Create table of missing values
    missing_val_table = pd.concat([missing_val, missing_val_percent], axis = 1)
    missing_val_table = missing_val_table.rename(columns = {0 : 'Missing Values',1 : '% of Total Values'})
    print(missing_val_table)

def handle_missing(df : pd.DataFrame) -> pd.DataFrame:
    missing_values_table(df)
    pass
    


# Create histogram for a specified column

# Create scatter plot for two specified columns

# Generate summary statistics for the dataframe


