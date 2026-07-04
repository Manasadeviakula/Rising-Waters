import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Read the dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Create LabelEncoder object
le = LabelEncoder()

# Select categorical columns
categorical_columns = dataset.select_dtypes(include=['object']).columns

# Apply Label Encoding
for column in categorical_columns:
    dataset[column] = le.fit_transform(dataset[column])

print(dataset.head())