import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Read Dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Independent Variables
X = dataset.iloc[:, 0:10].values

# Dependent Variable
y = dataset.iloc[:, 10].values

# Train-Test Split
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

# Random Forest Function
def randomForest(X_train, X_test, y_train, y_test,
                 n_estimators=100,
                 random_state=42):

    print("\n========== RANDOM FOREST MODEL BUILDING ==========")

    # Initialize Random Forest Classifier
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )

    print(f"[INFO] RandomForestClassifier initialized with n_estimators={n_estimators}, random_state={random_state}")

    # Train the Model
    model.fit(X_train, y_train)
    print("[INFO] Model training completed.")

    # Predict on Test Data
    y_pred = model.predict(X_test)
    print("[INFO] Prediction completed on test data.")

    # Evaluate the Model
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)

    # Display Results
    print(f"\n[RESULT] Accuracy: {accuracy:.4f}")

    print("\nConfusion Matrix:")
    print(cm)

    print("\nClassification Report:")
    print(cr)

    # Return Model and Predictions
    return model, y_pred


# Function Call
model_rf, y_pred_rf = randomForest(
    X_train,
    X_test,
    y_train,
    y_test
)