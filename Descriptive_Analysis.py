import pandas as pd

# Read the dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Display first 5 rows
print("First 5 Rows:")
print(dataset.head())

# Display dataset information
print("\nDataset Information:")
dataset.info()

# Display statistical summary
print("\nStatistical Summary:")
print(dataset.describe())

# Display data types
print("\nData Types:")
print(dataset.dtypes)