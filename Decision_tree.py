import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
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

# Decision Tree Function
def decisiontree(X_train, X_test, y_train, y_test):

    # Initialize Model
    dtree = DecisionTreeClassifier()

    # Train Model
    dtree.fit(X_train, y_train)

    # Prediction
    y_pred = dtree.predict(X_test)

    # Accuracy
    print("Decision Tree Accuracy")
    print(accuracy_score(y_test, y_pred))

    # Confusion Matrix
    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, y_pred))

    # Classification Report
    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    return dtree

# Call Function
decisiontree(X_train, X_test, y_train, y_test)