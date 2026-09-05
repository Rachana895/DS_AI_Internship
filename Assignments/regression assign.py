import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Student dataset
data = {
    "Attendance": [60, 70, 80, 90, 95, 65, 75, 85],
    "StudyHours": [2, 3, 4, 5, 6, 2, 4, 5],
    "FinalMarks": [50, 60, 70, 80, 90, 55, 68, 82]
}

df = pd.DataFrame(data)

# Supervised Learning
X = df[["Attendance", "StudyHours"]]
y = df["FinalMarks"]

model = LinearRegression()
model.fit(X, y)

print("Predicted marks:", round(model.predict([[85, 5]])[0], 2))

# Unsupervised Learning
kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
df["Group"] = kmeans.fit_predict(X)

print("\nStudent Groups:")
print(df)