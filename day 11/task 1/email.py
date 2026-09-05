# Develop a Machine Learning model to classify an email as Spam or Not Spam based on simple email features, and evaluate the model using a confusion matrix, accuracy, precision, and recall.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score


# Read dataset
data = pd.read_csv("email spam.csv")

print("Dataset:")
print(data)


# Input and output
X = data[["Free_Words", "Links", "Unknown_Sender"]]
y = data["Spam"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)


# Predict
y_pred = model.predict(X_test)

print("\nActual:")
print(y_test.values)

print("\nPredicted:")
print(y_pred)


# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# Precision
precision = precision_score(
    y_test, y_pred, pos_label="Spam"
)

print("Precision:", precision)


# Recall
recall = recall_score(
    y_test, y_pred, pos_label="Spam"
)

print("Recall:", recall)