import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Improve plot appearance
sns.set(style="whitegrid")

# ----------------------------------------------------------
# STEP 2 — Load / Create Dataset
# (In real projects: df = pd.read_csv("dataset.csv"))
# ----------------------------------------------------------
data = {
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Gender": ["M","F","M","M","F","F","M","M","F","F","M","F"]
}

df = pd.DataFrame(data)

# ----------------------------------------------------------
# TOPIC 3 — BIVARIATE ANALYSIS
# Study relationship between TWO variables
# ----------------------------------------------------------

# SCATTER PLOT — Age vs Salary
plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.show()

# SCATTER PLOT — Experience vs Salary
plt.figure()
sns.scatterplot(x="Experience", y="Salary", data=df)
plt.title("Experience vs Salary")
plt.show()

# BOXPLOT — Salary by Gender
plt.figure()
sns.boxplot(x="Gender", y="Salary", data=df)
plt.title("Salary by Gender")
plt.show()

# BOXPLOT — Salary by Department
plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary by Department")
plt.show()
