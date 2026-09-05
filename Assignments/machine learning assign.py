import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Temperature": [25, 30, 35, 20, 28, 32, 22, 27],
    "Appliances": [3, 5, 6, 2, 4, 7, 2, 4],
    "Consumption": [120, 200, 250, 90, 160, 280, 100, 150]
}

df = pd.DataFrame(data)

# Input and output
X = df[["Temperature", "Appliances"]]
y = df["Consumption"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction
result = model.predict(pd.DataFrame([[30, 5]], 
                    columns=["Temperature", "Appliances"]))

print("Predicted electricity consumption:", round(result[0], 2))