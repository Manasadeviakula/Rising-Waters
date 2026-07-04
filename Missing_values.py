import pandas as pd

# Read the dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Check missing values in each column
print("Missing Values in Each Column:")
print(dataset.isnull().sum())

# Check if any missing values exist
print("\nAny Missing Values?")
print(dataset.isnull().any())