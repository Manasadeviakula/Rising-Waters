import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn import ensemble
from sklearn import neighbors
from sklearn import metrics
from xgboost import XGBClassifier

# ==========================
# Read Dataset
# ==========================
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# ==========================
# Independent & Dependent Variables
# ==========================
X = dataset.iloc[:, 0:10].values
y = dataset.iloc[:, 10].values

# ==========================
# Train Test Split
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=10
)

# ==========================
# Feature Scaling
# ==========================
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# ==========================
# Create Models
# ==========================
dtree = tree.DecisionTreeClassifier(random_state=42)

rf = ensemble.RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

knn = neighbors.KNeighborsClassifier(
    n_neighbors=5
)

xgb = XGBClassifier(
    random_state=42,
    eval_metric="logloss"
)

# ==========================
# Train Models
# ==========================
dtree.fit(X_train, y_train)

rf.fit(X_train, y_train)

knn.fit(X_train, y_train)

xgb.fit(X_train, y_train)


# ==========================
# Compare Models
# ==========================
def compareModel():

    print("\n========== MODEL COMPARISON ==========\n")

    # Predictions
    p1 = dtree.predict(X_test)
    p2 = rf.predict(X_test)
    p3 = knn.predict(X_test)
    p4 = xgb.predict(X_test)

    # Accuracy
    acc1 = metrics.accuracy_score(y_test, p1)
    acc2 = metrics.accuracy_score(y_test, p2)
    acc3 = metrics.accuracy_score(y_test, p3)
    acc4 = metrics.accuracy_score(y_test, p4)

    print("Decision Tree Accuracy :", acc1)
    print("Random Forest Accuracy :", acc2)
    print("KNN Accuracy           :", acc3)
    print("XGBoost Accuracy       :", acc4)

    # Confusion Matrix
    print("\n========== CONFUSION MATRICES ==========\n")

    print("Decision Tree")
    print(metrics.confusion_matrix(y_test, p1))

    print("\nRandom Forest")
    print(metrics.confusion_matrix(y_test, p2))

    print("\nKNN")
    print(metrics.confusion_matrix(y_test, p3))

    print("\nXGBoost")
    print(metrics.confusion_matrix(y_test, p4))

    # Classification Report
    print("\n========== CLASSIFICATION REPORTS ==========\n")

    print("Decision Tree")
    print(metrics.classification_report(y_test, p1))

    print("Random Forest")
    print(metrics.classification_report(y_test, p2))

    print("KNN")
    print(metrics.classification_report(y_test, p3))

    print("XGBoost")
    print(metrics.classification_report(y_test, p4))

    # ==========================
    # Select Best Model
    # ==========================
    best_model = xgb

    print("\n========== FINAL MODEL ==========")
    print("Selected Model : XGBoost")
    print("Accuracy       :", acc4)

    # Save Model
    joblib.dump(best_model, "model.pkl")
    joblib.dump(sc, "scaler.pkl")

    print("\nmodel.pkl saved successfully.")
    print("scaler.pkl saved successfully.")


# ==========================
# Function Call
# ==========================
compareModel()