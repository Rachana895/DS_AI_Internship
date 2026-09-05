import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load real-world dataset
df = sns.load_dataset("iris")

# Basic information
print(df.head())
print("\nShape:", df.shape)
print("\nStatistics:")
print(df.describe())

# Univariate analysis
df.hist(figsize=(8, 6))
plt.show()

# Bivariate analysis
sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species")
plt.show()

# Skewness
print("\nSkewness:")
print(df.select_dtypes("number").skew())

# Correlation analysis
print("\nCorrelation:")
print(df.select_dtypes("number").corr())

sns.heatmap(df.select_dtypes("number").corr(), annot=True)
plt.show()

# Outlier detection using boxplot
sns.boxplot(data=df.select_dtypes("number"))
plt.show()

# Missing values
print("\nMissing values:")
print(df.isnull().sum())