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

def missing_values_table(df : pd.DataFrame):
    # Collect missing values
    missing_val = df.isnull().sum()

    # Determine percentage of missing values
    missing_val_percent = missing_val / len(df) * 100

    # Create table of missing values (pd.concat returns a DataFrame)
    missing_val_table = pd.concat([missing_val, missing_val_percent], axis = 1)
    missing_val_table.columns = ['Missing Values', '% of Total Values']
    
    # Drop Rows that have no missing values from missing_value table
    missing_val_table = missing_val_table[missing_val_table['Missing Values'] > 0]
    missing_val_table = missing_val_table.sort_values('% of Total Values', ascending = False)
    
    print(missing_val_table)

# Handle missing values
def handle_missing(
    df : pd.DataFrame,
    dropThresh: float = .6,
    num_fill: str = "mean",
    cat_fill: str = "mode"
    ) -> pd.DataFrame:
    
    # Drop columns with more missing values than the threshold allows
    df = df.dropna(axis = 1, thresh = int((1-dropThresh)*len(df)))
    
    # Iterate over columns and if numeric and not dropped, fill them with chosen strategy
    for col in df:
        if pd.api.types.is_numeric_dtype(df[col]):
            if num_fill.lower() == "mean":
                df[col] = df[col].fillna(df[col].mean())
            elif num_fill.lower() == "median":
                df[col] = df[col].fillna(df[col].median())
            else:
                try:
                    df[col] = df[col].fillna(float(num_fill))
                except Exception as e:
                    print("Invalid num_fill strategy entered. Defaulting to mean")
                    df[col] = df[col].fillna(df[col].mean())
        # Categorical missing value handling
        if not(pd.api.types.is_numeric_dtype):
            df[col] = df[col].fillna(df[col].mode())
 
    return df

def missing_value_interaction(df : pd.DataFrame) -> pd.DataFrame:
    missing_values_table(df)

    print("Would you like to alter the dataset to account for missing values? ")
    while (True):
        choice = int(input("Please enter your preference(Yes=1, No=2): "))

        if (choice == 1):
            # Collect args for handle_missing
            drop = float(input("Please enter the threshold of missing values necessary to drop a column: "))
            num_fill = input("Please input fill preferences for numerical data: ")
            cat_fill = input("Please input fill preferences for categorical data: ")
            df = handle_missing(df, drop, num_fill, cat_fill)
            return df
        elif choice == 2:
            print("Missing Value Management skipped. ")
            break
        else:
            print("Invalid input.")
    return df

# Generate summary statistics for each column
def summaryStats(df) -> dict:
    sumStatsList = {}
    for col in df:
        if pd.api.types.is_numeric_dtype(df[col]):
            tempDict = {}
            tempDict["Mean"] = df[col].mean()
            tempDict["Median"] = df[col].median()
            tempDict["Std"] = df[col].std()
            tempDict["Min"] = df[col].min()
            tempDict["Max"] = df[col].max()
            tempDict["Missing"] = df[col].isna().sum()
            sumStatsList[col] = tempDict
        else:
            # Convert series returned by value_counts() to dict
            pass
    return sumStatsList


def outlier(df):
    pass

