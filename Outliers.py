import pandas as pd

# Read the dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Select numerical columns
numerical_columns = dataset.select_dtypes(include=['int64', 'float64']).columns

# Apply IQR Capping
for column in numerical_columns:

   # Outlier Handling for Annual Rainfall

    Q1 = dataset['ANNUAL'].quantile(0.25)
    Q3 = dataset['ANNUAL'].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    dataset['ANNUAL'] = dataset['ANNUAL'].clip(lower=lower_limit,
                                            upper=upper_limit)
print("Outliers handled successfully using IQR Capping.")