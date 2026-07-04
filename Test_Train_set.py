import pandas as pd
from sklearn.model_selection import train_test_split

# Read the dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Independent variables
X = dataset.iloc[:, 0:10].values

# Dependent variable
y = dataset.iloc[:, 10].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=10
)

# Display shapes
print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("y_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)