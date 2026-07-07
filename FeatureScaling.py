import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Read the dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Independent Variables
X = dataset.iloc[:, 0:10].values

# Dependent Variable
y = dataset.iloc[:, 10].values

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=10
)

# Feature Scaling
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Save the scaler
joblib.dump(sc, "scaler.pkl")

print("Feature Scaling Completed Successfully!")
print("Scaler Saved as scaler.pkl")