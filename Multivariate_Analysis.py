import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
dataset = pd.read_excel("dataset/flood dataset.xlsx")

# Correlation Matrix
correlation_matrix = dataset.corr(numeric_only=True)

# Heat Map
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)

plt.title("Correlation Heat Map")
plt.show()