import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Read dataset
data = pd.read_csv("house_loan.csv")

print("Dataset:")
print(data)

# Convert Yes/No into numbers
encoder = LabelEncoder()

data["Employment"] = encoder.fit_transform(data["Employment"])
data["Eligibility"] = encoder.fit_transform(data["Eligibility"])

# Input features
X = data[["Age", "Income", "Credit_Score", "Employment", "Existing_Loans"]]

# Output
y = data["Eligibility"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

print("\nAccuracy:", accuracy)

# Predict for a new person
new_person = [[35, 45000, 700, 1, 0]]

prediction = model.predict(new_person)

if prediction[0] == 1:
    print("\nHouse Loan Status: Eligible")
else:
    print("\nHouse Loan Status: Not Eligible")