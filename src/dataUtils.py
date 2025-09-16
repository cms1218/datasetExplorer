import pandas as pd
from os import path

# Implement CSV Loading Functionality and return dataframe
def load_CSV():
    file_path = input("Enter the path to the file: ")
    if not path.exists(file_path):
        print("File does not exist.")
        return None
    return pd.read_csv(file_path)
