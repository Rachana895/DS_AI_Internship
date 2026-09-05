# A real-estate company wants to analyze houses in a city.
# Area_sqft
# Bedrooms
# Bathrooms
# Age_Years
# Distance_City_km
# to calculate house prices and group similar houses together.
 


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Read dataset
data = pd.read_csv("house data.csv")

print("Dataset:")
print(data)

# -------------------------------
# SUPERVISED LEARNING
# House Price Prediction
# -------------------------------

X = data[["Area_sqft", "Bedrooms", "Bathrooms", "Age_Years"]]
y = data["Price_Lakh"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

print("\nActual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(prediction)

# Check error
error = mean_absolute_error(y_test, prediction)

print("\nMean Absolute Error:", error)

# Predict price of a new house
new_house = [[1500, 3, 2, 5]]

price = model.predict(new_house)

print("\nPredicted price of new house:",
      round(price[0], 2), "Lakh")


# -------------------------------
# UNSUPERVISED LEARNING
# House Clustering
# -------------------------------

features = data[["Area_sqft", "Bedrooms", "Bathrooms", "Age_Years"]]

# Standardize data
features = StandardScaler().fit_transform(features)

# Create 3 groups
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

data["Cluster"] = kmeans.fit_predict(features)

print("\nHouse Clusters:")
print(data[["Area_sqft", "Bedrooms", "Price_Lakh", "Cluster"]])

# Show clusters
plt.scatter(
    data["Area_sqft"],
    data["Price_Lakh"],
    c=data["Cluster"]
)

plt.xlabel("Area (sqft)")
plt.ylabel("Price (Lakh)")
plt.title("House Clusters")
plt.show()