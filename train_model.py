# Import Libraries

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import joblib

# Read the dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

for column in dataset.select_dtypes(include=['int64', 'float64']).columns:
    plt.figure(figsize=(8,5))
    sns.histplot(dataset[column], kde=True)
    plt.title(f"Distribution Plot of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# Box Plot
for column in dataset.select_dtypes(include=['int64', 'float64']).columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x=dataset[column])
    plt.title(f"Box Plot of {column}")
    plt.xlabel(column)
    plt.show()
