import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Read dataset
data = pd.read_csv("electricity consumption.csv")

print("Dataset:")
print(data)

# Input features
X = data[["Temperature", "Appliances", "Time_of_Day", "Previous_Usage"]]

# Output
y = data["Electricity_Consumption"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict electricity consumption
y_pred = model.predict(X_test)

print("\nActual Consumption:")
print(y_test.values)

print("\nPredicted Consumption:")
print(y_pred)

# Model evaluation
print("\nMean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Predict for a new household
new_data = [[28, 7, 18, 7.0]]

prediction = model.predict(new_data)

print("\nPredicted Electricity Consumption:",
      round(prediction[0], 2), "kWh")