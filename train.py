import pandas as pd
import numpy as np
import joblib
import warnings
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, recall_score
from imblearn.over_sampling import SMOTE
warnings.filterwarnings("ignore")
if not os.path.exists("models"):
    os.makedirs("models")
    print("Created 'models' folder")
dataset = pd.read_excel("data/flood dataset.xlsx")
print("\nDataset Loaded!")
print(f" Shape: {dataset.shape}")
FEATURES = ['Temp', 'Humidity', 'Cloud Cover', 'ANNUAL', 
            'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec', 
            'avgjune', 'sub']
TARGET = 'flood'
X = dataset[FEATURES]
y = dataset[TARGET]
print(y.value_counts())
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)
print(f"Original: {len(X)} samples")
print(f" Resampled: {len(X_resampled)} samples")
print(f"New distribution:\n{pd.Series(y_resampled).value_counts()}")
X = X_resampled
y = y_resampled
print("\n🔍 Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print(f"Train: {len(X_train)} samples")
print(f"Test: {len(X_test)} samples")
print("\n🔍 Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
joblib.dump(scaler, "models/transform.save")
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=8,
    random_state=42,
    class_weight='balanced'
)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print(f" Accuracy: {acc:.4f}")
print(f"Recall: {recall:.4f}")
joblib.dump(model, "models/floods.save")
print("\n Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\n Classification Report:")
print(classification_report(y_test, y_pred, target_names=['SAFE', 'FLOOD']))