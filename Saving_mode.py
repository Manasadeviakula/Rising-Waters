import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
from xgboost import XGBClassifier

# Read Dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Independent Variables
X = dataset.iloc[:, 0:10].values

# Dependent Variable
y = dataset.iloc[:, 10].values

# Train Test Split
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

# Create XGBoost Model
xgb = XGBClassifier(
    random_state=42,
    eval_metric='logloss'
)

# Train Model
xgb.fit(X_train, y_train)

# Prediction
p4 = xgb.predict(X_test)

# Evaluation
print(confusion_matrix(y_test, p4))
print(accuracy_score(y_test, p4))
print(precision_score(y_test, p4))
print(recall_score(y_test, p4))

# Save Model
joblib.dump(xgb, "floods.save")

# Save Scaler
joblib.dump(sc, "transform.save")

print("\nModel saved successfully as floods.save")
print("Scaler saved successfully as transform.save")