import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Read dataset
data = pd.read_csv("salary data.csv")

print("Dataset:")
print(data)

# Input and output
X = data[["Experience", "Education", "Working_Hours"]]
y = data["Salary"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

print("\nActual Salary:")
print(y_test.values)

print("\nPredicted Salary:")
print(y_pred.astype(int))

# Model evaluation
print("\nMean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Predict salary for a new employee
new_employee = [[7, 16, 42]]

predicted_salary = model.predict(new_employee)

print("\nPredicted Salary for New Employee: ₹", int(predicted_salary[0]))